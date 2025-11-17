package ec.edu.espe.json.controller;

import ec.edu.espe.json.model.Product;
import ec.edu.espe.json.model.ProductModel;

/**
 * Arelys Otavalo
 */
public class ProductController {

    private ProductModel model;

    public ProductController(ProductModel model) {
        this.model = model;
    }

    public void create(String name, float price) {
        model.addProduct(name, price);
    }

    public void list() {
        for (Product p : model.getAll()) {
            System.out.println(p);
        }
    }

    public Product search(int id) {
        return model.findById(id);
    }

    public boolean update(int id, String newName, float newPrice) {
        Product p = model.findById(id);
        if (p != null) {
            p.setName(newName);
            p.setPrice(newPrice);
            return true;
        }
        return false;
    }

    public boolean delete(int id) {
        return model.delete(id);
    }
}
