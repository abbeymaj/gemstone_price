# Import packages
import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.components.config_entity import StoreFeatureConfig


# Creating a class to store the transformed datasets
class FeatureStoreCreation():
    '''
    '''
    # Creating the constructor for the class
    def __init__(self):
        '''
        The constructor instantiates the store feature config class.
        '''
        self.feature_store_config = StoreFeatureConfig()
    
    # Creating the function to store the transformed datasets
    def create_feature_store(self, train_set, test_set):
        '''
        This function creates the feature store folder and store the transformed features
        in the folder. 
        ======================================================================================
        -----------------
        Parameters:
        -----------------
        train_set : pandas dataframe - This is the train dataset.
        test_set : pandas dataframe - This is the test dataset.
        
        -----------------
        Returns:
        -----------------
        transformed train data path : str - Returns the path to the transformed train dataset.
        transformed test data path : str - Returns the path to the transformed test dataset.
        =======================================================================================
        '''
        try:
            # Creating the folder to store the transfomed datasets
            dirpath = os.path.dirname(self.feature_store_config.xform_train_path)
            os.makedirs(dirpath, exist_ok=True)
        
            # Saving the train and test set into the feature store
            train_set.to_parquet(self.feature_store_config.xform_train_path, index=False, compression='gzip')
            test_set.to_parquet(self.feature_store_config.xform_test_path, index=False, compression='gzip')
            
            return(
                self.feature_store_config.xform_train_path,
                self.feature_store_config.xform_test_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)
        
        
        
        
