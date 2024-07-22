import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'bento-kendra-test-bucket'
    file_name = 'users.csv'

    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    file_content = response["Body"].read().decode('utf-8')

    # Construct the response for Lex
    return {
        "sessionState": {
            'dialogAction': {
                'type': 'Close'
            },
            "intent": {
                "confirmationState": "Confirmed",
                "name": "PerformViewIntent",
                "state": "Fulfilled"
            }
        },
        'messages': [
            {
                'contentType': 'PlainText',
                'content': str(file_content).upper()
            }
        ]
    }
