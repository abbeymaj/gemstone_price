# Importing packages
import os
import pytest
from src.components.config_entity import StoreFeatureConfig
from src.components.config_entity import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

# Creating a function to return the transformed train data path
@pytest.fixture(scope='function')
def xform_train_data_path():
    feature_store = StoreFeatureConfig()
    return feature_store.xform_train_path

# Creating a function to return the transformed test data path
@pytest.fixture(scope='function')
def xform_test_data_path():
    feature_store = StoreFeatureConfig()
    return feature_store.xform_test_path

# Creating a function to return the trained model path
@pytest.fixture(scope='function')
def trained_model_path():
    model_path = ModelTrainerConfig()
    return model_path.trained_model_file_path

# Creating a function to verify that the X_train column count is correct
def test_verify_X_train_col_count():
    trainer = ModelTrainer()
    X_train, _, _, _ = trainer.create_feature_target_datasets()
    assert len(list(X_train.columns)) == 17

# Creating a function to verify that the y_train column contains the 'price' column
def test_verify_y_train_col_name():
    trainer = ModelTrainer()
    _, _, y_train, _ = trainer.create_feature_target_datasets()
    assert y_train.name == 'price'
    
# Creating a function to verify that the X_test column count is correct
def test_verify_X_test_col_count():
    trainer = ModelTrainer()
    _, X_test, _, _ = trainer.create_feature_target_datasets()
    assert len(list(X_test.columns)) == 17

# Creating a function to verify that the y_test column contains the 'price' column
def test_verify_y_test_col_name():
    trainer = ModelTrainer()
    _, _, _, y_test = trainer.create_feature_target_datasets()
    assert y_test.name == 'price'

# Creating a function to verify that the X_train and y_train record counts
# are the same.
def test_train_set_record_count():
    trainer = ModelTrainer()
    X_train, _, y_train, _ = trainer.create_feature_target_datasets()
    assert X_train.shape[0] == y_train.shape[0]

# Creating a function to verify that the X_test and y_test record counts
# are the same.
def test_test_set_record_count():
    trainer = ModelTrainer()
    _, X_test, _, y_test = trainer.create_feature_target_datasets()
    assert X_test.shape[0] == y_test.shape[0]

# Creating a function to verify that the new model path exists in the artifacts folder
def test_verify_trained_model_path(trained_model_path):
    assert os.path.exists(trained_model_path) is True
