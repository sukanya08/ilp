from rest_framework import viewsets
from django.http import Http404

from schools.models import Student, StudentStudentGroupRelation, StudentGroup
from schools.serializers import StudentSerializer
from common.pagination import LargeResultsSetPagination

class InstituteStudentsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    pagination_class = LargeResultsSetPagination
 
    def get_queryset(self):
        institute = self.request.GET.get('institution_id', None)
        if institute:
            queryset = Student.objects.filter(institution_id = institute).filter(studentstudentgrouprelation__status = 'AC',studentgroup__group_type='class')
            
        else:
            raise Http404
        return queryset