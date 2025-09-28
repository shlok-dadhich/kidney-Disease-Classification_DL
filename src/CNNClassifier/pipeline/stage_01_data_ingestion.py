from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.data_ingestion import DataInjection
from CNNClassifier import logger
from CNNClassifier.entity.config_entity import DataInjectionConfig
from CNNClassifier.utils.common import read_yaml, create_directories
from pathlib import Path
import os

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self, config: DataInjectionConfig):
        self.config = config
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_injection_config()
        data_ingestion = DataInjection(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
        obj = DataIngestionTrainingPipeline(config=DataInjectionConfig)
        obj.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e