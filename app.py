import pyscript
from utils import upload_df
import bento_data

# Downloading the local csv file - can be updated for a pull from AWS S3 or other data service using boto3
df = upload_df('upload_file4.csv')
new_df = bento_data.datahandler(df, df.shape)

# Displaying metrics of the data
# pyscript.display("Download Size of Preview: " + utils.get_download_attrs(df))
# pyscript.display('Number of Cases: ' + str(utils.get_shape(df)))

pyscript.display("download size of bentohandler preview: " + new_df.get_download_size())
pyscript.display("Number of cases for bentohandler: " + str(new_df.get_shape()))

# Displaying the Dataframe
pyscript.display(df.style.hide(axis='index'))