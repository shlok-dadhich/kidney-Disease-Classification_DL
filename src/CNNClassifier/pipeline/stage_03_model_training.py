from CNNClassifier.config.configuration import ConfigurationManager,TrainingConfig
from CNNClassifier.components.model_training import Training
from CNNClassifier import logger

STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self,config:TrainingConfig):
        self.config = config

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelTrainingPipeline(config=TrainingConfig)
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e