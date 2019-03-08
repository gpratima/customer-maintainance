import tornado.web
from customers import CUSTOMERS
import json


class AddHandler(tornado.web.RequestHandler):
    def initialize(self,customers):
        self.customers = customers
        
    def get(self):
        cust_name = self.get_argument('cust_name')
        cust_type = self.get_argument('cust_type')
        address=self.get_argument('address')
        phone=self.get_argument('phone')
        state=self.get_argument('state')
        
        result = self.Customers.add_customer(cust_name, cust_type, address, state, phone)
         self.write(result)
