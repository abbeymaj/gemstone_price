# Importing packages
from typing import List
from setuptools import setup, find_packages

# Setting Hypen-e dot as a global
HYPHEN_E_DOT = '-e .'

# Creating a function to fetch all packages from requirements.txt
def get_requirements(filepath:str)->List[str]:
    '''
    This function fetches all packages from requirements.txt.
    ===============================================================================
    ----------------
    Parameters:
    ----------------
    - filepath : str -> This is the filepath of the requirements.txt file. 
                  This must be a string.
    
    ----------------
    Returns:
    ----------------
    - List : str -> This is a list of the packages from the requirements.txt file.
    =================================================================================
    '''
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        # Replace any new line with spaces
        requirements = [req.replace("\n", "") for req in requirements]
        
        # Remove hypen e dot if present in requirements.txt
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


# Creating the setup to install packages retrieved from requirements.txt
setup(
    name = 'gemstone_price_prediction',
    author = 'Abhijit Majumdar',
    version = '0.0.1',
    packages = find_packages(),
    install_requires=get_requirements('requirements.txt')
) 