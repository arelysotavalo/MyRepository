const fs = require("fs");
const path = require("path");

class ProductCrud {

    constructor() {
        this.filePath = path.join(__dirname, "../data/products.json");

        if (!fs.existsSync(this.filePath)) {
            const content = "[]";
            fs.writeFileSync(this.filePath, content, "utf8");
        }

        const fileData = fs.readFileSync(this.filePath, "utf8");
        this.products = JSON.parse(fileData);
    }

    saveToFile() {
        const content = JSON.stringify(this.products, null, 4);
        fs.writeFileSync(this.filePath, content, "utf8");
    }

    addProduct(product) {
        // ID ASSIGNMENT LOGIC
        let newId;

        if (this.products.length === 0) {
            newId = 1;
        } else {
            const lastProduct = this.products[this.products.length - 1];
            newId = lastProduct.id + 1;
        }

        product.id = newId;

        this.products.push(product);
        this.saveToFile();
    }

    getAllProducts() {
        return this.products;
    }

    updateProduct(id, updatedProduct) {

        for (let i = 0; i < this.products.length; i++) {
            if (this.products[i].id === id) {

                updatedProduct.id = id;
                this.products[i] = updatedProduct;

                this.saveToFile();
                return true;
            }
        }
        return false;
    }

    deleteProduct(id) {

        for (let i = 0; i < this.products.length; i++) {
            if (this.products[i].id === id) {

                this.products.splice(i, 1);
                this.saveToFile();
                return true;
            }
        }
        return false;
    }
}

module.exports = ProductCrud;
