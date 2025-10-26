
import mlflow
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, random_split

from models import 

def train_model():
    """
    Trains the ResNet-18 model on the CIFAR-10 dataset.
    This function initializes the model, loads the dataset, and performs training over a specified number of epochs. The 
    train loss, validation loss, and accuracy are logged for each epoch using mlflow.

    Steps: 

    1. In

    Returns:
        None
    """