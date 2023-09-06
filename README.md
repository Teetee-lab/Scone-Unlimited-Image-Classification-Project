# Scone Unlimited; An Image Classification Project on AWS 

![Stepfunction](/images/process.png)

## Overview

Image Classifiers are used in the field of computer vision to identify the content of an image and it is used across a broad variety of industries, from advanced technologies like autonomous and augmented reality to eCommerce platforms. With that being said; in this project, I developed an image classification model that can automatically detect which kind of vehicle delivery drivers have, in order to route them to the correct loading bay and orders. The project focuses on assigning delivery professionals who have a bicycle to nearby orders and giving motorcyclists orders that are farther away.

The goal of the project is to ship a scalable and safe model that can tell bicycles apart from motorcycles.

## Dataset Overview

The data was extracted from the Python version of the CIFAR-100 dataset. The CIFAR dataset is open source and generously hosted by the University of Toronto at: https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz. In order to be able to use the dataset, I transformed the data into a usable shape and format, split it into train and test then saved it into an AWS S3 bucket.

## Project Result

After EDA, I used an AWS build-in image classification algorithm to train the model and deploy it. The model performs at its best with an accuracy of over 80% on the test dataset.

## AWS ML Workflow

**The ML Workflow process** 
![ML Automation](/images/wrkflow.png)

**Lambda Function and Step Function**
![Step Function](/images/stepsimage.png)

**Invoke Lambda function**
![Lambda Invoke - Inference filter](/images/img.png)

**Successful Continous Integration and Continous Deployment using Step Function**
![Sucessful Automation](/images/stepfunctions_graph.png)

## Repository Structure

      ├── Captured Data      <- A folder that stores the captured data from the model predictions            
      ├── images             <- A folder that stores images
      ├── lambda functions    <- A folder that stores the lambda functions
      ├── Scone_unlimited_notebook <- Documentation of the project in Jupyter Notebook
      ├── Stepfunction.json    <- A JSON file that combines all the lambda functions after successful deployment
      ├── lambda.py    <- A Python file to serialize data, classify, and filter inferences.
      ├── stop_instance.py     <- A Python file that stops notebook instances after all deployment is done to save cost.
      └── README.md          <- Top-level README

## Author

Titilayo Amuwo

