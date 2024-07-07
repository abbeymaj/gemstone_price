# Importing packages
from src.components.model_trainer import ModelTrainer

# Creating a model training pipeline script
if __name__ == '__main__':
    model_trainer = ModelTrainer()
    _, model_metric = model_trainer.initiate_model_training()
    print(model_metric)
 