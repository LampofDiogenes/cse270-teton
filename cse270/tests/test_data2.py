import unittest
import requests

class IntegrationTest(unittest.TestCase):
    def test_endpoint_response(self):
        url = 'http://127.0.0.1:8000/users/?username=admin&password=admin'
        
        response = requests.get(url)
        
        # Verify HTTP code 401
        self.assertEqual(response.status_code, 401)
        
        # Verify empty response
        self.assertFalse(response.text.strip())

if __name__ == '__main__':
    unittest.main()

