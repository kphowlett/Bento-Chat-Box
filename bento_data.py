import utils
from pandas import DataFrame

class datahandler:
    def __init__(self, file):
        self.dataframe = utils.upload_df(file)
    
    # Return length of the data to get the number of cases
    def get_shape(self):
        return len(self.dataframe)
    
    def full_size(self, file):
        self.dataframe = utils.upload_df(file)

    def get_download_size(self):
        return utils.get_download_attrs(self.dataframe)
    
    # Special Case check - Filter options yield 0 cases
    def zero_cases(self):
        if len(self.dataframe) <= 0:
            return True
        else:
            return False
        
    def filter_category(self, column, criteria):
        filtered_df = DataFrame(self.dataframe)
        self.dataframe = utils.filter_df(filtered_df, column, criteria)

    def filter_greater_than(self, column, criteria):
        self.dataframe = self.dataframe.loc[self.dataframe[str(column)] > criteria]

    def display(self):
        utils.display_data(self.dataframe)