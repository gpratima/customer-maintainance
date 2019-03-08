import tornado.web
from customer import customers
import json


class GetHandler(tornado.web.RequestHandler):
    def initialize(self, customers):
        self.customer = CUSTOMER
        
    def get(self):
        self.write(self.customer.json_list())
