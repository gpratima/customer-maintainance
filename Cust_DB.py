import json

class CUSTOMER:

    def __init__(self):
        self.Customers = []

    def add_customer(self, cust_name, cust_type, state):
        new_customer = {}
        new_customer["Customer Name: "] = cust_name
        new_customer["Customer Type: "] = cust_type
        new_customer["State: "]= state
        self.Customers.append(new_customer)
        print("CUSTOMER: {0}".format(new_customer))
        return json.dumps(new_customer)

    def del_customer(self, cust_name):
        found = False
        for idx, Cust_DB in enumerate(self.Customers):
            if Cust_DB["cust_name"] == cust_name:
                index = idx
                found = True
                del self.Customers[idx]
        print("Customers: {0}".format(json.dumps(self.Customers)))
        return found

    def get_all_Customers(self):
        return self.Customers

    def json_list(self):
        return json.dumps(self.Customers)
