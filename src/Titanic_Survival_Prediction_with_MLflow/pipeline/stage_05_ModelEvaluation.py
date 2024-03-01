
from src.Titanic_Survival_Prediction_with_MLflow.config.configuration import ConfigurationManager
from src.Titanic_Survival_Prediction_with_MLflow.components.model_evaluation import ModelEvaluation





STAGE_NAME = 'MODEL_EVALUATION_STAGE'



class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()