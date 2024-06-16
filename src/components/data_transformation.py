# Import packages
import sys
import pandas as pd
from sklearn import set_config
set_config(transform_output='pandas')
from src.utils import create_aspect_features
from src.logger import logging
from src.exception import CustomException 
from src.components.config_entity import DataTransformationConfig
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


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
        self.data_transformation_config = DataTransformationConfig()
    
    # Creating a function to build the preprocessor object
    def create_data_transformation_object(self):
        '''
        This function creates the preprocessor object.
        =============================================================================
        ------------------
        Returns:
        ------------------
        preprocessor : pipeline object - Returns the preprocessor object. 
        =============================================================================
        
        '''
        try:
            logging.info('Beginning the creation of the preprocessor object.')
            
            # Defining the column for the 'carat' feature
            carat = ['carat']
            # Defining the columns for the aspect features (x, y, z)
            aspect = ['x', 'y', 'z']
            # Defining the column for the 'cut' feature
            cut = ['cut']
            # Defining the column for the 'color' feature
            color = ['color']
            # Defining the column for the 'clarity' feature
            clarity = ['clarity']
            
            # Creating the pipeline for the 'Carat' feature
            carat_pipeline = Pipeline(
                steps=[
                    ('carat_std_sclr', StandardScaler())
                ]
            )
            
            # Creating the pipeline for the aspect (x, y, z) features
            aspect_pipeline = Pipeline(
                steps=[
                    ('aspect_ft', FunctionTransformer(create_aspect_features)),
                    ('aspect_simple_imp', SimpleImputer(strategy='median')),
                    ('aspect_std_sclr', StandardScaler())
                ]
            )
            
            # Creating the pipeline for the 'cut' feature
            cut_pipeline = Pipeline(
                steps=[
                    ('cut_oe', OrdinalEncoder(
                        categories=[['Fair', 'Good', 'Ideal', 'Very Good', 'Premium']]
                    ))
                ]
            )
            
            # Creating the pipeline for the 'color' feature
            color_pipeline = Pipeline(
                steps=[
                    ('color_oe', OrdinalEncoder(
                        categories=[['J', 'I', 'H', 'G', 'F', 'E', 'D']]
                    ))
                ]
            )
            
            # Creating the pipeline for the 'clarity' feature
            clarity_pipeline = Pipeline(
                steps=[
                    ('clarity_oe', OrdinalEncoder(
                        categories=[['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']]
                    ))
                ]
            )
            
            # Combining all pipelines into a single preprocessor object
            preprocessor = ColumnTransformer(
                [
                    ('carat', carat_pipeline, carat),
                    ('aspect', aspect_pipeline, aspect),
                    ('cut', cut_pipeline, cut),
                    ('color', color_pipeline, color),
                    ('clarity', clarity_pipeline, clarity)
                ]
            )
            
            logging.info('Preprocessing object creation completed.')
            
            return preprocessor
        
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
        
