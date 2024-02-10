

import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s : %(message)s]')

PROJECT_NAME = 'Titanic_Survival_Prediction_with_MLflow'


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/common.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/entity/config_entity.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "DockerFile",
    "Requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html",
    "templates/results.html"
]

for filepath in list_of_files:

    filepath = Path(filepath)   # we are converting to windows path

    filedir, filename = os.path.split(filepath)

    if filedir != "":

        os.makedirs(filedir, exist_ok= True)

        logging.info(f"creating directory of : {filedir} for the file : {filename}...!")


    if (not os.path.exists(filename)) or (os.path.getsize == 0):

        # creating the files in write mode
        with open(filepath, 'w') as f:
            pass
        logging.info(f'creating empty file : {filename}')

    else:

        logging.info(f"{filename} already exists...!")


