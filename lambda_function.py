import json
import requests


def lambda_handler(event, context):
    response = requests.get("https://api.github.com")
    api_status = response.status_code
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello, Lambda!", "api_status": api_status}),
    }
