#coding:utf-8
from main import make_app
from tornado.testing import AsyncHTTPTestCase

import unittest
import json
import tornado
import logging
logging.basicConfig(level=logging.DEBUG)

class ApiTestCase(AsyncHTTPTestCase):
    def get_app(self):
        self.app = make_app()
        return self.app

    def test_status(self):
        urls = [
                '/', 
            ]
        for url in urls:
            response = self.fetch(url)
            self.assertEqual(response.code, 200)

    def test_notfount(self):
        response = self.fetch('/notfound/')
        self.assertEqual(response.code, 404)

    @tornado.testing.gen_test
    def test_websocket(self):
        ws_url = "ws://localhost:" + str(self.get_http_port()) + "/echo"
        ws_client = yield tornado.websocket.websocket_connect(ws_url)
        ws_client.write_message(json.dumps({"message": "ping"}))
        response = yield ws_client.read_message()
        self.assertEqual(response, u'{"message": "pong"}')

if __name__ == '__main__':
    unittest.main()
