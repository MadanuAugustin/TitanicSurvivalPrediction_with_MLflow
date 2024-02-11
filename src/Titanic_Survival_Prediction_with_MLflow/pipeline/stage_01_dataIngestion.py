from src.Titanic_Survival_Prediction_with_MLflow.config.configuration import (ConfigurationManager)
from src.Titanic_Survival_Prediction_with_MLflow.components.data_ingestion import (DataIngestion)
from logger_file.logger import logger
from Exception_file.exception import CustomException
import sys
from logger_file.logger import logger

STAGE_NAME = 'Data_Ingestion_Stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass



    def main(self):
        logger.info(f'DataIngestionTrainingPipeline main function started...!')
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        logger.info(f'DataIngestionTrainingPipeline main function completed...!')



# if __name__ == '__main__':
#     try:
#         logger.info(f'--------------{STAGE_NAME}-started---------------------')
#         obj = DataIngestionTrainingPipeline()
#         obj.main()
#         logger.info(f'----------------{STAGE_NAME}-completed-------------------')
#     except Exception as e:
#         raise CustomException(e, sys)