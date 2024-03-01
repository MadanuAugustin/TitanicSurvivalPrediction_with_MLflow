from logger_file.logger import logger
from src.Titanic_Survival_Prediction_with_MLflow.pipeline.stage_01_dataIngestion import (DataIngestionTrainingPipeline,)
from src.Titanic_Survival_Prediction_with_MLflow.pipeline.stage_02_dataValidation import (DataValidationTrainingPipeline)
from src.Titanic_Survival_Prediction_with_MLflow.pipeline.stage_03_dataTransformation import (DataTransformationPipeline)
from src.Titanic_Survival_Prediction_with_MLflow.pipeline.stage_05_ModelEvaluation import ModelEvaluationTrainingPipeline
from src.Titanic_Survival_Prediction_with_MLflow.pipeline.stage_04_modelTraining import ModelTrainingPipeline
                                                                                         
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



STAGE_NAME = 'Data_Transformatin_Stage'

try:
    logger.info(f'--------------------------{STAGE_NAME} started---------------------')
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    
except Exception as e:
    raise CustomException(e, sys)



STAGE_NAME = 'Model_Training_Stage'

try:
    logger.info(f'------------------------{STAGE_NAME} started------------------')
    model_training = ModelTrainingPipeline()
    model_training.main()
except Exception as e:
    raise CustomException(e, sys)



STAGE_NAME = 'Model_Evaluation_Stage'

try:
    logger.info(f'-----------------------{STAGE_NAME} started----------------------')
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
except Exception as e:
    raise CustomException(e, sys)
