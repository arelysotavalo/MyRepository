class Product:
    def __init__(self, id=None, name=None, price=0, quantity=0):
        if id is not None and id != "":
            self.id = int(id)
        else:
            self.id = 0

        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
