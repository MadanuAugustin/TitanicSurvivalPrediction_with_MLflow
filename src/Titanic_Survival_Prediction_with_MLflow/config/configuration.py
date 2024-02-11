from src.Titanic_Survival_Prediction_with_MLflow.constants import *
from src.Titanic_Survival_Prediction_with_MLflow.utils.common import read_yaml, create_directories
from src.Titanic_Survival_Prediction_with_MLflow.entity.config_entity import (DataIngestionConfig, DataValidationConfig)
from logger_file.logger import logger

## The below class is responsible for storing all the folder and file paths

class ConfigurationManager:
    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH,
                 schema_file_path = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories([self.config.artifacts_root])

    
      
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        logger.info(f'ConfigurationManager get_data_ingestion_config function started...!')
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir = config.unzip_dir,
            
        )
        logger.info(f'ConfigurationManager get_data_ingestion_config function completed...!')

        return data_ingestion_config
    

    def get_data_validation_config(self) ->DataValidationConfig:
        logger.info(f'ConfigurationManager get_data_validation_config function started...!')
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE= config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema = schema
        )

        logger.info(f'ConfigurationManager get_data_validation_config function completed...!')

        return data_validation_config



