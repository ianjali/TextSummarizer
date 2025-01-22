from src.TextSummarizer.logging import logger
from src.TextSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.TextSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingPipeline

# logger.info("Logging is implemented successfully")
STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(f"stage {STAGE_NAME} failed : {str(e)}")
    raise e
      
STAGE_NAME="Data Transformation stage"
try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_transformation_pipeline=DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(f"stage {STAGE_NAME} failed : {str(e)}")
    raise e