import tornado.web
from Cust_DB import CUSTOMER
import json


class GetHandler(tornado.web.RequestHandler):
    def initialize(self, CUSTOMER):
        self.CUSTOMER = CUSTOMER
        
    def get(self):
        self.write(self.customer.json_list())
