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

# Verify that the train data file exists
def test_check_train_data_path(train_data_path):
    assert os.path.exists(train_data_path) is True

# Verify that the test data file exists
def test_check_test_data_path(test_data_path):
    assert os.path.exists(test_data_path) is True

# Verifying that the train set has 8 columns
def test_count_trainset_columns(train_data_path):
    df_train = pd.read_parquet(train_data_path)
    assert len(list(df_train.columns)) == 8

# Verifying that the dropped columns (id, depth, table)
# are not present in the train set.
def test_no_dropped_cols_trainset(train_data_path):
    df_train = pd.read_parquet(train_data_path)
    train_cols = list(df_train.columns)
    dropped_cols = ['id', 'depth', 'table']
    assert all(e in train_cols for e in dropped_cols) is False

# Verifying that the test set has 8 columns
def test_count_testset_columns(test_data_path):
    df_test = pd.read_parquet(test_data_path)
    assert len(list(df_test.columns)) == 8

# Verifying that the dropped columns (id, depth, table)
# are not present in the test set.
def test_no_dropped_cols_testset(test_data_path):
    df_test = pd.read_parquet(test_data_path)
    test_cols = list(df_test.columns)
    dropped_cols = ['id', 'depth', 'table']
    assert all(e in test_cols for e in dropped_cols) is False