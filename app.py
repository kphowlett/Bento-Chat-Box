import pyscript
import utils

# Downloading the local csv file - can be updated for a pull from AWS S3 or other data service using boto3
df = utils.upload_df('upload_file4.csv')

# Displaying the Dataframe
pyscript.display(df.style.hide(axis='index'), )

# Displaying metrics of the data
pyscript.display("Download Size of Preview: " + utils.get_download_attrs(df))
pyscript.display('Number of Cases: ' + str(df.shape[0]))