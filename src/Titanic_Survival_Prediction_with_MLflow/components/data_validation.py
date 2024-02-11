from src.Titanic_Survival_Prediction_with_MLflow.entity.config_entity import DataValidationConfig
import pandas as pd
from logger_file.logger import logger
from Exception_file.exception import CustomException
import sys

class DataValidation:
    def __init__(self, config : DataValidationConfig):
        self.config = config


    def validate_all_columns(self) -> bool:
        try:
            logger.info(f'DataValidation validate_all_columns function started...!')
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'Validation status : {validation_status}')

            

                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'Validation status : {validation_status}')
            

            return validation_status
        

            

        except Exception as e:
            raise CustomException(e, sys)
        
        
