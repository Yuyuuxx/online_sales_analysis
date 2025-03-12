from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()

    manager.add_product(Product("Camera", 1500.77, 10))
    manager.add_product(Product("Microwave", 6000.55, 20))
    manager.add_product(Product("Pencils", 50.99, 69))
    manager.add_product(Product("Useless Contraption", 99999.99, 1))
   
    print("Available Products:")
    manager.show_products()

    total_value = manager.total_value()
    print(f"\nTotal Inventory Value: ${total_value}")