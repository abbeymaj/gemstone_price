# Importing packages
import sys
import os
import dill
import numpy as np
from src.exception import CustomException
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor


# Creating a function to save objects as pickle files
def save_object(file_path:str, object):
    '''
    This function saves as object to the given file path.
    ================================================================================
    --------------------
    Parameters:
    --------------------
    file_path : str - This is path to the folder in which the object will be saved.
    object - This is the object, which will be saved.
    
    --------------------
    Returns:
    --------------------
    Saves the object into folder given in the file path. 
    =================================================================================
    '''
    try:
        # Checking if the directory exists and, if not, creating a new directory
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        # Saving the object in the given file path
        with open(file_path, 'wb') as file_obj:
            dill.dump(object, file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function to load the saved object
def load_object(file_path:str):
    '''
    This function will load a pickle object.
    ===================================================================================
    ---------------------
    Parameters:
    ---------------------
    file_path : str - This is the path where the object is stored.
    
    ---------------------
    Returns:
    ---------------------
    The function returns the object after it is loaded.
    ==================================================================================== 
    '''
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function to build addition features using the x, y and z features
def create_aspect_features(df):
    '''
    This function takes the dataframe and creates additional features.
    ================================================================================
    --------------------
    Parameters:
    --------------------
    df : dataframe object - This is the dataframe used to create the features.
    
    --------------------
    Returns:
    --------------------
    df : dataframe object - Returns dataframe object with additional features. 
    =================================================================================
    '''
    try:
        df["volume"] = df["x"] * df["y"] * df["z"]
        df["surface_area"] = 2 * (df["x"] * df["y"] + df["y"] * df["z"] + df["z"] * df["x"])
        df["aspect_ratio_xy"] = df["x"] / df["y"]
        df["diagonal_distance"] = np.sqrt(df["x"] ** 2 + df["y"] ** 2 + df["z"] ** 2)
        df["relative_height"] = (df["z"] - df["z"].min()) / (df["z"].max() - df["z"].min())
        df["relative_position"] = (df["x"] + df["y"] + df["z"]) / (df["x"] + df["y"] + df["z"]).sum()
        df["volume_ratio"] = df["x"] * df["y"] * df["z"] / (df["x"].mean() * df["y"].mean() * df["z"].mean())
        df["length_ratio"] = df["x"] / df["x"].mean()
        df["width_ratio"] = df["y"] / df["y"].mean()
        df["height_ratio"] = df["z"] / df["z"].mean()
        return df
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function to find the best model given the parameters
def find_best_model(X_train, y_train, estimator, params, cv):
    '''
    This function finds the best model, given the parameters for
    that model.
    ================================================================================
    -------------------
    Parameters:
    -------------------
    X_train : numpy array or pandas dataframe - This is the training feature set.
    y_train : numpy array or pandas dataframe - This is the training target set.
    estimator : model object - This is the estimator that will be used.
    params : dict - This is the parameters, which will be used for the grid search.
    cv : model selection object - This is the cross validation object. 
    
    -------------------
    Returns:
    -------------------
    best_model : model object - This is the model with the best parameters.
    =================================================================================
    '''
    try:
        # Instantiating a grid search cross validation
        gs = GridSearchCV(
            estimator=estimator,
            param_grid=params,
            cv=cv,
            scoring='neg_root_mean_squared_error',
            n_jobs=-1
        )
        
        # Fitting the model to the data
        gs.fit(X_train, y_train)
        
        # Capturing the best model
        best_model = gs.best_estimator_
        
        return best_model
    
    except Exception as e:
        raise CustomException(e, sys)
