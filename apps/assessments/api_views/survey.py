import logging

from django.http import Http404

from common.mixins import ILPStateMixin
from common.views import ILPViewSet

from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from assessments.models import (
    Survey, QuestionGroup, Question,
    QuestionGroup_Questions
)
from assessments.serializers import (
    SurveySerializer, QuestionGroupSerializer,
    QuestionSerializer, QuestionGroupQuestionSerializer
)

logger = logging.getLogger(__name__)


class SurveysViewSet(ILPViewSet, ILPStateMixin):
    '''Returns all surveys'''
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    # filter_class = StudentGroupFilter


class QuestionGroupViewSet(
        NestedViewSetMixin, ILPStateMixin, viewsets.ModelViewSet
):
    '''Returns all questiongroups belonging to a survey'''
    queryset = QuestionGroup.objects.all()
    serializer_class = QuestionGroupSerializer

    # M2M query returns duplicates. Overrode this function
    # from NestedViewSetMixin to implement the .distinct()
    def filter_queryset_by_parents_lookups(self, queryset):
        parents_query_dict = self.get_parents_query_dict()
        logger.debug("Arguments passed into view is: %s", parents_query_dict)
        if parents_query_dict:
            try:
                queryset = queryset.filter(
                    **parents_query_dict
                ).order_by().distinct('id')
            except ValueError:
                logger.exception(
                    ("Exception while filtering queryset based on dictionary."
                     "Params: %s, Queryset is: %s"),
                    parents_query_dict, queryset)
                raise Http404
        return queryset.order_by('id')


class QuestionViewSet(ILPStateMixin, viewsets.ModelViewSet):
    '''Return all questions'''
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionGroupQuestions(
        NestedViewSetMixin, ILPStateMixin, viewsets.ModelViewSet
):
    '''Returns all questions belonging to a questiongroup'''
    queryset = QuestionGroup_Questions.objects.all()
    serializer_class = QuestionGroupQuestionSerializer

    # M2M query returns duplicates. Overrode this function
    # from NestedViewSetMixin to implement the .distinct()
    def filter_queryset_by_parents_lookups(self, queryset):
        parents_query_dict = self.get_parents_query_dict()
        print(
            "Arguments passed into QuestionGroupQuestions view is: %s",
            parents_query_dict
        )
        questiongroup = parents_query_dict.get('questiongroup_id')
        print("Question group id is: ", questiongroup)
        if parents_query_dict:
            try:
                queryset = queryset.filter(
                    questiongroup_id=questiongroup
                ).order_by().distinct('id')
            except ValueError:
                logger.exception(
                    ("Exception while filtering queryset based on dictionary."
                     "Params: %s, Queryset is: %s"),
                    parents_query_dict, queryset)
                raise Http404
        return queryset.order_by('id')
