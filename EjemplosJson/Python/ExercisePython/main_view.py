# main_view.py

from product_manager import ProductManager

class ProductView:
    def __init__(self):
        self.manager = ProductManager()

    # ================================
    # VALIDACIONES
    # ================================
    def input_float(self, message):
        while True:
            value = input(message)
            try:
                return float(value)
            except ValueError:
                print("Error: Debe ingresar un número válido (decimal permitido).")

    def input_int(self, message):
        while True:
            value = input(message)
            try:
                return int(float(value))   # flotante → entero
            except ValueError:
                print("Error: Debe ingresar un número entero.")

    def input_string(self, message):
        while True:
            value = input(message).strip()
            if value:
                return value
            print("Error: no puede estar vacío.")

    # ================================
    # MENÚ
    # ================================
    def menu(self):
        while True:
            print("\n====== MENÚ DE PRODUCTOS ======")
            print("1. Agregar producto")
            print("2. Listar productos")
            print("3. Eliminar producto")
            print("4. Modificar producto")
            print("5. Salir")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.add_product()
            elif opcion == "2":
                self.list_products()
            elif opcion == "3":
                self.delete_product()
            elif opcion == "4":
                self.update_product()
            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida, intenta otra vez.")

    # ================================
    # CRUD desde la vista
    # ================================
    def add_product(self):
        print("\n--- AGREGAR PRODUCTO ---")
        nombre = self.input_string("Nombre: ")
        precio = self.input_float("Precio: ")
        cantidad = self.input_int("Cantidad: ")

        producto = self.manager.add_product(nombre, precio, cantidad)
        print(f"Producto agregado con ID: {producto.id}")

    def list_products(self):
        productos = self.manager.list_products()
        if not productos:
            print("No hay productos.")
            return

        print("\n--- LISTA DE PRODUCTOS ---")
        for p in productos:
            print(f"ID: {p.id} | Nombre: {p.name} | Precio: {p.price} | Cantidad: {p.quantity}")

    def delete_product(self):
        print("\n--- ELIMINAR PRODUCTO ---")
        product_id = self.input_int("ID a eliminar: ")

        if self.manager.delete_product(product_id):
            print("Producto eliminado.")
        else:
            print("ID no encontrado.")

    def update_product(self):
        print("\n--- MODIFICAR PRODUCTO ---")
        product_id = self.input_int("ID del producto: ")

        nombre = self.input_string("Nuevo nombre: ")
        precio = self.input_float("Nuevo precio: ")
        cantidad = self.input_int("Nueva cantidad: ")

        if self.manager.update_product(product_id, nombre, precio, cantidad):
            print("Producto actualizado.")
        else:
            print("ID no encontrado.")


if __name__ == "__main__":
    ProductView().menu()
