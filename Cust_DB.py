import json

class CUSTOMER:

    def __init__(self):
        self.Customers = []

    def add_customer(self, cust_name, cust_type, address, state, phone):
        new_customer = {}
        new_customer["Customer Name: "] = cust_name
        new_customer["Customer Type: "] = cust_type
        new_customer["Addres: "]= address
        new_customer["State: "]= state
        new_customer["Phone: "]= phone
        self.Customers.append(new_customer)
        print("Customer: {0}".format(new_customer))
        return json.dumps(new_customer)

    def del_customer(self, phone):
        found = False
        for idx, customers in enumerate(self.Customers):
            if customer["Phone"] == phone:
                index = idx
                found = True
                del self.Customers[idx]
        print("Customers: {0}".format(json.dumps(self.Customers)))
        return found

    def get_all_customer(self):
        return self.Customers

    def json_list(self):
        return json.dumps(self.Customers)
