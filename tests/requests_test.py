import unittest, requests, json, sys

class TestServerApiUsingRequests(unittest.TestCase):
	'''
	Testing the application with requests while it's running
	'''
	
	def test_connection(self):
		response = requests.get('http://localhost:5001/api')
		self.assertEquals(response.text, "{}")

	def test_search(self):
		response = requests.post("http://localhost:5001/api", 
		data={'name':'Luke Skywalker'})
		self.assertEqual(response.json()['0']['gender'], 'male')

if __name__ == "__main__":
	unittest.main()
