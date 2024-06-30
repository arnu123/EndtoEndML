import os
import sys
from src.exception import CustomException #the file we made for exception handling
from src.logger import logging #the file we made for logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig

@dataclass #now u will be able to directly define class variable instead of declaring it in __init__. And if u dont want to define any functions.
class DataIngestionConfig: #for all input things required in dataIngestion
    train_data_path: str = os.path.join('artifacts',"train.csv") #store train data in this path
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv") #initial data

class DataIngestion:
    def __init__(self): #automatically called when object is created
        self.ingestion_config = DataIngestionConfig() #store all 3 paths in this ingestion_config

    def initiate_data_ingestion(self): #read from the database
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv') #reading data from somewhere(mongo, clipboard,local etc)
            logging.info("Read the dataset as dataframe")  #keep writing logs so that when exception happens, u know where the error happened.

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) #create a folder for train data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header = True) #save the data in the raw_data_path

            logging.info("Train test split initiated")
            train_set, test_set= train_test_split(df, test_size = 0.2, random_state = 42) #split the data into train and test
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True) #save the train data
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True) #save the test data

            logging.info("Data ingestion completed") 

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                
            )
        except Exception as e:
            raise CustomException(f"Data ingestion failed due to {str(e)}")


    
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    data_transformation_obj = DataTransformation()
    train_arr,test_arr,_ = data_transformation_obj.initiate_data_transformation(train_data, test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))