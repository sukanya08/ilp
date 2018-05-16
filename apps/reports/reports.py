import argparse, hashlib, random
from abc import ABC, abstractmethod
from jinja2 import Environment, FileSystemLoader
import pdfkit
import os.path
import datetime

from boundary.models import Boundary
from assessments.models import SurveyInstitutionAgg
from schools.models import Institution
from assessments import models as assess_models
from assessments.models import AnswerGroup_Institution
from .models import Reports, Tracking

class BaseReport(ABC):

    @abstractmethod
    def get_data(self):
        pass

    def generate(self, report_type, output_name):
        if report_type == 'html':
            self.get_html(output_name)
        elif report_type == 'pdf':
            self.get_pdf(output_name)
        else:
            raise ValueError('Invalid report format')

    def get_html(self, output_name):
        env = Environment(loader=FileSystemLoader('apps/reports/report_templates'))
        template = env.get_template(self._template_path)
        data = self.get_data();
        html = template.render(data=data)

        with open('apps/reports/output/{}.html'.format(output_name), 'w') as out_file:
            out_file.write(html)

    def get_pdf(self,output_name):
        if not os.path.exists('apps/reports/output/{}.html'.format(output_name)):
            self.get_html(output_name)
        pdfkit.from_file('apps/reports/output/{}.html'.format(output_name), 'apps/reports/reports_pdf/{}.pdf'.format(output_name))

    def save(self):
        r= Reports(report_type=self._type,parameters=self.params)
        r.link_id = hashlib.sha256(str(random.random()).encode('utf-8')).hexdigest()[:7]
        r.save()
        return r

    def save_link(self, r_id):
        t = Tracking(report_id = r_id, track_id = '5d5dg')
        t.save()

class ReportOne(BaseReport):
    def __init__(self, from_date, to_date):
        self.from_date = from_date
        self.to_date = to_date
        self._template_path  = 'report_one.html'
        self._type = 'reportOne'
        self.params = dict(from_date=self.from_date,to_date=self.to_date)

    def get_data(self):
#        return assess_models.AnswerGroup_Institution.objects.all()[:5]
        return ['name','some','dfdfdfa','dfdafad']

class GPMathContestReport(BaseReport):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--gp_name', required=True)
        self.parser.add_argument('--academic_year', required=True)
        self._template_path = 'math_contest_report.html'
        self._type = 'GPMathContestReport'

    def parse_args(self, args):
        arguments = self.parser.parse_args(args)
        self.gp_name = arguments.gp_name
        self.academic_year = arguments.academic_year
        self.params = dict(gp_name=self.gp_name,academic_year=self.academic_year)

    def get_data(self):
        print(self.gp_name)
        print(self.academic_year)
        gp = self.gp_name #"peramachanahalli"
        ay = self.academic_year #"2016-2017"

        ay2 = ay.split('-')
        dates = [ay2[0]+'-06-01', ay2[1]+'-03-31'] # [2016-06-01, 2017-03-31]

        report_generated_on = datetime.datetime.now().date()

        try:
            gp_obj = Boundary.objects.get(name=gp) # Take the GP from db
        except Boundary.DoesNotExist:
            print('Gram panchayat {} does not exist\n'.format(self.gp_name))
            raise ValueError('Invalid Gram Panchayat name\n')

        block = gp_obj.parent.name           # Block name
        district = gp_obj.parent.parent.name    # District name

        gp_schools = Institution.objects.filter(admin3__name=gp).count() # Number of schools in GP


        # Get the answergroup_institution from gp name and academic year
        AGI = AnswerGroup_Institution.objects.filter(institution__admin3__name=self.gp_name, entered_at__range = dates, respondent_type_id='CH', questiongroup__survey_id=2)
        
        if not AGI.exists():
            raise ValueError("No contests found for {} in the year {}".format(gp, ay))

        num_boys = AGI.filter(answers__question__key='Gender', answers__answer='Male').count()
        num_girls = AGI.filter(answers__question__key='Gender', answers__answer='Female').count()
        number_of_students = num_boys + num_girls

        conditions = AGI.values_list('institution__name', 'questiongroup__name').distinct()
        contests = list(AGI.values_list('answers__question__key', flat=True).distinct())
        contests.pop(contests.index('Gender'))
        schools = []
        scores = {}
        
        for school, qgroup in conditions:
            school_ag = AGI.filter(institution__name=school, questiongroup__name=qgroup)
            for contest in contests:
                percent = []
                for ag in school_ag:
                    num_q = ag.answers.filter(question__key=contest).count()
                    if num_q == 0:
                        continue
                    answered = ag.answers.filter(question__key=contest, answer='Yes').count()
                    mark = (answered/num_q)*100
                    try:
                        scores[ag.id]['mark'].append(mark)
                    except KeyError:
                        scores[ag.id] = dict(mark=[], gender=ag.answers.get(question__key='Gender').answer)
                        scores[ag.id]['mark'].append(mark)
                    percent.append(mark)

                if len(percent) == 0:
                    continue
                details = dict(school=school, grade=qgroup)
                details['contest'] = contest
                details['percent'] = sum(percent)/len(percent)
                schools.append(details)

        #Calculate the perfomance of students
        boys_100 = 0
        girls_100 = 0
        boys_zero = 0
        girls_zero = 0
        for i in scores.values():
            total = sum(i['mark'])/len(i['mark'])
            if total == 100.0:
                if i['gender'] == 'Male':
                    boys_100 += 1
                else:
                    girls_100 += 1
            elif total == 0.0:
                if i['gender'] == 'Male':
                    boys_zero += 1
                else:
                    girls_zero += 1

        score_100 = boys_100 + girls_100
        score_zero = boys_zero + girls_zero

        contest_list = {i['contest'] for i in schools}
        schools_out = []
        out= []

        for item in schools:
            if not item['school'] in schools_out:
                schools_out.append(item['school'])
                out.append({'school':item['school'],
                            'grades':[{
                                'name':item['grade'],
                                'values':[{'contest':item['contest'],'count':item['percent']}]}]
                })
            else:
                for o in out:
                    if o['school']==item['school']:
                        gradeExist= False
                        for grade in o['grades']:
                            if item['grade'] == grade['name']:
                                gradeExist = True
                                grade['values'].append({'contest':item['contest'],'count':item['percent']})
                        if not gradeExist:
                            o['grades'].append({'name':item['grade'],'values':[{'contest':item['contest'],'count':item['percent']}]})

        return {'gp_name': gp, 'academic_year': ay, 'block':block, 'district':district,'no_schools_gp':gp_schools,'no_students':number_of_students,'today':report_generated_on,'boys':num_boys,'girls':num_girls,'schools':out,'cs':contest_list,'score_100':score_100,'score_zero':score_zero,'girls_zero':girls_zero,'boys_zero':boys_zero,'boys_100':boys_100,'girls_100':girls_100}



if __name__ == "__main__":
    r= ReportOne();
    r.get_data