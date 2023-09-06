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