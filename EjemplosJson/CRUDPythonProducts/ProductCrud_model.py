import json
import os

class ProductCrud:
    def __init__(self):
        # The direction of json
        self.file_path = os.path.join(os.path.dirname(__file__), "../data/products.json")

        # Create json if it does not exist
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump([], file)

        #Upload exist products
        with open(self.file_path, "r", encoding="utf-8") as file:
            self.products = json.load(file)

    def save_to_file(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.products, file, indent=4)

    def add_product(self, product):
        #ID assignment
        if len(self.products) == 0:
            new_id = 1
        else:
            last_product = self.products[-1]
            new_id = last_product["id"] + 1

        product.id = new_id
        self.products.append(product.__dict__)
        self.save_to_file()

    def get_all_products(self):
        return self.products

    def update_product(self, id, updated_product):
        for i, prod in enumerate(self.products):
            if prod["id"] == id:
                updated_product.id = id
                self.products[i] = updated_product.__dict__
                self.save_to_file()
                return True
        return False

    def delete_product(self, id):
        for i, prod in enumerate(self.products):
            if prod["id"] == id:
                self.products.pop(i)
                self.save_to_file()
                return True
        return False
