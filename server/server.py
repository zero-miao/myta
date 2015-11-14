#encoding:utf-8


import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.httpserver
import json

class MytaHandler(tornado.websocket.WebSocketHandler):
	def check_origin(self, origin):
		return True

	def open(self,params):
		print 'WebSocket open'
		print 'client:',params
		self.write_message(json.dumps('hello,world'))
		
	def on_message(self,message):
		pass

	def on_close(self):
		print 'WebSocket close'

application = tornado.web.Application([
    (r"/(.*)", MytaHandler),
])

#页面之间的跳转，服务器并不考虑，针对对应的页面，由客户端发送对应的url请求即可

if __name__ == "__main__":
   	http_server = tornado.httpserver.HTTPServer(application)
 	http_server.listen(80)
   	tornado.ioloop.IOLoop.instance().start()


