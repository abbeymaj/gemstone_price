# Importing packages
import os
import pytest
import pandas as pd
from src.components.config_entity import DataIngestionConfig

# Defining a function to return the train data path
@pytest.fixture(scope='function')
def train_data_path():
    data_ingestion_config = DataIngestionConfig()
    return data_ingestion_config.train_data_path

# Defining a function to return the test data path
@pytest.fixture(scope='function')
def test_data_path():
    data_ingestion_config = DataIngestionConfig()
    return data_ingestion_config.test_data_path

# Verifying that the artifacts folder exists
def test_check_artifacts_folder(path='artifacts'):
    assert os.path.exists('artifacts') is True

# Verifying that the train set has 11 columns
def test_count_trainset_columns(train_data_path):
    df_train = pd.read_parquet(train_data_path)
    assert len(list(df_train.columns)) == 11

# Verifying that the test set has 11 columns
def test_count_testset_columns(test_data_path):
    df_test = pd.read_parquet(test_data_path)
    assert len(list(df_test.columns)) == 11