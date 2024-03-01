
from src.Titanic_Survival_Prediction_with_MLflow.config.configuration import ConfigurationManager
from src.Titanic_Survival_Prediction_with_MLflow.components.model_training import ModelTrainer






STAGE_NAME = 'Model_Training_Stage'



class ModelTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config = model_trainer_config)
        model_trainer_config.train()
