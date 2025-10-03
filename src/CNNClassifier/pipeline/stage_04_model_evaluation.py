from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.model_evaluation import Evaluation
from CNNClassifier import logger
from CNNClassifier.entity.config_entity import EvaluationConfig
from CNNClassifier.utils.common import read_yaml, create_directories,save_json
from pathlib import Path

STAGE_NAME = "Model Evaluation Stage"
class ModelEvaluationPipeline:
    def __init__(self, config: EvaluationConfig):
        self.config = config
    
    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        evaluation = Evaluation(config=evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelEvaluationPipeline(config=EvaluationConfig)
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e