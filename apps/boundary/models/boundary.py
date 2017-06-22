from common.models.choices import *
from django.contrib.gis.db import models


class BoundaryType(models.Model):
    """ Boundary type """
    char_id = models.CharField(max_length=300, primary_key=True)
    name = models.CharField(max_length=300)


class Boundary(models.Model):
    """ educational boundaries """
    parent = models.ForeignKey('self')
    name = models.CharField(max_length=300)
    boundary_type = models.ForeignKey('BoundaryType')
    institution_type = models.CharField(
        max_length=20, choices=INSTITUTION_TYPE)
    dise_slug = models.CharField(max_length=300)
    geom = models.GeometryField()
    status = models.ForeignKey('common.Status')

    class Meta:
        unique_together = (('name', 'parent'), )

    def __unicode__(self):
        return '%s' % self.name


class ElectionBoundary(models.Model):
    """ Election boundaries """
    state = models.ForeignKey('self')
    dise_slug = models.CharField(max_length=300)
    elec_comm_code = models.IntegerField()
    const_ward_name = models.CharField(max_length=300)
    const_ward_type = models.ForeignKey('BoundaryType')
    current_elected_rep = models.CharField(max_length=300)
    current_elected_party = models.ForeignKey('ElectionParty')
    status = models.ForeignKey('common.Status')

    class Meta:
        unique_together = (('elec_comm_code'), )

    def __unicode__(self):
        return '%s' % self.name


class BoundaryNeighbours(models.Model):
    """Neighbouring boundaries"""
    boundary = models.ForeignKey('Boundary')
    neighbour = models.ForeignKey(
            'Boundary', related_name='boundary_neighbour')

    class Meta:
        unique_together = (('boundary','neighbour'), )


class ElectionNeighbours(models.Model):
    """Neighbouring election boundaries"""
    elect_boundary = models.ForeignKey('ElectionBoundary')
    neighbour = models.ForeignKey(
        'ElectionBoundary', related_name='electionboundary_neighbour')

    class Meta:
        unique_together = (('elect_boundary','neighbour'), )


class ElectionParty(models.Model):
    """Election Party"""
    char_id = models.CharField(max_length=300, primary_key=True)
    elect_boundary = models.ForeignKey('ElectionBoundary')
    neighbour = models.ForeignKey(
        'ElectionBoundary', related_name='electionparty_neighbour')

    class Meta:
        unique_together = (('elect_boundary'), )

