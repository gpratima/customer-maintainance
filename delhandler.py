import tornado.web
from Cust_DB import CUSTOMER
import json


class DelHandler(tornado.web.RequestHandler):
    def initialize(self,Customers):
        self.Customers = Customers
        
    def get(self):
        cust_name = self.get_argument('cust_name')
        result = self.Customers.del_customer(cust_name)
        if result:
            self.write("Deleted Customer phone: {0} successfully".format(cust_name))
            self.set_status(200)
        else:
            self.write("Customer '{0}' not found".format(cust_name))
            self.set_status(404)
