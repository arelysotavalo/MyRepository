package ec.edu.espe.json.model;

import java.util.ArrayList;

/**
 * Arelys
 */
public class ProductModel {

    private ArrayList<Product> products;
    private int autoId;

    public ProductModel() {
        products = new ArrayList<>();
        autoId = 1;
    }

    public ArrayList<Product> getAll() {
        return products;
    }

    public void addProduct(String name, float price) {
        Product p = new Product(autoId, name, price);
        products.add(p);
        autoId++;
    }

    public Product findById(int id) {
        for (Product p : products) {
            if (p.getId() == id) return p;
        }
        return null;
    }

    public boolean delete(int id) {
        Product p = findById(id);
        if (p != null) {
            products.remove(p);
            return true;
        }
        return false;
    }
}
