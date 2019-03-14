import unittest, requests, json, sys, os

sys.path.insert(0, "../")
from server import app

class TestServerApi(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()

	def test_connection(self):
		response = self.app.get('/api')
		self.assertEqual(
			json.loads(response.get_data().decode(sys.getdefaultencoding())), 
			{})
			
	def test_post(self):
		response = self.app.post('/api', data={'name':'Luke Skywalker'})
		self.assertEqual(
			json.loads(response.get_data().decode(sys.getdefaultencoding()))['0']['gender'], 
			'male')


if __name__ == "__main__":
	unittest.main()


