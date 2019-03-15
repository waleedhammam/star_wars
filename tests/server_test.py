import unittest, requests, json, sys, os

sys.path.insert(0, "../")
from server import app, request

class TestServer(unittest.TestCase):
	'''
	setup and tear down
	'''
	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['DEBUG'] = False
		self.app = app.test_client()

	def tearDown(self):
		pass

	'''
	tests
	'''
	def test_api_is_up(self):
		response = self.app.get('/api')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content_type, "application/json")
		self.assertEqual(
			json.loads(response.get_data().decode(sys.getdefaultencoding())), 
			{})

	def test_one_characer(self):
		response = self.app.post('/api', data={'name':'Luke Skywalker'})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content_type, "application/json")
		self.assertEqual(
			json.loads(response.get_data().decode(sys.getdefaultencoding()))['0']['gender'], 
			'male')
	
	def test_wrong_character(self):
		response = self.app.post('/api', data={'name':'sss'})
		self.assertEqual(response.status_code, 404)
		self.assertEqual(response.get_data().decode(sys.getdefaultencoding()), "404 Not found")
	
	def test_multi_characters(self):
		response = self.app.post('/api', data={'name':'Darth'})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content_type, "application/json")
		self.assertEqual(
			json.loads(response.get_data().decode(sys.getdefaultencoding()))['0']['gender'], 
			'male')

	def test_main_page(self):
		response = self.app.get('/', follow_redirects=True)
		self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
	unittest.main()


