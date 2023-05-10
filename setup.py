from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'
def get_requrements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace('\n','') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.emove(HYPEN_E_DOT)
        return requirements

setup(
    name='DiamondPriceprediction',
    version='0.0.1',
    author='Rajat',
    author_email='rajatjain852@gmail.com',
    install_requires=get_requrements('requirements.txt'),
    packages=find_packages()
)