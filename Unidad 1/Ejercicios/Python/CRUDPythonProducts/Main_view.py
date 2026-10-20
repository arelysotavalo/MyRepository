from Product_controller import ProductController
from Product_model import Product

controller = ProductController()

def menu():
    print("\n===== PRODUCT MENU =====")
    print("1. Show all products")
    print("2. Add new product")
    print("3. Update product")
    print("4. Delete product")
    print("5. Exit")
    print("6. Show total price")

    option = input("Choose an option: ")

    if option == "1":
        print("\n--- Product List ---")
        print(controller.get_all())
        menu()

    elif option == "2":
        name = input("Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        product = Product(0, name, price, quantity)
        controller.add(product)

        print("The product was added successfully.")
        menu()

    elif option == "3":
        id = int(input("Enter the ID of the product you want to update: "))
        name = input("New Name: ")
        price = float(input("New Price: "))
        quantity = int(input("New Quantity: "))

        updated = controller.update(id, Product(0, name, price, quantity))

        if updated:
            print("The product was updated successfully.")
        else:
            print("A product with the specified ID was not found.")
        menu()

    elif option == "4":
        id = int(input("Enter the ID of the product you want to delete: "))
        deleted = controller.delete(id)

        if deleted:
            print("The product was deleted successfully.")
        else:
            print("A product with the specified ID was not found.")
        menu()

    elif option == "5":
        print("Goodbye!")
        exit()

    elif option == "6":
        print("Total price = ", controller.calculate_total())
        menu()

    else:
        print("Invalid option. Please select a valid option from the menu.")
        menu()

if __name__ == "__main__":
    menu()





"""
from Product_controller import ProductController
from Product_model import Product

controller = ProductController()

def menu():
    print("\n===== PRODUCT MENU =====")
    print("1. Show all products")
    print("2. Add new product")
    print("3. Update product")
    print("4. Delete product")
    print("5. Exit")
    print("6. Show total price")

    option = input("Choose an option: ")

    if option == "1":
        # Mostrar todos los productos
        print("\n--- Product List ---")
        print(controller.get_all())
        menu()

    elif option == "2":
        # Agregar nuevo producto
        name = input("Name: ")

        # Validar que el precio sea positivo
        while True:
            price = float(input("Price (must be 0 or higher): "))
            if price >= 0:
                break
            print("Price must be zero or positive. Try again.")

        # Validar que la cantidad sea positiva
        while True:
            quantity = int(input("Quantity (must be 0 or higher): "))
            if quantity >= 0:
                break
            print("Quantity must be zero or positive. Try again.")

        product = Product(0, name, price, quantity)
        controller.add(product)

        print("The product was added successfully.")
        menu()

    elif option == "3":
        # Actualizar producto
        id = int(input("Enter the ID of the product you want to update: "))
        name = input("New Name: ")

        # Validar que el nuevo precio sea positivo
        while True:
            price = float(input("New Price (must be 0 or higher): "))
            if price >= 0:
                break
            print("Price must be zero or positive. Try again.")

        # Validar que la nueva cantidad sea positiva
        while True:
            quantity = int(input("New Quantity (must be 0 or higher): "))
            if quantity >= 0:
                break
            print("Quantity must be zero or positive. Try again.")

        updated = controller.update(id, Product(0, name, price, quantity))

        if updated:
            print("The product was updated successfully.")
        else:
            print("A product with the specified ID was not found.")
        menu()

    elif option == "4":
        # Eliminar producto
        id = int(input("Enter the ID of the product you want to delete: "))
        deleted = controller.delete(id)

        if deleted:
            print("The product was deleted successfully.")
        else:
            print("A product with the specified ID was not found.")
        menu()

    elif option == "5":
        # Salir
        print("Goodbye!")
        exit()

    elif option == "6":
        # Mostrar total de la bodega
        print("Total price = ", controller.calculate_total())
        menu()

    else:
        # Opción inválida
        print("Invalid option. Please select a valid option from the menu.")
        menu()

if __name__ == "__main__":
    menu()
"""
