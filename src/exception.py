# Importing packages
import sys
from src.utils import fetch_error_message


# Creating a custom exception class to handle errors given by the system.
# This custom class will inherit from the python Exception class.
class CustomException(Exception):
    '''
    The CustomException class is a custom class to handles errors. This class inherits from the Exception class.
    This class contains two functions - The constructor and a function to display the error message.
    '''
    # Defining the contructor
    def __init__(self, error_message, error_detail:sys):
        # Initiating the parent class and passing the error message to it
        super().__init__(error_message)
        self.error_message = fetch_error_message(error_message, error_detail=error_detail)
    
    # Creating a function to print the error message
    def __str__(self):
        return self.error_message
