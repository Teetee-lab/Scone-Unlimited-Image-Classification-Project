#The first Lambda function will copy an object from S3, base64 encode it, and then return it to the step function as image_data in an event.

import json
import boto3
import base64

import botocore

#The first Lambda function will copy an object from S3, base64 encode it, 
#and then return it to the step function as image_data in an event"""

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""
    
    # Get the s3 address from the Step Function event input
    key = event['s3_key'] ## TODO: fill in
    bucket = event['s3_bucket'] ## TODO: fill in
    
    # Download the data from s3 to /tmp/image.png
    s3.download_file(bucket, key, "/tmp/image.png") ## TODO: fill in
    
    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())
    

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }


#********************************************************************************************************
#The second function is responsible for the classification part - we're going to take the image output from the previous function, 
#decode it, and then pass inferences back to the the Step Function.


import json
import boto3
import base64


runtime_client = boto3.client('runtime.sagemaker') 

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2023-09-01-05-34-44-038"## TODO: fill in

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['image_data'])## TODO: fill in

    # Instantiate a Predictor
    response = runtime_client.invoke_endpoint(EndpointName = ENDPOINT, 
                                               Body = image, 
                                               ContentType = 'image/png')## TODO: fill in
    # Make a prediction:
    inferences = response['Body'].read().decode('utf-8')## TODO: fill in
    
    # We return the data back to the Step Function    
    event["inferences"] = [float(x) for x in inferences[1:-1].split(',')]
    
    
    return {
        'statusCode': 200,
        'body': {
            "inferences": event['inferences'], # Output of predictor.predict
            "s3_key": event['s3_key'], # Source data S3 key
            "s3_bucket": event['s3_bucket'], # Source data S3 bucket
            "image_data": event['image_data']  # base64 encoded string containing the image data
            }
    } 


#**************************************************************************************************************************
#Finally, we need to filter low-confidence inferences. 
#Define a threshold between 1.00 and 0.000 for your model: what is reasonble for you? 
#If the model predicts at `.70` for it's highest confidence label, do we want to pass that inference along to downstream systems? 
#Make one last Lambda function and tee up the same permissions:

import json

            
THRESHOLD = .75

def lambda_handler(event, context):
    
    # Grab the inferences from the event
    inferences = event['inferences']## TODO: fill in
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = max(list(inferences))## TODO: fill in
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': {
            "inferences": event['inferences'], # Output of predictor.predict
            "s3_key": event['s3_key'], # Source data S3 key
            "s3_bucket": event['s3_bucket'], # Source data S3 bucket
            "image_data": event['image_data']  # base64 encoded string containing the image data
            }
    }