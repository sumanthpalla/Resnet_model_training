# Image Classification Task of CIFAR-10 using Convolutional Neural Networks and Residual Neural Networks

This Repository is intended to understand about ResNet models and understand their architecture and train them to classify CIFAR-10 dataset. The proposed dataset is also trained with custom designed Convolutional Neural Networks and ResNet 18. 
<p align="center">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
</p>

## Project Description

This repository provides a complete implementation of the ResNet-18 architecture, a deep residual network renowned for its simplicity and effectiveness in image classification tasks. The model is trained on the CIFAR-10 dataset, which contains 60,000 32x32 color images in 10 classes. The focus of this project is to build and train the ResNet-18 model and some custom CNNs with varying arhitectures from the ground up, achieving high accuracy, and exploring the learned feature space of the model.

## Virtual Environment

Create a virtual environment by installing the packages in requirements.txt. This is made using Pytorch 2.8 which requires python >= 3.9

## Data
The data is downloaded to your current directory by using the following command on your terminal after cloning this repository

https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz

```bash
curl -o cifar-10.tar.gz  https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz

mkdir data

tar -xzvf cifar-10-python.tar.gz -C ./data

rm cifar-10.tar.gz
```

## Data Preparation



## References

