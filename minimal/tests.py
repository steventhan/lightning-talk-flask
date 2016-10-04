#!/usr/bin/env python
import app
import unittest
from flask import url_for


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.app.test_client()

    def tearDown(self):
        pass

    def test_home(self):
        response = self.client.get('/')
        import pdb; pdb.set_trace()
        self.assertTrue(b'Hello Codefellows!' in response.data)


if __name__ == '__main__':
    unittest.main()
