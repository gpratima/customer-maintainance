import tornado.web
from customers import CUSTOMERS
import json


class DelHandler(tornado.web.RequestHandler):
    def initialize(self,Customers):
        self.Customers = Customers
        
    def get(self):
        phone = self.get_argument('phone')
        result = self.Customers.del_phone(phone)
        if result:
            self.write("Deleted Customer phone: {0} successfully".format(phone))
            self.set_status(200)
        else:
            self.write("Customer '{0}' not found".format(phone))
            self.set_status(404)
