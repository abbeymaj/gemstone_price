# Importing packages
import sys
import os
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from src.components.config_entity import DataIngestionConfig
from sklearn import set_config
set_config(transform_output='pandas')
from sklearn.model_selection import train_test_split



# Creating the class to ingest the dataset
class DataIngestion():
    '''
    This class reads the data from source and splits the data into a train and test set.
    The class has two methods - The constructor and the method to ingest the data.
    '''
    # Creating the constructor
    def __init__(self):
        '''
        This the constructor for the data ingestion class.
        '''
        self.ingestion_config = DataIngestionConfig()
    
    # Creating the data ingestion method
    def initiate_data_ingestion(self):
        '''
        This function will initiate the data ingestion and also create the artifacts folder.
        ====================================================================================
        ---------------
        Returns:
        ---------------
        train file path : str - This is the path to the train dataset.
        test file path : str - This is the path to the test dataset.
        ====================================================================================
        '''
        try:
                      
            # Creating the artifacts directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            # Reading the data from source
            df = pd.read_parquet('https://github.com/abbeymaj80/my-ml-datasets/raw/master/project_datasets/gemstones/train.parquet')
            
            # Splitting the dataset into a train and test set
            train_set, test_set = train_test_split(df, test_size=0.33, random_state=42)
            
            # Saving the train and test dataset as parquet files
            train_set.to_parquet(self.ingestion_config.train_data_path, index=False, compression='gzip')
            test_set.to_parquet(self.ingestion_config.test_data_path, index=False, compression='gzip')
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
        
        except Exception as e:
            raise CustomException(e, sys)