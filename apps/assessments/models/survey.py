from django.db import models
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType


class SurveyType(models.Model):
    """Type of Survey"""
    char_id = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=50)


class SurveyOnType(models.Model):
    """Type of entity survey is conducted on"""
    char_id = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=50)


class ResponseType(models.Model):
    """Type of input expected"""
    char_id = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=50)


class DisplayType(models.Model):
    """Display type to be used"""
    char_id = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=50)


class Survey(models.Model):
    """Survey/Programme"""
    name = models.CharField(max_length=100)
    created_at = models.DateField(max_length=20)
    updated_at = models.DateField(max_length=20, null=True)
    partner = models.ForeignKey('Partner', null=True)
    description = models.CharField(max_length=200, null=True)
    status = models.ForeignKey('common.Status')

    class Meta:
        ordering = ['name', ]


class QuestionGroup(models.Model):
    """Group of questions for a Survey"""
    name = models.CharField(max_length=100)
    survey = models.ForeignKey('Survey')
    type = models.ForeignKey('SurveyType')
    inst_type = models.ForeignKey('common.InstitutionType')
    survey_on = models.ForeignKey('SurveyOnType')
    group_text = models.CharField(max_length=100, null=True)
    start_date = models.DateField(max_length=20)
    end_date = models.DateField(max_length=20, null=True)
    academic_year = models.ForeignKey('common.AcademicYear', null=True)
    version = models.IntegerField(blank=True, null=True)
    source = models.ForeignKey("Source", null=True)
    double_entry = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, null=True)
    created_at = models.DateField(max_length=20)
    updated_at = models.DateField(max_length=20, null=True)
    status = models.ForeignKey('common.Status')


class Question(models.Model):
    """pool of questions"""
    question_text = models.CharField(max_length=300)
    display_text = models.CharField(max_length=300)
    key = models.CharField(max_length=50, null=True)
    question_type = models.ForeignKey('QuestionType', null=True)
    options = models.CharField(max_length=300, null=True)
    is_featured = models.BooleanField()
    status = models.ForeignKey('common.Status')


class Partner(models.Model):
    """Boundary that partner is associated with"""
    char_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    admin0 = models.ForeignKey('boundary.Boundary')


class Source(models.Model):
    """Different sources of information"""
    name = models.CharField(max_length=100)


class QuestionType(models.Model):
    """Different response and display choices for questions"""
    type = models.ForeignKey('ResponseType')
    display = models.ForeignKey('DisplayType')


class QuestionGroup_Questions(models.Model):
    """Mapping of questions to a question group"""
    questiongroup = models.ForeignKey('QuestionGroup')
    question = models.ForeignKey('Question')
    sequence = models.IntegerField()

    class Meta:
        unique_together = (('question', 'questiongroup'), )


class QuestionGroup_Institution_Association(models.Model):
    """Mapping of question group to different institutions
        for institution assessments"""
    institution = models.ForeignKey('schools.Institution')
    questiongroup = models.ForeignKey('QuestionGroup')
    status = models.ForeignKey('common.Status')

    class Meta:
        unique_together = (('institution', 'questiongroup'), )


class QuestionGroup_StudentGroup_Association(models.Model):
    """Mapping of student groups to question groups for student
        and studentgroup assessments"""
    studentgroup = models.ForeignKey('schools.StudentGroup')
    questiongroup = models.ForeignKey('QuestionGroup')
    status = models.ForeignKey('common.Status')

    class Meta:
        unique_together = (('studentgroup', 'questiongroup'), )


class GuardianUserObjectPermission(models.Model):
    object_pk = models.CharField(max_length=100)
    content_type_id = models.ForeignKey(ContentType)
    user_id = models.ForeignKey(User)
    permission_id = models.ForeignKey(Permission)
