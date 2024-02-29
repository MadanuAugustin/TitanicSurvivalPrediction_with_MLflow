
from src.Titanic_Survival_Prediction_with_MLflow.entity.config_entity import DataTransformationConfig
import pandas as pd
from logger_file.logger import logger
from sklearn.model_selection import train_test_split
import os
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import OneHotEncoder
from Exception_file.exception import CustomException
import sys





class DataTransformation:
    def __init__(self, config : DataTransformationConfig):
        self.config = config

    
    def preprocessor_fun(self):
        try:

            logger.info(f'numeric and categoric pipelines construction started...!')

            numeric_columns = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']

            categoric_columns = ['Embarked']


            numeric_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', RobustScaler())
                ]
            )

            categoric_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('onehotencoding', OneHotEncoder())
                ]
            )

            preprocessor = ColumnTransformer(
                [
                    ('numericPipeline', numeric_pipeline, numeric_columns),
                    ('categoricPipeline', categoric_pipeline, categoric_columns)
                ]
            )

            logger.info(f'numeric and categoric pipelines construction completed and returned preprocessor...!')

            return preprocessor
        except:
            pass

    
    def train_test_splitting(self):
        try:
            mydata = pd.read_csv(self.config.data_path)

            logger.info('train-test-split started...!')

            train, test = train_test_split(mydata)


            train.to_csv(os.path.join(self.config.root_dir, 'train_raw.csv'), index= False, header = True)
            test.to_csv(os.path.join(self.config.root_dir, 'test_raw.csv'), index = False, header = True)

            logger.info(f'train-test-split completed...!')
            logger.info(f'data-transformation started...!')

            train.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis = 1, inplace = True)
            test.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis = 1, inplace = True)

            target_column = 'Survived'

            train_X = train.drop(columns = [target_column], axis = 1)
            train_Y = train[[target_column]]

            test_X = test.drop(columns = [target_column], axis = 1)
            test_Y = test[[target_column]]


            preprocessor_obj = self.preprocessor_fun()

            transformed_train_data = preprocessor_obj.fit_transform(train_X)
            transformed_test_data = preprocessor_obj.transform(test_X)


            transformed_train_data = pd.DataFrame(transformed_train_data)
            transformed_test_data = pd.DataFrame(transformed_test_data)

            transformed_train_df = pd.concat([transformed_train_data, train_Y], axis = 1)
            transformed_test_df = pd.concat([transformed_test_data, test_Y], axis = 1)

            transformed_train_df.to_csv(os.path.join(self.config.root_dir, 'transformed_train_df.csv'), index = False, header = True)
            transformed_test_df.to_csv(os.path.join(self.config.root_dir, 'transformed_test_df.csv'), index = False, header = True)

            logger.info(f'data-transformation completed and returned transformed data...!')

  
        except Exception as e:
            raise CustomException(e, sys)