import pandas as pd
import utils

class datahandler:
    def __init__(self, data, shape):
        self.data = utils.upload_df("upload_file4.csv")
        self.shape = utils.get_shape(self.data)
    
    def get_shape(self):
        return self.shape
    
    def get_download_size(self):
        return utils.get_download_attrs(self.data)
    
    