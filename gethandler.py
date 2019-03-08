import tornado.web
from customers import customers
import json


class GetHandler(tornado.web.RequestHandler):
    def initialize(self, CUSTOMER):
        self.CUSTOMER = CUSTOMER
        
    def get(self):
        self.write(self.customer.json_list())
