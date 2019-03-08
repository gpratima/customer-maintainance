import json

class customers:

    def __init__(self):
        self.customer = []

    def add_customer(self, cust_name, cust_type, address, state, phone):
        new_customer = {}
        new_customer["Customer Name: "] = cust_name
        new_customer["Customer Type: "] = cust_type
        new_customer["Addres: "]= address
        new_customer["State: "]= state
        new_customer["Phone: "]= phone
        self.Customer.append(new_customer)
        print("Customer: {0}".format(new_customer))
        return json.dumps(new_customer)

    def del_customer(self, phone):
        found = False
        for idx, customer in enumerate(self.customer):
            if customer["Phone"] == phone:
                index = idx
                found = True
                del self.customer[idx]
        print("customer: {0}".format(json.dumps(self.customer)))
        return found

    def get_all_customer(self):
        return self.customer

    def json_list(self):
        return json.dumps(self.customer)
