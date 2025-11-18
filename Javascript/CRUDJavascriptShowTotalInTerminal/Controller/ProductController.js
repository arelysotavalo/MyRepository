const ProductCrud = require("../Model/ProductCrud");

class ProductController {

    constructor() {
        this.crud = new ProductCrud();
    }

    add(product) {
        this.crud.addProduct(product);
    }

    getAll() {
        return this.crud.getAllProducts();
    }

    update(id, product) {
        return this.crud.updateProduct(id, product);
    }

    delete(id) {
        return this.crud.deleteProduct(id);
    }

    calculateTotal() {
        const products = this.crud.getAllProducts();
        let total = 0;

        for (let i = 0; i < products.length; i++) {
            total += products[i].price * products[i].quantity;
        }

        return total;
    }
}

module.exports = ProductController;
