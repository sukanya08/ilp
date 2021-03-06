import logging

from django.http import Http404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status

from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework_bulk import BulkCreateModelMixin

from schools.models import (
    Student, StudentGroup, StudentStudentGroupRelation
)
from schools.serializers import (
    StudentSerializer, StudentGroupSerializer, StudentStudentGroupSerializer
)
from schools.filters import (
    StudentFilter, StudentGroupFilter
)

from common.models import Status

logger = logging.getLogger(__name__)


class StudentViewSet(
        NestedViewSetMixin,
        viewsets.ModelViewSet
):

    queryset = Student.objects.exclude(status=Status.DELETED)
    serializer_class = StudentSerializer
    filter_class = StudentFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_destroy(self, instance):
        instance.status_id = Status.DELETED
        instance.save()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        response = []
        for datum in request.data:
            inst = Student.objects.get(id=datum['id'])
            serializer = self.get_serializer(
                inst, data=datum, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response.append(serializer.data)
        return Response(response)


class StudentGroupViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    # permission_classes = (WorkUnderInstitutionPermission,)
    queryset = StudentGroup.objects.exclude(status=Status.DELETED)
    serializer_class = StudentGroupSerializer
    filter_class = StudentGroupFilter
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

    def perform_destroy(self, instance):
        instance.status_id = Status.DELETED
        instance.save()


class StudentStudentGroupViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = StudentStudentGroupRelation.objects.all()
    serializer_class = StudentStudentGroupSerializer

    # M2M query returns duplicates. Overrode this function
    # from NestedViewSetMixin to implement the .distinct()
    def filter_queryset_by_parents_lookups(self, queryset):
        parents_query_dict = self.get_parents_query_dict()
        if parents_query_dict:
            try:
                return queryset.filter(
                    **parents_query_dict
                ).order_by().distinct('id')
            except ValueError:
                raise Http404
        else:
            return queryset

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.active = 0
#         instance.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)
