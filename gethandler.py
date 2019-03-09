import tornado.web
from Cust_DB import CUSTOMER
import json


class GetHandler(tornado.web.RequestHandler):
    def initialize(self, Customers):
        self.Customers = Customers
        
    def get(self):
        self.write(self.Customers.json_list())
