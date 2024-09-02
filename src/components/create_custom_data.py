# Importing packages
import sys
import pandas as pd 
from src.exception import CustomException

# Creating a class to convert the user entered data into a pandas dataframe
class CustomData():
    '''
    This class takes the data entered by the user on the website and the converts the data
    into a dataframe (for data transformation and predictions).
    '''
    # Creating the constructor for the class
    def __init__(self,
                 carat:float,
                 cut:str,
                 color:str,
                 clarity:str,
                 x:float,
                 y:float,
                 z:float
                 ):
        '''
        This is the constructor for the class and lists the data that will be entered by the
        user on the website.
        '''
        self.carat = carat
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.x = x
        self.y = y
        self.z = z
    
    # Creating the method to convert the online data into a dataframe
    def create_dataframe(self):
        '''
        This method takes the data input by the user and returns a dataframe. The method 
        converts the data, input by the user on the website, into a dictionary and then creates
        a pandas dataframe using the dictionary.
        ========================================================================================
        -----------------------
        Returns:
        -----------------------
        df : pandas dataframe - A pandas dataframe of the data entered by the user.
        ========================================================================================
        '''
        try:
            # Converting the data into a dictionary 
            custom_data_input_dict = {
                'carat': [self.carat],
                'cut': [self.cut],
                'color': [self.color],
                'clarity': [self.clarity],
                'x': [self.x],
                'y': [self.y],
                'z': [self.z]
            }
            
            # Coverting the data dictionary into a pandas dataframe
            df = pd.DataFrame(custom_data_input_dict)
            
            return df
        
        except Exception as e:
            raise CustomException(e, sys)