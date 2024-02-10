
import os
import yaml
import sys
import json
import joblib
from box import ConfigBox
from pathlib import Path
from typing import Any
from logger_file.logger import logger
from Exception_file.exception import CustomException


##  The below method is used for reading the yaml files...

def read_yaml(path_to_yaml:Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file : {path_to_yaml} loaded successfully...!')
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e, sys)
    

## The below method is used for creating the directories...

def create_directories(path_to_directories : list, verbose = True):   
    for path in path_to_directories:
        os.makedirs(path, exist_ok= True)

        if verbose:
            logger.info(f"created directory at : {path}...!")


## The below method is used for saving the json files...

def save_json(path: Path, data : dict):

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    
    logger.info(f'json file saved at {path}...!')


## The below method is used for loading the json files...

def load_json(path : Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)

    logger.info(f'json file loaded successfully from : {path}')
    return ConfigBox(content)



## The below method is used for saving the pickel files or joblib files

def save_bin(data : Any, path : Path):
    joblib.dump(value=data, filename=path)
    logger.info(f'joblib file saved at {path}...!')



## The below method is used for loading the pickel files or joblib files

def load_bin(path : Path) -> Any:
    data = joblib.load(path)
    logger.info(f'joblib file loaded from {path}...!')
    return data


## The below method is used for getting the size of the files

def get_size(path : Path) -> str:
    size_in_kb  = round(os.path.getsize(path)/1024)
    return f'The size of the file : {path} is {size_in_kb}KB'

