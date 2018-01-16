from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from common.mixins import ILPStateMixin
from common.views import ILPViewSet

from boundary.models import BoundaryType, BasicBoundaryAgg, BoundaryStateCode
from assessments.models import (
    Survey, SurveySummaryAgg, SurveyDetailsAgg,
    Source, SurveyBoundaryAgg, SurveyUserTypeAgg,
    SurveyRespondentTypeAgg, SurveyInstitutionAgg,
    SurveyAnsAgg, Question, SurveyQuestionKeyAgg,
    SurveyElectionBoundaryAgg, SurveyClassGenderAgg,
    SurveyClassAnsAgg, SurveyClassQuestionKeyAgg,
    SurveyQuestionGroupQuestionKeyAgg, SurveyQuestionGroupGenderAgg,
    SurveyQuestionGroupGenderCorrectAnsAgg, SurveyClassGenderCorrectAnsAgg,
    SurveyQuestionKeyCorrectAnsAgg, SurveyClassQuestionKeyCorrectAnsAgg,
    SurveyQuestionGroupQuestionKeyCorrectAnsAgg,
    SurveyBoundaryQuestionGroupAgg, SurveyInstitutionQuestionGroupAgg,
    SurveyBoundaryQuestionGroupAnsAgg, SurveyInstitutionQuestionGroupAnsAgg,
    QuestionGroup_Institution_Association,
    QuestionGroup_StudentGroup_Association
)

from common.models import AcademicYear
from assessments.serializers import SurveySerializer
from assessments.filters import SurveyTagFilter
from rest_framework.exceptions import ParseError, APIException
from django.conf import settings


class SurveysViewSet(ILPViewSet, ILPStateMixin):
    '''Returns all surveys'''
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    filter_class = SurveyTagFilter


class SurveyInstitutionDetailAPIView(ListAPIView, ILPStateMixin):

    def list(self, request, *args, **kwargs):
        survey_id = self.request.query_params.get('survey_id', None)
        survey_on = Survey.objects.get(id=survey_id).survey_on
        institution_id = self.request.query_params.get('institution_id', None)
        if survey_on == 'institution':
            res = {}
            qset = QuestionGroup_Institution_Association.objects.filter(
                institution_id=institution_id,
                questiongroup__survey_id=survey_id)
            for qgroup_inst in qset:
                res[qgroup_inst.questiongroup_id] = {
                    "id": qgroup_inst.questiongroup_id,
                    "name": qgroup_inst.questiongroup.name
                }
        else:
            res = {}
            sg_qset = QuestionGroup_StudentGroup_Association.\
                objects.filter(
                    studentgroup__institution_id=institution_id,
                )
            response = {}
            for sgroup_inst in sg_qset:
                sg_name = sgroup_inst.studentgroup.name
                sg_id = sgroup_inst.studentgroup.id
                res[sg_name] = {
                    "id": sg_id, "name": sg_name
                }
                for studgroup_qgroup in sg_qset.filter(
                        questiongroup__survey_id=survey_id):
                    qgroup = studgroup_qgroup.questiongroup
                    res[sg_name][qgroup.id] = {
                        "id": qgroup.id, "name": qgroup.name
                    }
                    response.update(res)
        return Response(response)

'''Returns all survey answers for a specific institution'''
class SurveyInstitutionAnsAggView(ListAPIView, ILPStateMixin):
    queryset = SurveyInstitutionQuestionGroupAnsAgg.objects.all()

    def list(self, request, *args, **kwargs):
        surveyid = self.request.query_params.get('survey_id', None)
        schoolid = self.request.query_params.get('school_id', None)
        questions_list=[]
        if surveyid is not None and schoolid is not None:
            question_answers = SurveyInstitutionQuestionGroupAnsAgg.objects.all().filter(survey_id=surveyid).filter(institution_id=schoolid).distinct('answer_option')
            distinct_questions = SurveyInstitutionQuestionGroupAnsAgg.objects.all().filter(survey_id=surveyid).filter(institution_id=schoolid).distinct('question_desc')
            for question in distinct_questions:
                answers=question_answers.values('answer_option', 'num_answers')
                answer_list={}
                for answer in answers:
                    answer_list[answer['answer_option']]= answer['num_answers']
                answer = {"display_text": question.question_desc,
                          "question_id": question.question_id.id,
                          "answers": answer_list,
                          }
                questions_list.append(answer)

        return Response(questions_list)


class SurveyQuestionGroupDetailsAPIView(APIView):

    response = {}

    def get_from_to(self, queryset, from_monthyear, to_monthyear):
        if from_monthyear:
            from_split = from_monthyear.split('-')
            from_year, from_month = from_split[0], from_split[1]
            queryset = queryset.filter(year__gte=from_year, month__gte=from_month)

        if to_monthyear:
            to_split = to_monthyear.split('-')
            to_year, to_month = to_split[0], to_split[1]
            queryset = queryset.filter(year__lte=to_year, month__lte=to_month)

        return queryset

    def get_boundary_data(self, boundary_id, questiongroup_id, year, from_monthyear, to_monthyear):
        basicqueryset = BasicBoundaryAgg.objects.filter(boundary_id=boundary_id, year=year).values_list('num_schools', flat=True)
        if basicqueryset:
            self.response["summary"]["total_schools"] = basicqueryset[0]
        queryset = SurveyBoundaryQuestionGroupAgg.objects.filter(boundary_id=boundary_id, questiongroup_id=questiongroup_id)
        queryset = self.get_from_to(queryset, from_monthyear, to_monthyear)

        qs_agg = queryset.aggregate(Sum('num_schools'), Sum('num_children'), Sum('num_assessments'))

        self.response["summary"]["schools_impacted"] = qs_agg['num_schools__sum']
        self.response["summary"]["children_impacted"] = qs_agg['num_children__sum']
        self.response["summary"]["num_assessments"] = qs_agg['num_assessments__sum']

        queryset = self.get_from_to(SurveyBoundaryQuestionGroupAnsAgg.objects.filter(boundary_id=boundary_id,   questiongroup_id=questiongroup_id), from_monthyear, to_monthyear)
        return queryset

    def get_institution_data(self, institution_id, questiongroup_id, year, from_monthyear, to_monthyear):
        queryset = SurveyInstitutionQuestionGroupAgg.objects.filter(institution_id=institution_id, questiongroup_id=questiongroup_id)
        queryset = self.get_from_to(queryset, from_monthyear, to_monthyear)

        qs_agg = queryset.aggregate(Sum('num_children'), Sum('num_assessments'))

        self.response["summary"]["total_schools"] = 1
        self.response["summary"]["schools_impacted"] = 1
        self.response["summary"]["children_impacted"] = qs_agg['num_children__sum']
        self.response["summary"]["num_assessments"] = qs_agg['num_assessments__sum']

        queryset = self.get_from_to(SurveyInstitutionQuestionGroupAnsAgg.objects.filter(institution_id=institution_id, questiongroup_id=questiongroup_id), from_monthyear, to_monthyear)
        return queryset

    def get(self, request):
        if not self.request.GET.get('questiongroup'):
            raise ParseError("Mandatory parameter questiongroup not passed")
        questiongroup_id = self.request.GET.get('questiongroup')
        boundary_id = self.request.GET.get('boundary')
        institution_id = self.request.GET.get('institution')
        to_monthyear = self.request.GET.get('to')
        from_monthyear = self.request.GET.get('from')

        year = self.request.GET.get('year', settings.DEFAULT_ACADEMIC_YEAR)
        try:
            academic_year = AcademicYear.objects.get(char_id=year)
        except AcademicYear.DoesNotExist:
            raise APIException('Academic year is not valid.\
                    It should be in the form of 1112.', 404)

        state_id = BoundaryStateCode.objects.filter(char_id=settings.ILP_STATE_ID).values("boundary_id")[0]["boundary_id"]

        self.response["summary"] = {}
        if boundary_id:
            queryset = self.get_boundary_data(boundary_id, questiongroup_id, year, from_monthyear, to_monthyear)
        elif institution_id:
            queryset = self.get_institution_data(institution_id, questiongroup_id, year, from_monthyear, to_monthyear)
        else:
            queryset = self.get_boundary_data(state_id, questiongroup_id, year, from_monthyear, to_monthyear)

        queryset = queryset.values('question_desc', 'answer_option', 'num_answers')

        self.response["questions"] = {}
        for row in queryset:
            if row["question_desc"] in self.response["questions"]:
                self.response["questions"][row["question_desc"]][row["answer_option"]] = row["num_answers"]
            else:
                self.response["questions"][row["question_desc"]] = {"text": row["question_desc"],
                                                                    row["answer_option"]: row["num_answers"]}

        return Response(self.response)
=======
>>>>>>> master
