from access import aws_access
import boto3

def get_filter_selection(user_option, initial_option, filter_value, confirmation):

    runtime_client = boto3.client('lexv2-runtime', region_name = 'us-east-1', aws_access_key_id = aws_access.aws_access_key_id,
                              aws_secret_access_key = aws_access.aws_secret_access_key, aws_session_token = aws_access.aws_session_token)
    botId = "42BS4C4PHY"
    botAliasId = "TSTALIASID"
    localeId = "en_US"
    sessionId = '100'

    response = runtime_client.recognize_text(
    botId = botId,
    botAliasId = botAliasId,
    localeId = localeId,
    sessionId = sessionId,
    text = user_option
    )
    
    response = runtime_client.recognize_text(
    botId = botId,
    botAliasId = botAliasId,
    localeId = localeId,
    sessionId = sessionId,
    text = initial_option
    )

    response = runtime_client.recognize_text(
    botId = botId,
    botAliasId = botAliasId,
    localeId = localeId,
    sessionId = sessionId,
    text = filter_value
    )

    response = runtime_client.recognize_text(
    botId = botId,
    botAliasId = botAliasId,
    localeId = localeId,
    sessionId = sessionId,
    text = confirmation
    )
    filter_option = response['interpretations'][0]['intent']['slots']['filter_value']['value']['resolvedValues'][0]
    runtime_client.close()

    print(filter_option)
    return filter_option