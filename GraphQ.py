import requests # type: ignore

# GraphQL endpoint URL
url = 'https://bento-tools.org/v1/graphql/'

# Queries and variables
queries = {
    "search_subjects_without_filters": {
        "query": """
        query searchSubjects(
          $subject_ids: [String], 
          $programs: [String], 
          $studies: [String], 
          $diagnoses: [String], 
          $rc_scores: [String], 
          $tumor_sizes: [String], 
          $chemo_regimen: [String], 
          $tumor_grades: [String], 
          $er_status: [String], 
          $pr_status: [String], 
          $endo_therapies: [String], 
          $meno_status: [String], 
          $tissue_type: [String], 
          $composition: [String], 
          $association: [String], 
          $file_type: [String], 
          $age_at_index: [Float]
        ) {
        searchSubjects(
          subject_ids: $subject_ids
          programs: $programs
          studies: $studies
          diagnoses: $diagnoses
          rc_scores: $rc_scores
          tumor_sizes: $tumor_sizes
          chemo_regimen: $chemo_regimen
          tumor_grades: $tumor_grades
          er_status: $er_status
          pr_status: $pr_status
          endo_therapies: $endo_therapies
          meno_status: $meno_status
          tissue_type: $tissue_type
          composition: $composition
          association: $association
          file_type: $file_type
          age_at_index: $age_at_index
        ) {
          numberOfPrograms
          numberOfStudies
          numberOfSubjects
          numberOfSamples
          numberOfLabProcedures
          numberOfFiles
          subjectCountByProgram {
            group
            subjects
          }
          subjectCountByStudy {
            group
            subjects
          }
          subjectCountByDiagnoses {
            group
            subjects
          }
          subjectCountByRecurrenceScore {
            group
            subjects
          }
          subjectCountByTumorSize {
            group
            subjects
          }
          subjectCountByChemotherapyRegimen {
            group
            subjects
          }
          subjectCountByEndocrineTherapy {
            group
            subjects
          }
          subjectCountByTumorGrade {
            group
            subjects
          }
          subjectCountByErStatus {
            group
            subjects
          }
          subjectCountByPrStatus {
            group
            subjects
                }
          subjectCountByMenopauseStatus {
            group
            subjects
          }
          subjectCountByFileType {
            group
            subjects
          }
          subjectCountByFileAssociation {
            group
            subjects
          }
          subjectCountByTissueComposition {
            group
            subjects
          }
          subjectCountByTissueType {
            group
            subjects
          }
        }
        }
        """,
        "variables": {}
    },
    "search_subjects_with_filters": {
        "query": """
        query searchSubjects(
          $subject_ids: [String], 
          $programs: [String], 
          $studies: [String], 
          $diagnoses: [String], 
          $rc_scores: [String], 
          $tumor_sizes: [String], 
          $chemo_regimen: [String], 
          $tumor_grades: [String], 
          $er_status: [String], 
          $pr_status: [String], 
          $endo_therapies: [String], 
          $meno_status: [String], 
          $tissue_type: [String], 
          $composition: [String], 
          $association: [String], 
          $file_type: [String], 
          $age_at_index: [Float]
        ) {
          searchSubjects(
            subject_ids: $subject_ids
            programs: $programs
            studies: $studies
            diagnoses: $diagnoses
            rc_scores: $rc_scores
            tumor_sizes: $tumor_sizes
            chemo_regimen: $chemo_regimen
            tumor_grades: $tumor_grades
            er_status: $er_status
            pr_status: $pr_status
            endo_therapies: $endo_therapies
            meno_status: $meno_status
            tissue_type: $tissue_type
            composition: $composition
            association: $association
            file_type: $file_type
            age_at_index: $age_at_index
          ) {
            numberOfPrograms
            numberOfStudies
            numberOfSubjects
            numberOfSamples
            numberOfLabProcedures
            numberOfFiles
            subjectCountByProgram {
              group
              subjects
            }
            subjectCountByStudy {
              group
              subjects
            }
            subjectCountByDiagnoses {
              group
              subjects
            }
            subjectCountByRecurrenceScore {
              group
              subjects
            }
            subjectCountByTumorSize {
              group
              subjects
            }
            subjectCountByChemotherapyRegimen {
              group
              subjects
            }
            subjectCountByEndocrineTherapy {
              group
              subjects
            }
            subjectCountByTumorGrade {
              group
              subjects
            }
            subjectCountByErStatus {
              group
              subjects
            }
            subjectCountByPrStatus {
              group
              subjects
                  }
            subjectCountByMenopauseStatus {
              group
              subjects
            }
            subjectCountByFileType {
              group
              subjects
            }
            subjectCountByFileAssociation {
              group
              subjects
            }
            subjectCountByTissueComposition {
              group
              subjects
            }
            subjectCountByTissueType {
              group
              subjects
            }
          }
        }
        """,
        "variables": {
            "diagnoses": ["Adenocarcinoma", "Carcinoma, NOS"],
            "studies": ["C: RS 11-25, randomized to chemo + endocrine therapy"]
        }
    },
    "participants_table_with_filters": {
        "query": """
        query subjectOverview(
          $subject_ids: [String], 
          $programs: [String], 
          $studies: [String], 
          $diagnoses: [String], 
          $rc_scores: [String], 
          $tumor_sizes: [String], 
          $chemo_regimen: [String], 
          $tumor_grades: [String], 
          $er_status: [String], 
          $pr_status: [String], 
          $endo_therapies: [String], 
          $meno_status: [String], 
          $tissue_type: [String], 
          $composition: [String], 
          $association: [String], 
          $file_type: [String], 
          $age_at_index: [Float], 
          $first: Int, 
          $offset: Int, 
          $order_by: String, 
          $sort_direction: String
        ){
          subjectOverview(
            subject_ids: $subject_ids
            programs: $programs
            studies: $studies
            diagnoses: $diagnoses
            rc_scores: $rc_scores
            tumor_sizes: $tumor_sizes
            chemo_regimen: $chemo_regimen
            tumor_grades: $tumor_grades
            er_status: $er_status
            pr_status: $pr_status
            endo_therapies: $endo_therapies
            meno_status: $meno_status
            tissue_type: $tissue_type
            composition: $composition
            association: $association
            file_type: $file_type
            age_at_index: $age_at_index
            first: $first
            offset: $offset
            order_by: $order_by
            sort_direction: $sort_direction
          ) {
            subject_id
            program
            program_id
            study_acronym
            study_short_description
            study_info
            diagnosis
            recurrence_score
            tumor_size
            tumor_grade
            er_status
            pr_status
            chemotherapy
            endocrine_therapy
            menopause_status
            age_at_index
            survival_time
            survival_time_unit
            files
            lab_procedures
            samples
          }
        }
        """,
        "variables": {
            "diagnoses": ["Adenocarcinoma", "Carcinoma, NOS"],
            "studies": ["C: RS 11-25, randomized to chemo + endocrine therapy"],
            "offset": 0,
            "order_by": "subject_id",
            "first": 10,
            "sort_direction": "asc"
        }
    }
}

# Function to make a request
def make_request(query_name):
    query_info = queries[query_name]
    payload = {
        "query": query_info["query"],
        "variables": query_info["variables"]
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Will raise an error for bad status
        result = response.json()
        print(result)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
make_request("search_subjects_without_filters")
make_request("search_subjects_with_filters")
make_request("participants_table_with_filters")
