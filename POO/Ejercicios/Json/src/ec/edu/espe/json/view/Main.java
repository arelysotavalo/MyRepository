package ec.edu.espe.json.view;

import ec.edu.espe.json.controller.ProductController;
import ec.edu.espe.json.model.ProductModel;
import java.util.Scanner;

/**
 * Arelys Otavalo
 */
public class Main {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        ProductModel model = new ProductModel();
        ProductController controller = new ProductController(model);

        int option = 0;

        while (option != 5) {
            System.out.println("\n===== MENU CRUD PRODUCTOS =====");
            System.out.println("1. Agregar producto");
            System.out.println("2. Listar productos");
            System.out.println("3. Editar producto");
            System.out.println("4. Eliminar producto");
            System.out.println("5. Salir");
            System.out.print("Elige una opción: ");

            try {
                option = Integer.parseInt(input.nextLine());
            } catch (Exception e) {
                System.out.println("Error: ingrese un número válido.");
                continue;
            }

            switch (option) {

                case 1:
                    System.out.print("Nombre: ");
                    String name = input.nextLine();

                    float price = -1;
                    while (price <= 0) {
                        try {
                            System.out.print("Precio (solo números positivos): ");
                            price = Float.parseFloat(input.nextLine());

                            if (price <= 0) {
                                System.out.println("ERROR: el precio debe ser mayor que 0.");
                            }

                        } catch (Exception e) {
                            System.out.println("ERROR: ingrese un número válido.");
                            price = -1;
                        }
                    }

                    controller.create(name, price);
                    System.out.println("Producto agregado.");
                    break;

                case 2:
                    System.out.println("\n--- Lista de productos ---");
                    controller.list();
                    break;

                case 3:
                    System.out.print("ID a editar: ");
                    int editId = Integer.parseInt(input.nextLine());

                    System.out.print("Nuevo nombre: ");
                    String newName = input.nextLine();

                    float newPrice = -1;
                    while (newPrice <= 0) {
                        try {
                            System.out.print("Nuevo precio (positivo): ");
                            newPrice = Float.parseFloat(input.nextLine());

                            if (newPrice <= 0) {
                                System.out.println("ERROR: el precio debe ser mayor que 0.");
                            }

                        } catch (Exception e) {
                            System.out.println("ERROR: ingrese un número válido.");
                            newPrice = -1;
                        }
                    }

                    if (controller.update(editId, newName, newPrice)) {
                        System.out.println("Producto actualizado.");
                    } else {
                        System.out.println("Producto no encontrado.");
                    }
                    break;

                case 4:
                    System.out.print("ID a eliminar: ");
                    int deleteId = Integer.parseInt(input.nextLine());

                    if (controller.delete(deleteId)) {
                        System.out.println("Producto eliminado.");
                    } else {
                        System.out.println("Producto no encontrado.");
                    }
                    break;

                case 5:
                    System.out.println("Saliendo...");
                    break;

                default:
                    System.out.println("Opción inválida.");
            }
        }

        input.close();
    }
}
