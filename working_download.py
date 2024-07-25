import boto3
import pandas as pd
from io import StringIO # python3; python2: BytesIO 
import boto3

S3 = boto3.client('s3')
bucket_name = 'bento-chat-bucket'
file_name = 'fileOverview.csv'


""" --- Main handler --- """


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # By default, treat the user request
    
    
    
    intent = event['sessionState']['intent']['name']

    # bot = event['sessionState']['bot']['name']
    # slots = event['sessionState']['intent']['slots']

    if(intent == 'PerformView'):
        obj = S3.get_object(Bucket = bucket_name , Key = file_name)
        my_df = pd.read_csv(obj['Body'])
        # Construct the response for Lex
        return {
        "sessionState": {
            'dialogAction': {
                'type': 'Close'
                },
            "intent": {
                "confirmationState": "Confirmed",
                "name": "PerformView",
                "state": "Fulfilled"
                }
            },
        'messages': [
            {
                'contentType': 'PlainText',
                'content': str(my_df)
            },
            {
                'contentType': 'PlainText',
                'content': 'Here are your summary statistics...'
            },
            {
                'contentType': 'PlainText',
                'content': str(my_df.describe(include='all'))
            },
            {
                'contentType': 'CustomPayload',
                'content': 'https://bento-chat-bucket.s3.amazonaws.com/fileOverview.csv'
            }
            ]
        }
    elif(intent == 'PerformFilter'):
        csv_buffer = StringIO()
        s3_resource = boto3.resource('s3')
        
        obj = S3.get_object(Bucket = bucket_name , Key = file_name)
        my_df = pd.read_csv(obj['Body'])
        
        slots = event['sessionState']['intent']['slots']
        field = slots['Field']['value']['interpretedValue']
        arm1 = slots['ArmButtonSelect1']['value']['interpretedValue']
        arm2 = slots['ArmButtonSelect2']['value']['interpretedValue']
        
        new_df = my_df[my_df[field].isin([arm1, arm2])]
        new_df.to_csv(csv_buffer)
        s3_resource.Object('bento-chat-bucket', 'filterResult.csv').put(Body=csv_buffer.getvalue())
        
        
        
        A = 'Here are your summary statistics for your selections of '
        
        # s3_resource.Object(Bucket="bento-chat-bucket", Key='filtered_file.csv').put(Body=csv_buffer.getvalue())
        return {
        "sessionState": {
            'dialogAction': {
                'type': 'Close'
            },
            "intent": {
                "confirmationState": "Confirmed",
                "name": "PerformFilter",
                "state": "Fulfilled"
            }
        },
        'messages': [
            {
                'contentType': 'PlainText',
                'content': str(new_df)
            },
            {
                'contentType': 'PlainText',
                'content': str(A+field)
            },
            {
                'contentType': 'PlainText',
                'content': str(new_df[field].describe(include='all'))
            },
            {
                'contentType': 'CustomPayload',
                'content': 'https://bento-chat-bucket.s3.amazonaws.com/filterResult.csv'
            }
            ]
        }
    else:
        return {
        "messages":[
            {'contentType': 'PlainText',
                'content': 'Failure here'
            }]
        }
