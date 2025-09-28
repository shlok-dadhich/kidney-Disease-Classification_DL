import os
import gdown
import zipfile
import os
from pathlib import Path

from CNNClassifier.utils.common import get_size
from CNNClassifier.entity.config_entity import DataInjectionConfig
from CNNClassifier import logger


class DataInjection:
    def __init__(self, config: DataInjectionConfig):
        self.config = config

    def download_file(self):
        """
        Download file from Google Drive using gdown
        """
        os.makedirs("artifacts/data_injection", exist_ok=True)

        if not os.path.exists(self.config.local_data_file):
            logger.info(
                f"Downloading file from: [{self.config.source_URL}] "
                f"to: [{self.config.local_data_file}]"
            )
            gdown.download(
                url=self.config.source_URL,
                output=str(self.config.local_data_file),
                quiet=False
            )
        else:
            logger.info(
                f"File already exists of size: "
                f"[{get_size(Path(self.config.local_data_file))}]"
            )

    def extract_zip_file(self):
        """
        Extracts the downloaded zip file into the configured unzip directory
        """
        unzip_dir = Path(self.config.unzip_dir)
        os.makedirs(unzip_dir, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_dir)
            logger.info(f"Extracted zip file to: {unzip_dir}")
