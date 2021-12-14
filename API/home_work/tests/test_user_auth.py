import pytest
import requests
from API.home_work.lib.base_case import BaseCase

class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self):
        data = {
            "email": "vinkotov@example.ru",
            "password": "1234"
        }
        response1 = requests.post("https://playgroung.learnqa.ru/api/user/login", data=data)
        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_headers(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

    def test_auth_user(self):

        response1 = requests.get(
            "https://playgroung.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_id": self.auth_sid}
        )
