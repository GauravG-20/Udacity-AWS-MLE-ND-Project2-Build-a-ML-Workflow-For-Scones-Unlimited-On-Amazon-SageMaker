import json
import base64
import boto3

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2023-10-10-06-28-45-621"

runtime_client = boto3.client('sagemaker-runtime')

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['image_data'])

    # Instantiate a Predictor
    predictor = runtime_client.invoke_endpoint(
        EndpointName = ENDPOINT,
        Body = image,
        ContentType = 'image/png'
    )

    # Make a prediction:
    inferences = json.loads(predictor['Body'].read().decode('utf-8'))

    return {
        'statusCode': 200,
        'inferences': inferences
    }