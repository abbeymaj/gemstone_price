# Import packages
import sys
import pandas as pd
from sklearn import set_config
set_config(transform_output='pandas')
from src.logger import logging
from src.exception import CustomException 
from src.components.config_entity import DataTransformationConfig


# Creating a class to create the preprocessing object and transform the data
class DataTransformation():
    '''
    This class contains methods to preprocess the train an test datasets and
    save the preprocessing object. 
    '''
    # Creating the constructor
    def __init__(self):
        '''
        The constructor instantiates the Data Transformation Config path.
        '''
        pass
    
    # Creating a function to build the preprocessor object
    def create_data_transformation_object(self):
        '''
        This function creates the preprocessor object.
        '''
        try:
            pass
        
        except Exception as e:
            raise CustomException(e, sys)
    
    
    # Creating a function to initiate the data transformation
    def initiate_data_transformation(self, train_path:str, test_path:str):
        '''
        This function performs the data transformation on the feature set.
        ===============================================================================
        ----------------
        Parameters:
        ----------------
        train_path : str - The path in which the training data is stored.
        test_path : str - The path in which the test data is stored.
        
        ----------------
        Returns:
        ----------------
        train_arr : numpy array - The array used for training the model.
        test_arr : numpy array - The array used for testing the model.
        preprocessor object path : str - The path in which the preprocessor object 
        is stored.
        ================================================================================
        '''
        try:
            pass
        
        except Exception as e:
            raise CustomException(e, sys)
        
