# Import the relevant packages utilized
import requests
import pandas as pd

# Establish the GraphQL endpoint URL
url = 'https://bento-tools.org/v1/graphql/'

# In our sample deployment demonstrated on 7/25, we utilized this query
# This could be expanded for further deployment to include all records, or more objects
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

# Send the request
try:
    response = requests.post(url, json=payload)
    response.raise_for_status()  # Will raise an error for bad status
    result = response.json()
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    result = None

if result:
    # Extract relevant data
    try:
        file_data = result['data']['fileOverview']
        # Create DataFrame
        df = pd.DataFrame(file_data)
        
        # Save DataFrame to CSV, in this case we named it after the queried object
        df.to_csv('fileOverview.csv', index=False)
        
        print("CSV file 'fileOverview.csv' created successfully.")
    except KeyError as e:
        print(f"Key error: {e}")
else:
    print("No data retrieved from the GraphQL endpoint.")
