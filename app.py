import pyscript
# from get_session_input import get_filter_selection
from bento_data import datahandler

# Downloading the local csv file - can be updated for a pull from AWS S3 or other data service using boto3
new_df = datahandler("upload_file4.csv")

# Testing Filtering Cases
# new_df.filter_category(get_filter_selection('User options', 'Filter Cases', 'Age', 'Yes'), 'Black or African American')
new_df.filter_greater_than('age', 100)

# Displaying metrics of the data
pyscript.display("download size of bentohandler preview: " + new_df.get_download_size())
pyscript.display("Number of cases for bentohandler: " + str(new_df.get_shape()))


if(new_df.zero_cases() == True):
    pyscript.display('Your selection returned 0 cases')
else:
    # Displaying the Dataframe
    new_df.display()