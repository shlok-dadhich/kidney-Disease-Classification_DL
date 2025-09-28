from CNNClassifier.constants import *
from CNNClassifier.utils.common import read_yaml, create_directories
from pathlib import Path
from CNNClassifier.entity.config_entity import DataInjectionConfig

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
