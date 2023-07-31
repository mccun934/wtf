import unittest
from wtf import app

class TestApp(unittest.TestCase):

    def test_schema_query(self):
        with app.test_client() as client:
            response = client.get('/graphql?query={__schema{types{name}}}')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Organization', str(response.data))
            self.assertIn('User', str(response.data))
            self.assertIn('Project', str(response.data))

if __name__ == '__main__':
    unittest.main()
