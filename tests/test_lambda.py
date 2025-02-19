import json
import pytest
import requests
from unittest.mock import patch
from lambda_function import lambda_handler


# `requests.get` をモック化し、APIレスポンスをシミュレーション
@patch("requests.get")
def test_lambda(mock_get):
    # モックのレスポンスを設定（例: GitHub API の 200 OK を模倣）
    mock_get.return_value.status_code = 200

    # Lambda 関数を実行
    response = lambda_handler({}, None)

    # レスポンスの検証
    assert response["statusCode"] == 200  # HTTP ステータスコード
    body = json.loads(response["body"])
    assert body["message"] == "Hello, Lambda!"
    assert body["api_status"] == 200  # API ステータスコード
