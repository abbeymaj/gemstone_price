# Importing packages
import sys
import os
import dill
from src.exception import CustomException


# Creating a function to fetch error message details from sys
def fetch_error_message(error, error_detail:sys):
    '''
    This function fetches the error details from the sys package.
    =============================================================
    ------------------
    Parameters:
    ------------------
    error - str : This is the error message.
    error_detail: This is the error detail from the sys package.
    
    ------------------
    Returns:
    ------------------
    error_message - This is the error message from the sys package.
    ==============================================================
    '''
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message = "Error occurred in script name [{0}], line number [{1}], with error message [{2}]".format(file_name, line_no, str(error))
    return error_message


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