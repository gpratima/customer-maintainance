import tornado.web
from customers import customer
import json


class AddHandler(tornado.web.RequestHandler):
    def initialize(self,customer):
        self.customer =customer
        
    def get(self):
        cust_name = self.get_argument('cust_name')
        cust_type = self.get_argument('cust_type')
        address=self.get_argument('address')
        phone=self.get_argument('phone')
        state=self.get_argument('state')
        
        result = self.customer.add_customer(cust_name,cust_type,address,phone,state)
        self.write(result)
