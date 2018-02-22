#coding:utf-8
import os.path
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.gen
import traceback
import json
from tornado.httpclient import AsyncHTTPClient
from bridge import WebsocketBridge
from mqtt import MQTTClient
from settings import *
from echarts import target_url, parse_echarts

tornado.httpclient.AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient",
    defaults=dict(
        user_agent="tornadoUserAgent"
     ), 
    max_clients=10,
)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class EchoHandler(tornado.websocket.WebSocketHandler, WebsocketBridge):
    def open(self):
        self.subscribe(self)

    def check_origin(self, origin): 
        return True

    def on_message(self, message):
        if json.loads(message).get('message') == 'ping':
            self.write_message(json.dumps({ "message": "pong" }))
        # print message 

    def on_close(self):
        self.unsubscribe(self)

class JSONHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, target):
        data = {}
        data['pk'] = 13
        data['date'] = self.request.arguments
        url = target_url(target)
        req= tornado.httpclient.HTTPRequest(url=url, method='POST', body=json.dumps(data), \
		 connect_timeout=200, request_timeout=600)
        client = tornado.httpclient.AsyncHTTPClient()
        response = None
        try:
            #response = yield client.fetch(req)
            pass
        except:
            traceback.print_exc()
        self.on_response(response, target)

    def on_response(self,response,target):
        data = {}
        if response and response.body:
            body = json.loads(response.body)
            data = parse_echarts(target, body)
        self.finish(data)


def make_app():
    return tornado.web.Application([
            (r"/", MainHandler),
            (r"/echo", EchoHandler),
            (r"/json/(.*)", JSONHandler),
        ],
       cookie_secret=SECRET, \
        login_url="/login", \
        template_path=os.path.join(os.path.dirname(__file__), "templates"), \
        static_path=os.path.join(os.path.dirname(__file__), "static"), \
        xsrf_cookies=True, \
        debug=DEBUG, \
    )

if __name__ == "__main__":
    mqtt = MQTTClient(MQTT_HOST, MQTT_PORT, MQTT_USER, MQTT_PASS, MQTT_TOPIC)
    app = make_app()
    app.listen(PORT)
    print 'webserver listen port: ', PORT
    tornado.ioloop.IOLoop.current().start()
