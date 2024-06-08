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