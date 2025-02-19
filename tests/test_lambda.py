import json
from lambda_function import lambda_handler


def test_lambda():
    # Lambda 関数を実行
    response = lambda_handler({}, None)

    # レスポンスの検証
    assert response["statusCode"] == 200  # HTTP ステータスコード
    body = json.loads(response["body"])
    assert body["message"] == "Hello, sleek!"
