from src.Titanic_Survival_Prediction_with_MLflow.entity.config_entity import (DataIngestionConfig)
import os
import urllib.request as request
from logger_file.logger import logger
from src.Titanic_Survival_Prediction_with_MLflow.utils.common import get_size
from pathlib import Path
import zipfile
from logger_file.logger import logger


class DataIngestion:
    def __init__(self, config : DataIngestionConfig):
        self.config = config

    ## The below function is responsible for downloading the zip file from URL and saving it in the local repository
        
    def download_file(self):
        logger.info(f'DataIngestion download_file function started...!')
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
                )
            logger.info(f'{filename} has been downloaded with the following info : \n{headers}')
            logger.info(f'DataIngestion download_file function completed...!')

        else:
            logger.info(f'file already exists of size : {get_size(Path(self.config.local_data_file))}')
            logger.info(f'DataIngestion download_file function completed...!')
            pass


    def extract_zip_file(self):
        logger.info(f'DataIngestion extract_zip_file started...!')
        unzip_file = self.config.unzip_dir
        os.makedirs(unzip_file , exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file , 'r') as zip:
            zip.extractall(unzip_file)
            logger.info(f'DataIngestion extract_zip_file completed...!')
