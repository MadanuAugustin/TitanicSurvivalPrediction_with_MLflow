
from src.Titanic_Survival_Prediction_with_MLflow.entity.config_entity import ModelTrainerConfig
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os



class ModelTrainer:
    def __init__(self, config : ModelTrainerConfig):
        self.config = config




    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)



        train_x = train_data.drop([self.config.target_column], axis = 1)
        train_y = train_data[[self.config.target_column]]



        classifier = RandomForestClassifier(criterion=self.config.criterion, n_estimators=self.config.n_estimators)

        classifier.fit(train_x, train_y)


        joblib.dump(classifier, os.path.join(self.config.root_dir, self.config.model_name))






