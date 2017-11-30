from .survey import Survey, Question, Source, SurveyTag
from .answers import RespondentType
from users.models import User
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


class SurveySummaryAgg(models.Model):
    """Survey Summary Data"""
    survey_id = models.ForeignKey('Survey', db_column="survey_id")
    survey_tag = models.ForeignKey('SurveyTag', db_column="survey_tag")
    institution_type = models.ForeignKey('common.InstitutionType', db_column="institution_type")
    year_month = models.CharField(max_length=10, db_column="year_month")
    num_schools = models.IntegerField(db_column="num_schools")
    num_assessments = models.IntegerField(db_column="num_assessments")
    num_children = models.IntegerField(db_column="num_children")

    class Meta:
        managed = False
        db_table = 'mvw_survey_summary_agg'


class SurveyDetailsAgg(models.Model):
    """Survey Details Agg"""
    survey_id = models.ForeignKey('Survey', db_column="survey_id")
    survey_tag = models.ForeignKey('SurveyTag', db_column="survey_tag")
    source = models.ForeignKey('Source', db_column="source")
    institution_type = models.ForeignKey('common.InstitutionType', db_column="institution_type")
    year_month = models.CharField(max_length=10, db_column="year_month")
    num_schools = models.IntegerField(db_column="num_schools")
    num_assessments = models.IntegerField(db_column="num_assessments")
    num_children = models.IntegerField(db_column="num_children")
    num_users = models.IntegerField(db_column="num_users")
    num_verified_assessment = models.IntegerField(db_column="num_verified_assessments")
    last_assessment = models.DateField(db_column="last_asessment")

    class Meta:
        managed = False
        db_table = 'mvw_survey_details_agg'


class SurveyInstitutionAgg(models.Model):
    """Survey Institution Agg"""
    survey_id = models.ForeignKey('Survey', db_column="survey_id")
    survey_tag = models.ForeignKey('SurveyTag', db_column="survey_tag")
    institution_id = models.ForeignKey('schools.Institution', db_column="institution_id")
    source = models.ForeignKey('Source', db_column="source")
    year_month = models.CharField(max_length=10, db_column="year_month")
    num_assessments = models.IntegerField(db_column="num_assessments")
    num_children = models.IntegerField(db_column="num_children")
    num_users = models.IntegerField(db_column="num_users")
    num_verified_assessment = models.IntegerField(db_column="num_verified_assessments")
    last_assessment = models.DateField(db_column="last_asessment")

    class Meta:
        managed = False
        db_table = 'mvw_survey_institution_agg'


class SurveyBoundaryAgg(models.Model):
    """Survey Boundary Agg"""
    survey_id = models.ForeignKey('Survey', db_column="survey_id")
    survey_tag = models.ForeignKey('SurveyTag', db_column="survey_tag")
    boundary_id = models.ForeignKey('boundary.Boundary', db_column="boundary_id")
    source = models.ForeignKey('Source', db_column="source")
    year_month = models.CharField(max_length=10, db_column="year_month")
    num_schools = models.IntegerField(db_column="num_schools")
    num_assessments = models.IntegerField(db_column="num_assessments")
    num_children = models.IntegerField(db_column="num_children")
    num_users = models.IntegerField(db_column="num_users")
    num_verified_assessment = models.IntegerField(db_column="num_verified_assessments")
    last_assessment = models.DateField(db_column="last_asessment")

    class Meta:
        managed = False
        db_table = 'mvw_survey_boundary_agg'


class SurveyElectionBoundaryAgg(models.Model):
    """Survey Election Boundary Agg"""
    survey_id = models.ForeignKey('Survey', db_column="survey_id")
    survey_tag = models.ForeignKey('SurveyTag', db_column="survey_tag")
    boundary_id = models.ForeignKey('boundary.ElectionBoundary', db_column="electionboundary_id")
    source = models.ForeignKey('Source', db_column="source")
    year_month = models.CharField(max_length=10, db_column="year_month")
    num_schools = models.IntegerField(db_column="num_schools")
    num_assessments = models.IntegerField(db_column="num_assessments")
    num_children = models.IntegerField(db_column="num_children")
    num_users = models.IntegerField(db_column="num_users")
    num_verified_assessment = models.IntegerField(db_column="num_verified_assessments")
    last_assessment = models.DateField(db_column="last_asessment")

    class Meta:
        managed = False
        db_table = 'mvw_survey_election_boundary_agg'


