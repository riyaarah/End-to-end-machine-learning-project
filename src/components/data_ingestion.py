import os
import sys
from pathlib import Path
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts', 'train.csv')
    test_data_path:str=os.path.join('artifacts', 'test.csv')
    raw_data_path:str=os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        # repository root (two levels up from src/components)
        self.base_dir = Path(__file__).resolve().parents[2]
        # ensure artifacts are created under repo root
        self.ingestion_config.train_data_path = str(self.base_dir / 'artifacts' / 'train.csv')
        self.ingestion_config.test_data_path = str(self.base_dir / 'artifacts' / 'test.csv')
        self.ingestion_config.raw_data_path = str(self.base_dir / 'artifacts' / 'raw.csv')

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            data_file = self.base_dir / 'notebook' / 'data' / 'stud.csv'
            df = pd.read_csv(str(data_file))
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)#raw data save

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            raise CustomException(e, sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()