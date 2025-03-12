from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()

    manager.add_product(Product("Camera", 1500.77, 15))
    manager.add_product(Product("Microwave", 6000.55, 25))
    manager.add_product(Product("Pencils", 50.99, 74))
    manager.add_product(Product("Useless Contraption", 99999.99, 2))