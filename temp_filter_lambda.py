"""
This sample demonstrates an implementation of the Lex Code Hook Interface
in order to serve a sample bot which manages orders for flowers.
Bot, Intent, and Slot models which are compatible with this sample can be found in the Lex Console
as part of the 'OrderFlowers' template.

For instructions on how to set up and test this bot, as well as additional samples,
visit the Lex Getting Started documentation http://docs.aws.amazon.com/lex/latest/dg/getting-started.html.
"""
# import math
# import dateutil.parser
# import datetime
import json
import time
import os
import logging
import boto3
import pandas as pd


# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

S3 = boto3.client('s3')
bucket_name = 'bento-chat-bucket'
file_name = 'fileOverview.csv'

""" --- Helpers to build responses which match the structure of the necessary dialog actions --- """


def get_slots(intent_request):
    return intent_request['currentIntent']['slots']


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message
        }
    }


def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response


def delegate(session_attributes, slots):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }


""" --- Helper Functions --- """





""" --- Functions that control the bot's behavior --- """


# def order_flowers(intent_request):
#     """
#     Performs dialog management and fulfillment for ordering flowers.
#     Beyond fulfillment, the implementation of this intent demonstrates the use of the elicitSlot dialog action
#     in slot validation and re-prompting.
#     """

#     arm_type1 = get_slots(intent_request)["arm"]
#     arm_type2 = get_slots(intent_request)['arm']
#     # date = get_slots(intent_request)["PickupDate"]
#     # pickup_time = get_slots(intent_request)["PickupTime"]
#     # source = intent_request['invocationSource']

#     if source == 'DialogCodeHook':
#         # Perform basic validation on the supplied input slots.
#         # Use the elicitSlot dialog action to re-prompt for the first violation detected.
#         slots = get_slots(intent_request)

#         slots[validation_result['violatedSlot']] = None
#         return elicit_slot(intent_request['sessionAttributes'],
#                             intent_request['currentIntent']['name'],
#                             slots,
#                             validation_result['violatedSlot'],
#                             validation_result['message'])

#         # Pass the price of the flowers back through session attributes to be used in various prompts defined
#         # on the bot model.
#         output_session_attributes = intent_request['sessionAttributes'] if intent_request['sessionAttributes'] is not None else {}


#         return delegate(output_session_attributes, get_slots(intent_request))

#     # Order the flowers, and rely on the goodbye message of the bot to define the message to the end user.
#     # In a real bot, this would likely involve a call to a backend service.
#     return close(intent_request['sessionAttributes'],
#                  'Fulfilled',
#                  {'contentType': 'PlainText',
#                   'content': 'Thanks, your order for {} has been placed and will be ready for pickup by {} on {}'.format(flower_type, pickup_time, date)})


""" --- Intents --- """


def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    logger.debug('dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))

    intent_name = intent_request['currentIntent']['name']

    # Dispatch to your bot's intent handlers
    if intent_name == 'PerformFilter':
        return order_flowers(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')


""" --- Main handler --- """


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # By default, treat the user request
    
    obj = S3.get_object(Bucket = bucket_name , Key = file_name)
    my_df = pd.read_csv(obj['Body'])
    
    intent = event['sessionState']['intent']['name']

    # bot = event['sessionState']['bot']['name']
    # slots = event['sessionState']['intent']['slots']

    if(intent == 'PerformView'):
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
            }
            ]
        }
    elif(intent == 'PerformFilter'):
        # filter_df = pd.read_csv(obj['Body'])
        
        slots = event['sessionState']['intent']['slots']
        field = slots['Field']['value']['interpretedValue']
        arm1 = slots['ArmButtonSelect1']['value']['interpretedValue']
        arm2 = slots['ArmButtonSelect2']['value']['interpretedValue']
        
        # arms = [arm1,arm2]
        # filtered_df = my_df[my_df['field'] in arms]]
        # new_df = filter_df
    
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
                'content': str(arm1)
            },
            {
                'contentType': 'PlainText',
                'content': str(arm2)
            },
            {
                'contentType': 'PlainText',
                'content': str(field)
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
