from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import ExtendedSimpleRouter

from schools.api_view import (
    InstitutionViewSet, InstitutionInfoViewSet
)
from schools.api_view import (
    StudentViewSet, StudentGroupViewSet, StudentStudentGroupViewSet,
    ProgrammeViewSet
)

nested_router = ExtendedSimpleRouter()
router = DefaultRouter()

router.register(
    r'institutions/list', InstitutionViewSet, base_name='basic')
router.register(
    r'institutions/info', InstitutionInfoViewSet, base_name='info')

# Institution -> StudentGroup -> Students
nested_router.register(
    r'institutions',
    InstitutionViewSet,
    base_name='institution'
    ).register(
        r'studentgroups',
        StudentGroupViewSet,
        base_name='institution-studentgroup',
        parents_query_lookups=['institution']
        ).register(
            r'students',
            StudentViewSet,
            base_name='institution-studentgroup-students',
            parents_query_lookups=[
                'institution', 'studentgroups']
        )

# StudentGroups -> Students -> StudentStudentGroupRelation
nested_router.register(
    r'studentgroups',
    StudentGroupViewSet,
    base_name='studentgroup',
    ).register(
        r'students',
        StudentViewSet,
        base_name='nested_students',
        parents_query_lookups=['studentgroups']
        ).register(
            r'enrollment',
            StudentStudentGroupViewSet,
            base_name='studentstudentgrouprelation',
            parents_query_lookups=['student__studentgroups', 'student']
        )
#  Students -> StudentGroups -> StudentStudentGroupRelation
nested_router.register(
    r'students',
    StudentViewSet,
    base_name='students',
    ).register(
        r'studentgroups',
        StudentGroupViewSet,
        base_name='nested_students',
        parents_query_lookups=['students']
        ).register(
            r'enrollment',
            StudentStudentGroupViewSet,
            base_name='studentstudentgrouprelation',
            parents_query_lookups=['student_id', 'student_group']
        )

## Programme
nested_router.register(
    r'programmes',
    ProgrammeViewSet,
    base_name='programme'
    )
urlpatterns = router.urls + nested_router.urls
