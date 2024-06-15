# Importing packages
import os
from dataclasses import dataclass


# Creating the config for data ingestion 
@dataclass
class DataIngestionConfig():
    '''
    This class defines the path for the train and validation datasets.
    '''
    train_data_path:str = os.path.join('artifacts', 'train_data.parquet')
    test_data_path:str = os.path.join('artifacts', 'test_data.parquet')


# Creating the config for data transformation
@dataclass
class DataTransformationConfig():
    '''
    This class defines the path for the preprocessor object. 
    '''
    preprocessor_obj_path:str = os.path.join('artifacts', 'preprocessor.pkl')
    