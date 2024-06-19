import requests
import json

# GraphQL endpoint URL
url = 'https://bento-tools.org/v1/graphql/'

# Define the query
query = """
query {
  program {
    program_id
    program_name
  }
  study_subject {
    study_subject_id
    study_subject_first_name
  }
  demographic_data {
    gender
    height
  }
  diagnosis {
    diagnosis_id
    tumor_stage
    primary_diagnosis
    hpv_status
    treatment_data
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
    
    # Writing JSON data to a file
    with open('data2.txt', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

