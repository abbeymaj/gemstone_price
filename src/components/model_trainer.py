# Importing packages
import sys
import numpy as np
import pandas as pd
from sklearn import set_config
set_config(transform_output='pandas')
from src.exception import CustomException
from src.logger import logging
from src.project_utils import save_object
from src.components.config_entity import ModelTrainerConfig
from src.components.config_entity import DataTransformationConfig
from src.components.config_entity import StoreFeatureConfig
from src.components.config_entity import ModelTrainerConfig
from src.project_utils import find_best_model
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error


# Creating a class to train the model
class ModelTrainer():
    '''
    This class contains methods to train the model and then save the trained model
    in the artifacts folder. 
    '''
    # Creating the constructor of the class
    def __init__(self):
        '''
        This is the constructor of the class. The constructor instantiates the path to 
        the transformed data and the preprocessor object.
        '''
        # Instantiating the path to the preprocessor object
        self.preprocessor_obj_path = DataTransformationConfig()
        # Instantiating the path to the transformed datasets
        self.transformed_dataset_path = StoreFeatureConfig()
        # Instantiating the path to the trained model
        self.trained_model_path = ModelTrainerConfig()
    
    # Creating the feature and target datasets
    def create_feature_target_datasets(self):
        '''
        This method creates the feature and target datasets.
        ============================================================================       
        -------------------
        Returns:
        -------------------
        X_train : pandas dataframe - The training feature set.
        y_train : pandas dataframe - The training target set.
        X_test : pandas dataframe - The test feature set.
        y_test : pandas dataframe - The test target set.
        ============================================================================= 
        '''
        try:
            # Reading the train and test datasets
            train_df = pd.read_parquet(self.transformed_dataset_path.xform_train_path)
            test_df = pd.read_parquet(self.transformed_dataset_path.xform_test_path)
            
            # Splitting the train dataset into a feature and target set
            X_train = train_df.copy().drop(labels=['price'], axis=1)
            y_train = train_df.loc[:, 'price'].copy()
            
            # Splitting the test dataset into a feature and target set
            X_test = test_df.copy().drop(labels=['price'], axis=1)
            y_test = test_df.loc[:, 'price'].copy()
            
            return (
                X_train,
                X_test,
                y_train,
                y_test
            )
        
        except Exception as e:
            raise CustomException(e, sys)
    
    # Creating a function to initiate model training
    def initiate_model_training(self):
        '''
        This method trains the model and then saves the trained model to the artifacts
        folder.
        ===================================================================================
        ------------------------
        Returns:
        ------------------------
        model_path : str - This is the path to the saved model.
        metric : float - This is the metric from the prediction.
        ====================================================================================
        '''
        try:
            # Fetching the train and test sets
            X_train, X_test, y_train, y_test = self.create_feature_target_datasets()
            
            # Instantiating the XGBoost model
            xgb = XGBRegressor(objective='reg:squarederror')
            
            # Defining the parameters for grid search cross validation
            params = {
                'eta': [0.1, 0.01, 0.08, 0.001],
                'max_depth': [4, 6, 8, 10],
                'learning_rate': [0.1, 0.01, 0.001],
                'n_estimators': [100, 200, 500, 800]
            }
            
            # Defining the best model using grid search cross validation
            best_model = find_best_model(
                X_train=X_train,
                y_train=y_train,
                estimator=xgb,
                params=params,
                cv=5
            )
            
            # Saving the best model
            save_object(
                file_path=self.trained_model_path.trained_model_file_path,
                object=best_model
            )
            
            # Predicting using the best model and test set
            y_preds = best_model.predict(X_test)
            
            # Calculate the root mean squared error for the prediction
            metric = np.sqrt(mean_squared_error(y_test, y_preds))
            
            return (
                self.trained_model_path.trained_model_file_path,
                metric
            )
        
        except Exception as e:
            raise CustomException(e, sys)
