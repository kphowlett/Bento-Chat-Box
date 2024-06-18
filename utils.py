import pandas as pd
import sys
import pyscript

# Gets shape of a dataframe
def get_cases(df):
    return df.shape[0]

    # Finds all unique values of a dataframe column
def get_unique_values(df, column):
    print(df[str(column)].unique())

    # Filters a dataframe for a specific value of a specific column
def filter_df(df, column, criteria):
    return df.loc[df[str(column)] == str(criteria)]

    # Returns the size in MB of the current dataframe on the page
def get_download_attrs(df):
    # import sys
    return str('{:9.4f}MB').format(sys.getsizeof(df) / 1000000)

def upload_df(file):
    df = pd.read_csv(file, encoding="UTF-8", index_col=False)
    df = df.rename(columns={
    "demographic_data_id": "id",
    "age_at_index": "age",
    }).drop(columns = ["type", "study_subject.study_subject_id"]).reset_index(drop=True)
    return df
    
def display_data(df):
    pyscript.display(df.style.hide(axis='index'))