class Product:
    auto_id = 1

    def __init__(self, name, price, quantity):
        self.id = Product.auto_id
        Product.auto_id += 1

        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }