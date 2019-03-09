import tornado.web
from Cust_DB import CUSTOMER
import json


class AddHandler(tornado.web.RequestHandler):
    def initialize(self,Customers):
        self.Customers = Customers
        
    def get(self):
        cust_name = self.get_argument('cust_name')
        cust_type = self.get_argument('cust_type')
        state=self.get_argument('state')        
        result = self.Customers.add_customer(cust_name, cust_type, state)
        self.write(result)
