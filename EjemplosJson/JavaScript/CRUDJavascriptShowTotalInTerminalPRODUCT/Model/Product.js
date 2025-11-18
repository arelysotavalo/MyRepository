class Product {
    constructor(id, name, price, quantity) {

    if (id !== undefined && id !== null && id !== "") {
        this.id = Number(id);
    } else {
        this.id = 0;
    }

        this.name = name;
        this.price = Number(price);
        this.quantity = Number(quantity);
    }
}

module.exports = Product;
