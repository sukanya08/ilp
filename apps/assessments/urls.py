from django.conf.urls import url
from assessments.api_views import(
    SurveysViewSet, QuestionGroupViewSet,
    QuestionViewSet, QuestionGroupQuestions,
    QGroupAnswersMetaAPIView, QGroupAnswersVolumeAPIView,
    QGroupStoriesInfoView
)
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter

nested_router = ExtendedSimpleRouter()
simple_router = routers.DefaultRouter()

simple_router.register(
    r'surveys/questions', QuestionViewSet, base_name='survey-questions')

# surveys -> questiongroup -> questions
# maps to earlier programs -> # assessments -> questions

nested_router.register(
    r'surveys',
    SurveysViewSet,
    base_name='surveys').register(
        r'questiongroup',
        QuestionGroupViewSet,
        base_name="surveys-questiongroup",
        parents_query_lookups=['survey']).register(
            r'questions', QuestionGroupQuestions,
            base_name="surveys-questiongroup-questions",
            parents_query_lookups=['survey', 'questiongroup_id']
        )

# surveys -> questiongroup -> answers maps to earlier programs ->
# assessments -> answers
# nested_router.register(
#     r'surveys',
#     SurveysViewSet,
#     base_name='surveys').register(
#         r'questiongroup',
#         QuestionGroupViewSet,
#         base_name="surveys-questiongroup",
#         parents_query_lookups=['survey']).register(
#             r'answers', QuestionGroupAnswers,
#             base_name="surveys-questiongroup-answers",
#             parents_query_lookups=['survey', 'questiongroup_id']
#        )

urlpatterns = [
    url(r'survey/(?P<survey_id>[0-9]+)/storiesinfo',
        QGroupStoriesInfoView.as_view(), name='stories-info')
    url(
        r'survey/(?P<survey_id>[0-9]+)/qgroup/(?P<qgroup_id>[0-9]+)'
        '/answers/meta/',
        QGroupAnswersMetaAPIView.as_view(), name='qgroup-answers-meta'),
    url(
        r'survey/(?P<survey_id>[0-9]+)/qgroup/(?P<qgroup_id>[0-9]+)'
        '/answers/volume/',
        QGroupAnswersVolumeAPIView.as_view(), name='qgroup-answers-volume'),
] + simple_router.urls + nested_router.urls
