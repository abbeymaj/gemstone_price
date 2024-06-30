# Importing packages
import os
import pytest
import pandas as pd
from src.components.config_entity import DataIngestionConfig
from src.components.config_entity import DataTransformationConfig
from src.components.config_entity import StoreFeatureConfig

# Creating a function to return the non-tranformed train data path
@pytest.fixture(scope='function')
def train_data_path():
    data_ingestion_config = DataIngestionConfig()
    return data_ingestion_config.train_data_path

# Creating a function to return the non-transformed test data path
@pytest.fixture(scope='function')
def test_data_path():
    data_ingestion_config = DataIngestionConfig()
    return data_ingestion_config.test_data_path

# Creating a function to return the transformed train data path
@pytest.fixture(scope='function')
def xform_train_data_path():
    data_transform_config = StoreFeatureConfig()
    return data_transform_config.xform_train_path

# Creating a function to return the transformed test data path
@pytest.fixture(scope='function')
def xform_test_data_path():
    data_transform_config = StoreFeatureConfig()
    return data_transform_config.xform_test_path

# Creating a function to return the preprocessor object path
@pytest.fixture(scope='function')
def preprocessor_obj_path():
    preprocessor_obj = DataTransformationConfig()
    return preprocessor_obj.preprocessor_obj_path

# Creating a function to check if the preprocessor object is present
def test_check_preprocessor_obj_path(preprocessor_obj_path):
    assert os.path.exists(preprocessor_obj_path) is True

# Creating a function to check if the feature_store folder exists
def test_feature_store_folder_path(path='feature_store'):
    assert os.path.exists(path) is True

# Creating a function to check if the transformed train dataset is present
def test_check_xform_train_dataset_path(xform_train_data_path):
    assert os.path.exists(xform_train_data_path) is True

# Creating a function to check if the transformed test dataset is present
def test_check_xform_test_dataset_path(xform_test_data_path):
    assert os.path.exists(xform_test_data_path) is True

# Creating a function to check if the transformed train dataset has the correct 
# number of columns
def test_check_train_dataset_col_length(xform_train_data_path):
    df = pd.read_parquet(xform_train_data_path)
    assert len(list(df.columns)) == 18

# Creating a function to check if the transformed test dataset has the 
# correct number of columns
def test_check_test_dataset_col_length(xform_test_data_path):
    df = pd.read_parquet(xform_test_data_path)
    assert len(list(df.columns)) == 18

# Creating a function to verify that the price column is in the train dataset
def test_verify_price_column_exists(xform_train_data_path):
    df = pd.read_parquet(xform_train_data_path)
    tr_cols = list(df.columns)
    assert 'price' in tr_cols

# Creating a function to verify that the price column is in the test dataset
def test_verify_price_column_exists(xform_test_data_path):
    df = pd.read_parquet(xform_test_data_path)
    tr_cols = list(df.columns)
    assert 'price' in tr_cols

# Creating a function to verify that all expected columns are present in the
# train dataset
def test_verify_cols_in_train_df(xform_train_data_path):
    df = pd.read_parquet(xform_train_data_path)
    train_cols = list(df.columns)
    expected_cols = [
        'carat__carat', 
        'aspect__x', 
        'aspect__y', 
        'aspect__z', 
        'aspect__volume', 
        'aspect__surface_area', 
        'aspect__aspect_ratio_xy',
       'aspect__diagonal_distance', 
       'aspect__relative_height', 
       'aspect__relative_position',
       'aspect__volume_ratio', 
       'aspect__length_ratio', 
       'aspect__width_ratio', 
       'aspect__height_ratio', 
       'cut__cut',
       'color__color', 
       'clarity__clarity', 
       'price']
    assert all(e in train_cols for e in expected_cols) is True

# Creating a function to verify that all expected columns are present in the
# test dataset
def test_verify_cols_in_test_df(xform_test_data_path):
    df = pd.read_parquet(xform_test_data_path)
    train_cols = list(df.columns)
    expected_cols = [
        'carat__carat', 
        'aspect__x', 
        'aspect__y', 
        'aspect__z', 
        'aspect__volume', 
        'aspect__surface_area', 
        'aspect__aspect_ratio_xy',
       'aspect__diagonal_distance', 
       'aspect__relative_height', 
       'aspect__relative_position',
       'aspect__volume_ratio', 
       'aspect__length_ratio', 
       'aspect__width_ratio', 
       'aspect__height_ratio', 
       'cut__cut',
       'color__color', 
       'clarity__clarity', 
       'price']
    assert all(e in train_cols for e in expected_cols) is True

