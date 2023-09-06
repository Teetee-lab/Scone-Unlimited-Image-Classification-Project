import json
import boto3
import base64


#The next function is responsible for the classification part - we're going to take the 
#image output from the previous function, decode it, and then pass inferences back to the the Step Function

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