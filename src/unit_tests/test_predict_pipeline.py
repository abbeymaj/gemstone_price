# Importing packages
import os
import pandas as pd
import pytest
from src.pipelines.predict_pipeline import PredictPipeline
from src.components.config_entity import DataIngestionConfig


# Creating a function to return the test data path
@pytest.fixture(scope='function')
def data_path():
    data = DataIngestionConfig()
    return data.test_data_path

# Verifying that the prediction pipeline returns predictions
def test_create_preds(data_path):
    df = pd.read_parquet(data_path)
    df = df.iloc[:, :-1]
    df5 = df.sample(5)
    pred_model = PredictPipeline()
    preds = pred_model.predict(df5)
    assert len(preds) == 5


    

