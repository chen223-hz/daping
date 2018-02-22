#coding:utf-8

import traceback

class WebsocketBridge(object):
    clients = []

    def subscribe(self, client):
        WebsocketBridge.clients.append(client)

    def unsubscribe(self, client):
        WebsocketBridge.clients.remove(client)

    def broadcast(self, message):
        cls = WebsocketBridge
        for client in cls.clients:
            try:
                client.write_message(message)
            except:
                traceback.print_exc()
