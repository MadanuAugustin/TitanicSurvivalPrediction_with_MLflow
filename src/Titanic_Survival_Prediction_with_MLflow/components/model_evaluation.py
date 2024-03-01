
from src.Titanic_Survival_Prediction_with_MLflow.entity.config_entity import ModelEvaluationConfig
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import pandas as pd
import joblib
import dagshub
import mlflow
from src.Titanic_Survival_Prediction_with_MLflow.utils.common import save_json
from pathlib import Path
import mlflow.sklearn



class ModelEvaluation:
    def __init__(self, config : ModelEvaluationConfig):
        self.config = config



    def eval_metrics(self, actual, pred):
        precision = precision_score(actual, pred, average='weighted')
        recall = recall_score(actual, pred, average='weighted')
        f1 = f1_score(actual, pred, average='weighted')
        accuracy = accuracy_score(pred, pred)
        return precision, recall, f1, accuracy
    


    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]


        dagshub.init("TitanicSurvivalPrediction_with_MLflow", "augustin7766", mlflow=True)

        mlflow.set_experiment('tenth_exp_10')

        with mlflow.start_run():
            
            predicted = model.predict(test_x)

            (precision, recall, f1, accuracy) = self.eval_metrics(test_y, predicted)


            scores = {'precision' : precision, 'recall' : recall, 'f1' : f1, 'accuracy': accuracy}

            save_json(path = Path(self.config.metric_file_name), data = scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric('precision', precision)
            mlflow.log_metric('recall', recall)
            mlflow.log_metric('f1', f1)
            mlflow.log_metric('accuracy', accuracy)

            mlflow.sklearn.log_model(model, 'model', registered_model_name='RandomForestClassifier')











