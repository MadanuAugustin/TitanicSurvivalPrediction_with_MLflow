
from pathlib import Path
from src.Titanic_Survival_Prediction_with_MLflow.config.configuration import ConfigurationManager
from src.Titanic_Survival_Prediction_with_MLflow.components.data_transformation import DataTransformation
from Exception_file.exception import CustomException
import sys


STAGE_NAME = 'Data_Transformation_Stage'


class DataTransformationPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path('artifacts//data_validation//status.txt'), 'r') as f:
                status = f.read().split(" ")[-1]


            if status == 'True':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            
            else:
                print('your schema data is not valid..plese check...!')
        except Exception as e:
            raise(e, sys)