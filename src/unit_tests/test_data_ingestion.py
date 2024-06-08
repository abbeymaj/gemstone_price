# Importing packages
import pytest
import pandas as pd
from src.components.config_entity import DataIngestionConfig

@pytest.fixture(scope='function')
def train_data_path():
    data_ingestion_config = DataIngestionConfig()
    return data_ingestion_config.train_data_path

@pytest.fixture(scope='function')
def test_data_path():
    data_ingestion_config = DataIngestionConfig()
    return data_ingestion_config.test_data_path


def test_count_trainset_columns(train_data_path):
    df_train = pd.read_parquet(train_data_path)
    assert len(list(df_train.columns)) == 11


def test_count_testset_columns(test_data_path):
    df_test = pd.read_parquet(test_data_path)
    assert len(list(df_test.columns)) == 11