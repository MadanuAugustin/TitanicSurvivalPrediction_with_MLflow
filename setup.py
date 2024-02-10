

from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    content = f.read()



setup(
    name = 'TitanicSurvivalPrediction_with_MLflow',
    version= '0.0.0.0',
    author = 'augustin',
    author_email= 'augustin7766@gmail.com',
    description='ML-End-End-Project',
    long_description=content,
    url=  'https://github.com/MadanuAugustin/TitanicSurvivalPrediction_with_MLflow.git',
    packages = find_packages()
)