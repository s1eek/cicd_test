import json
from lambda_function import lambda_handler


def test_lambda():
    response = lambda_handler({}, None)
    assert response["statusCode"] == 200
    assert json.loads(response["body"])["message"] == "Hello, Lambda!"
