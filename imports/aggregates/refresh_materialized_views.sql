CREATE UNIQUE INDEX ON mvw_institution_aggregations (id,gender,mt,religion,category);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_institution_aggregations;

CREATE UNIQUE INDEX ON mvw_institution_stu_gender_count(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_institution_stu_gender_count;

CREATE UNIQUE INDEX ON mvw_institution_class_year_stucount(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_institution_class_year_stucount;

CREATE UNIQUE INDEX ON mvw_boundary_hierarchy(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_boundary_hierarchy;
    
CREATE UNIQUE INDEX ON mvw_boundary_basic_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_boundary_basic_agg;

CREATE UNIQUE INDEX ON mvw_electionboundary_basic_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_electionboundary_basic_agg;

CREATE UNIQUE INDEX ON mvw_boundary_school_gender_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_boundary_school_gender_agg;

CREATE UNIQUE INDEX ON mvw_boundary_school_category_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_boundary_school_category_agg;

CREATE UNIQUE INDEX ON mvw_electionboundary_school_category_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_electionboundary_school_category_agg;

CREATE UNIQUE INDEX ON mvw_boundary_school_mgmt_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_boundary_school_mgmt_agg;

CREATE UNIQUE INDEX ON mvw_boundary_student_mt_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_boundary_student_mt_agg;

CREATE UNIQUE INDEX ON mvw_electionboundary_student_mt_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_electionboundary_student_mt_agg;

CREATE UNIQUE INDEX ON mvw_boundary_school_moi_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_boundary_school_moi_agg;

CREATE UNIQUE INDEX ON mvw_electionboundary_school_moi_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_electionboundary_school_moi_agg;

CREATE UNIQUE INDEX ON mvw_survey_institution_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_agg;

CREATE UNIQUE INDEX ON mvw_survey_electionboundary_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_electionboundary_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_respondenttype_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_respondenttype_agg;

CREATE UNIQUE INDEX ON mvw_survey_institution_respondenttype_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_respondenttype_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_usertype_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_usertype_agg;

CREATE UNIQUE INDEX ON mvw_survey_institution_usertype_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_usertype_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_questionkey_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_questionkey_agg;

CREATE UNIQUE INDEX ON mvw_survey_institution_questionkey_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_questionkey_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_questiongroup_questionkey_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_questiongroup_questionkey_agg;

CREATE UNIQUE INDEX ON mvw_survey_institution_questiongroup_questionkey_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_questiongroup_questionkey_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_questiongroup_gender_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_questiongroup_gender_agg;
CREATE UNIQUE INDEX ON mvw_survey_institution_questiongroup_gender_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_questiongroup_gender_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_class_questionkey_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_class_questionkey_agg;
CREATE UNIQUE INDEX ON mvw_survey_institution_class_questionkey_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_class_questionkey_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_class_gender_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_class_gender_agg;
CREATE UNIQUE INDEX ON mvw_survey_institution_class_gender_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_class_gender_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_class_ans_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_class_ans_agg;
CREATE UNIQUE INDEX ON mvw_survey_institution_class_ans_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_class_ans_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_questionkey_correctans_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_questionkey_correctans_agg;
CREATE UNIQUE INDEX ON mvw_survey_institution_questionkey_correctans_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_questionkey_correctans_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_questiongroup_questionkey_correctans_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_questiongroup_questionkey_correctans_agg;
CREATE UNIQUE INDEX ON mvw_survey_institution_questiongroup_questionkey_correctans_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_questiongroup_questionkey_correctans_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_questiongroup_gender_correctans_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_questiongroup_gender_correctans_agg;
CREATE UNIQUE INDEX ON mvw_survey_institution_questiongroup_gender_correctans_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_questiongroup_gender_correctans_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_class_questionkey_correctans_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_class_questionkey_correctans_agg;
CREATE UNIQUE INDEX ON mvw_survey_institution_class_questionkey_correctans_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_class_questionkey_correctans_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_class_gender_correctans_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_class_gender_correctans_agg;
CREATE UNIQUE INDEX ON mvw_survey_institution_class_gender_correctans_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_class_gender_correctans_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_questiongroup_ans_agg(id,survey_tag);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_questiongroup_ans_agg;
CREATE UNIQUE INDEX ON mvw_survey_institution_questiongroup_ans_agg(id,survey_tag);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_questiongroup_ans_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_questiongroup_agg(id,survey_tag);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_questiongroup_agg;
CREATE UNIQUE INDEX ON mvw_survey_institution_questiongroup_agg(id,survey_tag);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_institution_questiongroup_agg;

CREATE UNIQUE INDEX ON mvw_survey_tagmapping_agg(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_tagmapping_agg;

CREATE UNIQUE INDEX ON mvw_survey_boundary_electiontype_count(id);
REFRESH MATERIALIZED VIEW CONCURRENTLY mvw_survey_boundary_electiontype_count;
