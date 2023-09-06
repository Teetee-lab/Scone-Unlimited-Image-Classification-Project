import boto3

def stop_sagemaker_instances():
    try:
        # Initialize the SageMaker client
        sagemaker_client = boto3.client('sagemaker')

        # List SageMaker instances
        instances = sagemaker_client.list_notebook_instances()

        # Loop through instances and stop them
        for instance in instances['NotebookInstances']:
            instance_name = instance['NotebookInstanceName']
            instance_status = instance['NotebookInstanceStatus']
            #if instance is running
            
            if instance_status != "InService":
                print(f"{instance_name} isn't in service")

            if instance_status == "InService" :
                sagemaker_client.stop_notebook_instance(NotebookInstanceName=instance_name)
                print(f"Stopped SageMaker instance {instance_name}")

    
    except Exception as e:
        print(f"Error: {str(e)}")

def lambda_handler(event, context):
    stop_sagemaker_instances()