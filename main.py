from cnnimgClassifier import logger
from cnnimgClassifier.pipeline.Stage_01_Data_ingestion import DataIngestionTrainingPipeline
from dotenv import load_dotenv

load_dotenv()


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
