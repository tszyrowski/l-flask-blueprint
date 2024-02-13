from application import create_app
import unittest

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app(config='settings')
        app.config['TESTING'] = True
        self.app = app

    def tearDown(self):
        pass

    def test_app_configuration(self):
        self.assertTrue(self.app.config['TESTING'])

    # def test_home_status_code(self):
    #     result = self.client.get('/')
    #     self.assertEqual(result.status_code, 200)

    # def test_home_data(self):
    #     result = self.client.get('/')
    #     self.assertEqual(result.data, b'Hello, World!')

