import pyscript
import utils

# df = pd.read_csv('./upload_file4.csv', index_col=False)

df = utils.upload_df('upload_file4.csv')

# df = df.rename(columns={
#     "demographic_data_id": "id",
#     "age_at_index": "age",
# }).drop(columns = ["type", "study_subject.study_subject_id"]).reset_index(drop=True)

# df = utils.filter_df(df, 'race', "White")

pyscript.display(df.style.hide(axis='index'), )


pyscript.display("download size of preview: " + utils.get_download_attrs(df))