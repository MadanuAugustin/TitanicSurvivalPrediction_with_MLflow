
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
import numpy as np





class DataTransformation:
    def __init__(self, config : DataTransformationConfig):
        self.config = config

    
    def preprocessor_fun(self):
        try:

            logger.info(f'numeric and categoric pipelines construction started...!')

            numeric_columns = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']

            categoric_columns = ['Embarked', 'Sex']
            


            numeric_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', RobustScaler(with_centering=False))
                ]
            )

            categoric_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('onehotencoding', OneHotEncoder(drop='first')),
                    ('robustsc', RobustScaler(with_centering=False))
            
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

            train.drop(columns= ['PassengerId', 'Name', 'Ticket', 'Cabin'], axis = 1, inplace = True)
            test.drop(columns = ['PassengerId', 'Name', 'Ticket', 'Cabin'], axis = 1, inplace = True)

            train_X = train.drop(columns = 'Survived', axis = 1)
            train_Y = train[['Survived']]

            test_X = test.drop(columns = 'Survived', axis = 1)
            test_Y = test[['Survived']]


            preprocessor_obj = self.preprocessor_fun()

            train_X = preprocessor_obj.fit_transform(train_X)
            test_X = preprocessor_obj.transform(test_X)

            transformed_train_df = pd.DataFrame(np.c_[train_X, train_Y])
            transformed_test_df = pd.DataFrame(np.c_[test_X, test_Y])

            transformed_train_df.rename(columns={8 : 'Survived'}, inplace=True)
            transformed_test_df.rename(columns={8 : 'Survived'}, inplace=True)

            transformed_train_df.to_csv(os.path.join(self.config.root_dir, 'transformed_train_df.csv'), index = False, header = True)
            transformed_test_df.to_csv(os.path.join(self.config.root_dir, 'transformed_test_df.csv'), index = False, header = True)

            logger.info(f'data-transformation completed and returned transformed data...!')

  
        except Exception as e:
            raise CustomException(e, sys)