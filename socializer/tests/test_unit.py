import unittest

from application import create_app


class AppTestCase(unittest.TestCase):

    def setUp(self) -> None:
        app = create_app()
        app.config["TESTING"] = True
        self.app = app
        # Further DB initialisation

    def tearDown(self) -> None:
        pass

    def test_app_configuration(self):
        self.assertTrue(self.app.config["TESTING"])

if __name__ == "__main__":
    unittest.main()
