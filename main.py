from CNNClassifier import logger
from CNNClassifier.entity.config_entity import DataInjectionConfig, PrepareBaseModelConfig,TrainingConfig
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CNNClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
        obj = DataIngestionTrainingPipeline(config=DataInjectionConfig)
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Prepare Base Model Stage"
try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline(config=PrepareBaseModelConfig)
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Training"

try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelTrainingPipeline(config=TrainingConfig)
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e