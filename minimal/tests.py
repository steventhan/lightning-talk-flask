#!/usr/bin/env python
from app import app
import unittest


class AppTestCase(unittest.TestCase):
    """Sample test case"""

    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_home(self):
        """Test home page."""
        response = self.client.get('/')
        self.assertTrue(b'Hello Codefellows!' in response.data)


if __name__ == '__main__':
    unittest.main()
