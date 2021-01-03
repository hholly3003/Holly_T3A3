import unittest
from main import create_app, db
from tests.helpers import Helpers

class TestUsers(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()

        runner = cls.app.test_cli_runner()
        result_seed = runner.invoke(args=["db-custom", "seed"])
        if result_seed.exit_code != 0:
            raise ValueError(result_seed.stdout)

        cls.headers = {}
        for i in range(1,6):
            cls.login = cls.client.post(
                "users/login",
                json={
                    "email": f"test{i}@test.com",
                    "password": "123456"
                }
            )
            cls.token = cls.login.get_json()["token"]
            cls.header = {"Authorization" : f"Bearer {cls.token}"}
            cls.headers[f"test{i}"] = cls.header
        cls.headers["fakeuser"] = {"Authorization": "Bearer invalid_token"}

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
    
    def test_users_register(self):
        endpoint = "/users/register"
        body = {
                "email": "user1@testing.com",
                "password": "abcdef",
                "subscription_status": "1"}
        response, data = Helpers.post_request(endpoint, body=body)
        response2, data2 = Helpers.post_request(endpoint, body=body)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["user_id"], 6)
        self.assertEqual(data["email"], "user1@testing.com")
        self.assertEqual(data["subscription_status"], True)
        self.assertEqual(response2.status_code, 401)
        self.assertIsNone(data2)