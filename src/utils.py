# Importing packages
import sys


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