import tornado.ioloop
import tornado.web
from CUSTOMER import customers
from addhandler import AddHandler
from delhandler import DelHandler
from gethandler import GetHandler

customer = customers()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Customer Maintainance VERSION 1")

def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/addcust", AddHandler, dict(customer = customer)),
        (r"/v1/delcust", DelHandler, dict(customer = customer)),
        (r"/v1/getcust", GetHandler, dict(customer = customer)),
        ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


#http://localhost:8888/v1/addbook?title="The design of everyday things"&author="Don Norman"
#http://localhost:8888/v1/addbook?title="The Billion Dollars"&author="Richie Rich"
#http://localhost:8888/v1/getbooks
#http://yourserver:8888/v1/delbook?title="The book of errors"
#http://yourserver:8888/v1/delbook?title="The Billion Dollars"
