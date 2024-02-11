from src.Titanic_Survival_Prediction_with_MLflow.config.configuration import ConfigurationManager
from src.Titanic_Survival_Prediction_with_MLflow.components.data_validation import (DataValidation)
from logger_file.logger import logger

STAGE_NAME = 'Data Validation Stage'

class DataValidationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        logger.info(f'DatValidationTrainingPipeline main function started...!')
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_columns()
        logger.info(f'DataValidationTrainingPipeline main function completed...!')
        