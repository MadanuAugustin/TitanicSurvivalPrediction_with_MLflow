from logger_file.logger import logger
from src.Titanic_Survival_Prediction_with_MLflow.pipeline.stage_01_dataIngestion import (DataIngestionTrainingPipeline,)
from src.Titanic_Survival_Prediction_with_MLflow.pipeline.stage_02_dataValidation import (DataValidationTrainingPipeline)
                                                                                         
from Exception_file.exception import CustomException
import sys
from logger_file.logger import logger

STAGE_NAME = 'Data_Ingestion_Stage'


try:
    logger.info(f'--------------{STAGE_NAME}-started--------------')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'--------------{STAGE_NAME}-completed-----------------')

except Exception as e:
    raise CustomException(e, sys)


STAGE_NAME = 'Data_Validation_Stage'

try:
    logger.info(f'---------------{STAGE_NAME}-started---------------')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'-------------------{STAGE_NAME}-completed-------------------')
    
except Exception as e:
    raise CustomException(e, sys)