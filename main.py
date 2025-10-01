from CNNClassifier import logger
from CNNClassifier.entity.config_entity import DataInjectionConfig, PrepareBaseModelConfig
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

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
    