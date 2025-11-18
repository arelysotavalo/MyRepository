# product_manager.py

import json
import os
from product_model import Product

class ProductManager:
    def __init__(self, filename="products.json"):
        self.filename = filename
        self.products = []
        self.load_data()

    # ---------------------
    # UTILIDAD
    # ---------------------
    def get_product_by_id(self, product_id):
        for p in self.products:
            if p.id == product_id:
                return p
        return None

    # ---------------------
    # CRUD
    # ---------------------
    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)
        self.save_data()
        return product

    def list_products(self):
        return self.products

    def delete_product(self, product_id):
        product = self.get_product_by_id(product_id)
        if product:
            self.products.remove(product)
            self.save_data()
            return True
        return False

    def update_product(self, product_id, new_name, new_price, new_quantity):
        product = self.get_product_by_id(product_id)
        if product:
            product.name = new_name
            product.price = new_price
            product.quantity = new_quantity
            self.save_data()
            return True
        return False

    # ---------------------
    # JSON
    # ---------------------
    def save_data(self):
        data = [p.to_dict() for p in self.products]
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)

                    for item in data:
                        product = Product(item["name"], item["price"], item["quantity"])
                        product.id = item["id"]
                        self.products.append(product)

                    if self.products:
                        Product.auto_id = max(p.id for p in self.products) + 1

            except json.JSONDecodeError:
                self.products = []
