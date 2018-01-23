from datetime import datetime, timedelta

from django.db import transaction
from django.core.management.base import BaseCommand

from schools.models import Institution
from ivrs.utils import get_question
#from common.utils import post_to_slack
from common.models import Status
from ivrs.models import State, QuestionGroupType
from assessments.models import AnswerGroup_Institution,AnswerInstitution, RespondentType, QuestionGroup

class Command(BaseCommand):
    args = ""
    help = """Analyzes the IVRS/SMS states and saves stories.
    ./manage.py fetchgkaivrs"""

    @transaction.atomic
    def handle(self, *args, **options):
        qg_types = QuestionGroupType.objects.filter(is_active=True)
        print ("qg_types is:", qg_types)
        for qg_type in qg_types:
            self.process_state(qg_type)

    def process_state(self, qg_type):
        states = State.objects.filter(qg_type=qg_type, is_processed=False,)

        valid_count = states.filter(is_invalid=False).count()
        invalid_count = states.filter(is_invalid=True).count()
        print ("valid:", valid_count)
        print ("invalid:", invalid_count)

        for state in states:
            state.is_processed = True
            state.save()

            if state.is_invalid:
                continue

            user = state.user
            institution = Institution.objects.get(id=state.school_id)
            date = state.date_of_visit
            akshara_staff = RespondentType.objects.get(name='Akshara Staff')
            question_group = qg_type.questiongroup
            status = Status.objects.get(name = 'Active')
            answergroup, created = AnswerGroup_Institution.objects.get_or_create(
                created_by=user,
                institution=institution,
                is_verified=True,
                questiongroup=question_group,
                date_of_visit=date,
                status = status,
                respondent_type=akshara_staff
            )
            print ("the created:", created)
            for (question_number, answer) in enumerate(state.answers[1:]):
                if answer != 'NA':
                    print("the answer is :", answer)
                    print("the ques is :", question_number)
                    question = get_question(
                        question_number+1,
                        qg_type.questiongroup
                    )
                    answerinstitution = AnswerInstitution.objects.get_or_create(
                        answergroup=answergroup,
                        question=question,
                        answer=answer,
                        double_entry = 0
                    )