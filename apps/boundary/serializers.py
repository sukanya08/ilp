from rest_framework import serializers

from common.serializers import ILPSerializer
from boundary.models import (Boundary, ElectionBoundary,
                             BoundaryHierarchy,
                             BoundaryType, BoundaryAggregation
                             )
from rest_framework_gis.serializers import (GeoFeatureModelSerializer,                                                     GeometrySerializerMethodField)


class BoundarySerializer(ILPSerializer):

    class Meta:
        model = Boundary
        fields = (
            'id', 'name', 'parent', 'dise_slug', 'boundary_type', 'type',
            'status',
        )


class BoundaryWithParentSerializer(ILPSerializer):
    parent_boundary = BoundarySerializer(source='parent')

    class Meta:
        model = Boundary
        fields = (
            'id', 'name', 'dise_slug', 'type', 'boundary_type',
            'parent_boundary'
        )


class BoundaryHierarchySerializer(ILPSerializer):
    class Meta:
        model = BoundaryHierarchy()
        fields = (
            'admin0_name', 'admin0_id', 'admin1_name', 'admin1_id',
            'admin2_name', 'admin2_id', 'admin3_name', 'admin3_id'
        )

class ElectionBoundarySerializer(ILPSerializer):
    name = serializers.CharField(source='const_ward_name')

    class Meta:
        model = ElectionBoundary
        fields = ('id', 'name',  'const_ward_type', 'dise_slug', 'elec_comm_code', 'current_elected_rep', 'current_elected_party', 'state', 'parent')


class BoundaryTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoundaryType
        fields = ('char_id', 'name')


class BoundaryAggregationSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoundaryAggregation
        fields = (
            'bid', 'name', 'academic_year',
            'gender', 'mt', 'religion', 'category',
            'num'
        )
