# import unittest
# from main import create_app, db
# from models.Collection import Collection

# class TestCollections(unittest.TestCase):
#     @classmethod
#     def setUp(cls):
#         cls.app = create_app()
#         cls.app_context = cls.app.app_context()
#         cls.app_context.push()
#         cls.client = cls.app.test_client()
#         db.create_all()

#         runner = cls.app.test_cli_runner()
#         result_seed = runner.invoke(args=["db-custom", "seed"])
#         if result_seed.exit_code != 0:
#             raise ValueError(result_seed.stdout)

#         cls.headers = {}
#         for i in range(1,6):
#             cls.login = cls.client.post(
#                 "users/login",
#                 json={
#                     "email": f"test{i}@test.com",
#                     "password": "123456"
#                 }
#             )
#             cls.token = cls.login.get_json()["token"]
#             cls.header = {"Authorization" : f"Bearer {cls.token}"}
#             cls.headers[f"test{i}"] = cls.header
#         cls.headers["fakeuser"] = {"Authorization": "Bearer invalid_token"}

#     @classmethod
#     def tearDown(cls):
#         db.session.remove()
#         db.drop_all()
#         cls.app_context.pop()

#     def test_collection_index(self):
#         response = self.client.get("/collections/")
#         data = response.get_json()

#         self.assertEqual(response.status_code, 200)
#         self.assertIsInstance(data,list)
    
#     # def test_collection_create(self):
#     #     response = self.client.post("/collections/", json={
#     #         "name": "Test Collection",
#     #         "description": "testing collection create",
#     #         "collaborative": False,
#     #         "public": True
#     #     })

#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertIsInstance(data, dict)
#     #     self.assertTrue(bool("id" in data.keys()))

#     #     collection = Collection.query.get(data["id"])
#     #     self.assertIsNotNone(collection)        
