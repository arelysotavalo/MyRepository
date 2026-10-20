from ProductCrud_model import ProductCrud

class ProductController:
    def __init__(self):
        self.crud = ProductCrud()

    def add(self, product):
        self.crud.add_product(product)

    def get_all(self):
        return self.crud.get_all_products()

    def update(self, id, product):
        return self.crud.update_product(id, product)

    def delete(self, id):
        return self.crud.delete_product(id)

    def calculate_total(self):
        products = self.crud.get_all_products()
        total = 0

        for product in products:
            total += product["price"] * product["quantity"]

        return total
