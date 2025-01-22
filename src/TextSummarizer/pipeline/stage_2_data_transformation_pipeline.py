from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.components.data_tranformation import DataTransformation
from src.TextSummarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_transformer_config = config.get_data_transformer_config()
        data_transformer_config=DataTransformation(config=data_transformer_config)
        data_transformer_config.convert()