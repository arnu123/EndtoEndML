from setuptools import find_packages, setup
#find_packages will find all the packages in the project
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]: #returns list
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # but since all requirements are in separate lines in tat file, it will also include \n, we should remove that
        requirements = [req.replace("\n"," ") for req in requirements]
        print(requirements)
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Arnav',
    author_email = 'arnavaggarwal85@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
)