import requests

# GraphQL endpoint URL
url = 'https://bento-tools.org/v1/graphql/'

# Define the query
query = """
query {
  fileOverview {
        file_id
        file_name
        association
        file_description
        file_format
        file_size
        program
        arm
        subject_id
        sample_id
        diagnosis
    }
}
"""

# Construct the payload
payload = {
    "query": query,
    "variables": {}
}

# Receive the request
try:
    response = requests.post(url, json=payload)
    response.raise_for_status() #Will Raise an Error for Bad Status
    result = response.json()
    print(result)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
