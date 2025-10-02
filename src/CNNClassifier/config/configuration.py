from CNNClassifier.constants import *
from CNNClassifier.utils.common import read_yaml, create_directories
from pathlib import Path
from CNNClassifier.entity.config_entity import DataInjectionConfig, PrepareBaseModelConfig, TrainingConfig
import os
class ConfigurationManager:
    def __init__(self,
                 config_filepath=Config_PATH,
                 params_filepath=Params_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_injection_config(self) -> DataInjectionConfig:
        config = self.config.data_injection
        create_directories([config.root_dir])
        data_injection_config = DataInjectionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )
        return data_injection_config
    

    def get_prepare_base_model_config(self) ->PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        params = self.params
        create_directories([config.root_dir])
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=params.IMAGE_SIZE,
            params_learning_rate=params.LEARNING_RATE,
            params_include_top=params.INCLUDE_TOP,
            params_weights=params.WEIGHTS,
            params_classes=params.CLASSES
        )
        return prepare_base_model_config    
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_injection.unzip_dir,"CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone")
        create_directories([Path(training.root_dir)])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_batch_size=params.BATCH_SIZE,
            params_epochs=params.EPOCHS,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )
        return training_config
    
