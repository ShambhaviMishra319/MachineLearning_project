##A setup.py file in Python is a configuration file used to build and distribute Python packages. It typically contains information about the package, such as its name, version, and dependencies, and it is used by tools like pip to install and manage Python packages from the command line.

from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this func will return the list of req
    '''

    HYPHEN_E_DOT = '-e .'

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name='ML project',
    version='0.0.1',
    author='Shambhavi Mishra',
    author_email='sm1066279@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)