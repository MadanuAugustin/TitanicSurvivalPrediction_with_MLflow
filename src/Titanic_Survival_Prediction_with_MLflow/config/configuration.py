from src.Titanic_Survival_Prediction_with_MLflow.constants import *
from src.Titanic_Survival_Prediction_with_MLflow.utils.common import read_yaml, create_directories
from src.Titanic_Survival_Prediction_with_MLflow.entity.config_entity import (DataIngestionConfig, DataValidationConfig,
                                                                              DataTransformationConfig, ModelTrainerConfig,
                                                                              ModelEvaluationConfig)
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
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation


        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path
        )

        return data_transformation_config
    



    def get_model_trainer_config(self)-> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.RandomForestClassifier
        schema = self.schema.TARGET_COLUMN


        create_directories([config.root_dir])


        model_trainer_config =ModelTrainerConfig(
            root_dir =  config.root_dir,
            train_data_path= config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            criterion= params.criterion,
            n_estimators=params.n_estimators,
            target_column=schema.name
        )

        return model_trainer_config
    



    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.RandomForestClassifier
        schema = self.schema.TARGET_COLUMN


        create_directories([config.root_dir])


        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            all_params=params,
            metric_file_name=config.metric_file_name,
            target_column=schema.name,
            mlflow_uri='https://dagshub.com/augustin7766/TitanicSurvivalPrediction_with_MLflow.mlflow'
        )

        return model_evaluation_config



