from product import Product

class ProductManager:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        if not self.products:
            print("No products available")
        else:
            for product in self.products:
                print(product.output_info())
    
    def total_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        return total_value
    
    def remove_product(self):
        product_name = input("Enter the name of the product you want to remove.\n")
        for product in self.products:
            if product_name == product.name:
                self.products.remove(product)
                return f"Product {product_name} has been removed."
        
        return(f"Product {product_name} does not exist.")