const readline = require("readline");
const ProductController = require("../Controller/ProductController");
const Product = require("../Model/Product");

const reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const controller = new ProductController();

function menu() {
    console.log("\n===== PRODUCT MENU =====");
    console.log("1. Show all products");
    console.log("2. Add new product");
    console.log("3. Update product");
    console.log("4. Delete product");
    console.log("5. Exit");
    console.log("6. Show total price");

    reader.question("Choose an option: ", (option) => {
        switch (option) {

            case "1":
                console.log("\n--- Product List ---");
                console.log(controller.getAll());
                menu();
                break;

            case "2":
                reader.question("Name: ", (name) => {

                    function askPrice() {
                        reader.question("Price (positive number): ", (priceInput) => {
                            const price = parseFloat(priceInput);
                            if (isNaN(price) || price <= 0) {
                                console.log("Invalid price. Please enter a positive number.");
                                askPrice(); // REPEAT UNTIL VALID
                            } else {
                                askQuantity(price);
                            }
                        });
                    }

                    function askQuantity(validPrice) {
                        reader.question("Quantity (positive number): ", (quantityInput) => {
                            const quantity = parseInt(quantityInput);
                            if (isNaN(quantity) || quantity <= 0) {
                                console.log("Invalid quantity. Please enter a positive number.");
                                askQuantity(validPrice); // REPEAT UNTIL VALID
                            } else {
                                const product = new Product(0, name, validPrice, quantity);
                                controller.add(product);
                                console.log("The product was added successfully.");
                                menu();
                            }
                        });
                    }

                    askPrice(); // QUESTION NEW PRICE
                });
                break;

            case "3":
                reader.question("Enter the ID of the product you want to update: ", (id) => {
                    reader.question("New Name: ", (name) => {

                        function askNewPrice() {
                            reader.question("New Price (positive number): ", (priceInput) => {
                                const price = parseFloat(priceInput);
                                if (isNaN(price) || price <= 0) {
                                    console.log("Invalid price. Please enter a positive number.");
                                    askNewPrice();
                                } else {
                                    askNewQuantity(price);
                                }
                            });
                        }

                        function askNewQuantity(validPrice) {
                            reader.question("New Quantity (positive number): ", (quantityInput) => {
                                const quantity = parseInt(quantityInput);
                                if (isNaN(quantity) || quantity <= 0) {
                                    console.log("Invalid quantity. Please enter a positive number.");
                                    askNewQuantity(validPrice);
                                } else {
                                    const updated = controller.update(
                                        Number(id),
                                        new Product(0, name, validPrice, quantity)
                                    );

                                    if (updated) {
                                        console.log("The product was updated successfully.");
                                    } else {
                                        console.log("A product with the specified ID was not found.");
                                    }

                                    menu();
                                }
                            });
                        }

                        askNewPrice(); // QUESTION NEW PRICE
                    });
                });
                break;

            case "4":
                reader.question("Enter the ID of the product you want to delete: ", (id) => {
                    const deleted = controller.delete(Number(id));

                    if (deleted) {
                        console.log("The product was deleted successfully.");
                    } else {
                        console.log("A product with the specified ID was not found.");
                    }

                    menu();
                });
                break;

            case "5":
                console.log("Goodbye!");
                reader.close();
                break;

            case "6":
                console.log("Total price = " + controller.calculateTotal());
                menu();
                break;

            default:
                console.log("Invalid option. Please select a valid option from the menu.");
                menu();
        }
    });
}

menu();
