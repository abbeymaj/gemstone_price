# Importing packages
from src.logger import logging
from src.components.config_entity import DataIngestionConfig
from src.components.data_transformation import DataTransformation
from src.components.store_features import FeatureStoreCreation

# Running the script
if __name__ == '__main__':
    logging.info('Beginning the creation of the feature store.')
    
    # Getting the train and test data paths
    data_path = DataIngestionConfig()
    train_path = data_path.train_data_path
    test_path = data_path.test_data_path
    
    # Transforming the datasets
    data_transf = DataTransformation()
    train_set, test_set = data_transf.initiate_data_transformation(train_path=train_path, test_path=test_path)
    
    # Saving the transformed datasets into a feature store
    store = FeatureStoreCreation()
    store.create_feature_store(train_set=train_set, test_set=test_set)
    
    logging.info('Feature store has been created.')