# Importing packages
import sys
from src.project_utils import load_object
from src.logger import logging
from src.exception import CustomException
from src.components.config_entity import DataTransformationConfig
from src.components.config_entity import ModelTrainerConfig

# Creating the prediction pipeline class
class PredictPipeline():
    '''
    This class will make predictions using the trained model. When the user enters data on
    the site, the data is first transformed using the preprocessor object and then the 
    trained model is used to make predictions.
    '''
    # Creating the constructor for the class
    def __init__(self):
        '''
        The constructor instantiates the preprocessor object and the trained model
        config classes.
        '''
        # Instantiating the preprocessing object class
        self.preprocessor_obj = DataTransformationConfig()
        # Instantiating the trained model class
        self.trained_model = ModelTrainerConfig()
    
    # Creating the method to make predictions
    def predict(self, features):
        '''
        This method makes predictions using the feature inputs from the web page and 
        the trained model. This method also transforms the input data using the 
        preprocessor object before making the predictions.
        ============================================================================================
        -------------------
        Parameters:
        -------------------
        features : This is the feature data input received from the web page.
        
        -------------------
        Returns:
        -------------------
        preds : This is the prediction based on the input features.
        =============================================================================================
        '''
        try:
            # Loading the preprocessing object and trained model
            preprocessor = load_object(file_path=self.preprocessor_obj.preprocessor_obj_path)
            model = load_object(file_path=self.trained_model.trained_model_file_path)
            
            # Transforming the features using the preprocessing object
            xform_data = preprocessor.transform(features)
            
            # Making predictions using the transformed data
            preds = model.predict(xform_data)
            
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)
            