class SurveyRespondentTypeAgg(models.Model):
    """Survey RespondentType Agg"""
    survey_id = models.ForeignKey('Survey', db_column="survey_id")
    survey_tag = models.ForeignKey('SurveyTag', db_column="survey_tag")
    respondent_type = models.ForeignKey('RespondentType', db_column="respondent_type")
    source = models.ForeignKey('Source', db_column="source")
    year_month = models.CharField(max_length=10, db_column="year_month")
    num_schools = models.IntegerField(db_column="num_schools")
    num_assessments = models.IntegerField(db_column="num_assessments")
    num_children = models.IntegerField(db_column="num_children")
    num_verified_assessment = models.IntegerField(db_column="num_verified_assessments")
    last_assessment = models.DateField(db_column="last_asessment")

    class Meta:
        managed = False
        db_table = 'mvw_survey_respondenttype_agg'


class SurveyUserTypeAgg(models.Model):
    """Survey UserType Agg"""
    survey_id = models.ForeignKey('Survey', db_column="survey_id")
    survey_tag = models.ForeignKey('SurveyTag', db_column="survey_tag")
    user_type = models.ForeignKey(User, db_column="user_type")
    source = models.ForeignKey('Source', db_column="source")
    year_month = models.CharField(max_length=10, db_column="year_month")
    num_schools = models.IntegerField(db_column="num_schools")
    num_assessments = models.IntegerField(db_column="num_assessments")
    num_children = models.IntegerField(db_column="num_children")
    num_verified_assessment = models.IntegerField(db_column="num_verified_assessments")
    last_assessment = models.DateField(db_column="last_asessment")

    class Meta:
        managed = False
        db_table = 'mvw_survey_usertype_agg'


class SurveyAnsAgg(models.Model):
    """Survey Answer Agg"""
    survey_id = models.ForeignKey('Survey', db_column="survey_id")
    survey_tag = models.ForeignKey('SurveyTag', db_column="survey_tag")
    source = models.ForeignKey('Source', db_column="source")
    year_month = models.CharField(max_length=10, db_column="year_month")
    question_id = models.ForeignKey('Question', db_column="question_id")
    answer_option = models.CharField(max_length=100, db_column="answer_option")
    num_answers = models.IntegerField(db_column="num_answers")

    class Meta:
        managed = False
        db_table = 'mvw_survey_ans_agg'


class SurveyQuestionKeyAgg(models.Model):
    """Survey QuestionKey Agg"""
    survey_id = models.ForeignKey('Survey', db_column="survey_id")
    survey_tag = models.ForeignKey('SurveyTag', db_column="survey_tag")
    source = models.ForeignKey('Source', db_column="source")
    year_month = models.CharField(max_length=10, db_column="year_month")
    question_key = models.CharField(max_length=100, db_column="question_key")
    num_assessments = models.IntegerField(db_column="num_assessments")
    num_correct_assessments = models.IntegerField(db_column="num_correct_assessments")

    class Meta:
        managed = False
        db_table = 'mvw_survey_questionkey_agg'


class SurveyClassGenderAgg(models.Model):
    """Survey Class Gender Agg"""
    survey_id = models.ForeignKey('Survey', db_column="survey_id")
    survey_tag = models.ForeignKey('SurveyTag', db_column="survey_tag")
    source = models.ForeignKey('Source', db_column="source")
    year_month = models.CharField(max_length=10, db_column="year_month")
    sg_name = models.CharField(max_length=100, db_column="sg_name")
    gender = models.ForeignKey("common.Gender", db_column="gender")
    num_assessments = models.IntegerField(db_column="num_assessments")
    num_perfectscore_assessments = models.IntegerField(db_column="num_perfectscore_assessments")

    class Meta:
        managed = False
        db_table = 'mvw_survey_classs_gender_agg'


class SurveyClassAnsAgg(models.Model):
    """Survey Class Answer Agg"""
    survey_id = models.ForeignKey('Survey', db_column="survey_id")
    survey_tag = models.ForeignKey('SurveyTag', db_column="survey_tag")
    source = models.ForeignKey('Source', db_column="source")
    year_month = models.CharField(max_length=10, db_column="year_month")
    sg_name = models.CharField(max_length=100, db_column="sg_name")
    question_id = models.ForeignKey("Question", db_column="question_id")
    answer_option = models.CharField(max_length=100, db_column="answer_option")
    num_answers = models.IntegerField(db_column="num_answers")

    class Meta:
        managed = False
        db_table = 'mvw_survey_classs_ans_agg'