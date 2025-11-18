const readline = require("readline");
const EmployeeController = require("../Controller/EmployeeController");

const reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const controller = new EmployeeController();

function menu() {
    console.log("\n===== EMPLOYEE MENU =====");
    console.log("1. Show all employees");
    console.log("2. Add new employee");
    console.log("3. Edit employee");
    console.log("4. Delete employee");
    console.log("5. Exit");

    reader.question("Choose an option: ", (option) => {

        switch(option) {

            case "1":
                console.log("\n--- EMPLOYEE LIST ---");
                console.log(controller.getAll());
                menu();
                break;

            case "2":
                reader.question("Employee name: ", (name) => {
                    reader.question("Hours worked: ", (hours) => {

                        const employee = controller.add(name, hours);

                        console.log("\nEmployee added successfully!");
                        console.log(employee);

                        menu();
                    });
                });
                break;

            case "3":
                reader.question("Enter employee ID to edit: ", (idInput) => {
                    const id = Number(idInput);
                    reader.question("New name: ", (name) => {
                        reader.question("New hours worked: ", (hours) => {

                            const success = controller.edit(id, name, hours);

                            if(success) {
                                console.log("\nEmployee updated successfully!");
                            } else {
                                console.log("\nEmployee not found.");
                            }

                            menu();
                        });
                    });
                });
                break;

            case "4":
                reader.question("Enter employee ID to delete: ", (idInput) => {
                    const id = Number(idInput);

                    const success = controller.delete(id);

                    if(success) {
                        console.log("\nEmployee deleted successfully!");
                    } else {
                        console.log("\nEmployee not found.");
                    }

                    menu();
                });
                break;

            case "5":
                console.log("Goodbye!");
                reader.close();
                break;

            default:
                console.log("Invalid option");
                menu();
        }
    });
}

menu();

