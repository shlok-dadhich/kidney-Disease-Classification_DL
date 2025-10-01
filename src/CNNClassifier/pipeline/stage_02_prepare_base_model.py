from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.prepare_base_model import PrepareBaseModel
from CNNClassifier import logger
from CNNClassifier.entity.config_entity import PrepareBaseModelConfig
from CNNClassifier.utils.common import read_yaml, create_directories
from pathlib import Path

STAGE_NAME = "Prepare Base Model Stage"
class PrepareBaseModelTrainingPipeline:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config
    
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline(config=PrepareBaseModelConfig)
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e