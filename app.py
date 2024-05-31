import pandas as pd
from tabulate import tabulate
import pyscript

df = pd.read_csv('./upload_file4.csv', index_col=False)

# THIS IS FOR UPLOAD_FILE1.CSV
# df = df.rename(columns={
#     "diagnosis.diagnosis_id": "diagnosis_id",
#     "therapeutic_procedure_id": "procedure_id",
#     "primary_surgical_procedure": "procedure",
#     "days_to_treatment_start": "treatment start (days)",
#     "days_to_treatment_end": "treatment end (days)"
# }).drop(columns=["endocrine_therapy_type", "all_endocrine_therapy_stopped", "chemotherapy_regimen"])

df = df.rename(columns={
    "demographic_data_id": "id",
    "age_at_index": "age",
}).drop(columns = ["type", "study_subject.study_subject_id"]).reset_index(drop=True)

pyscript.display('dataframe', df.style.hide(axis='index'))