from product import Product
from product_manager import ProductManager
from cart import Cart
import random

def main():
    manager = ProductManager()

    manager.add_product(Product("Camera", 1500.77, 15))
    manager.add_product(Product("Microwave", 6000.55, 25))
    manager.add_product(Product("Pencils", 50.99, 74))
    manager.add_product(Product("Useless Contraption", 99999.99, 2))
    # print("Available Products:")
    # manager.show_products()

    # total_value = manager.total_value()
    # print(f"\nTotal Inventory Value: ${total_value}")

    cart = Cart()
    
    products = manager.products
    for _ in range(3):
        product = random.choice(products)
        max_quantity = min(product.quantity, 3)
        if max_quantity > 0:
            quantity = random.randint(1, max_quantity)
            cart.add_to_cart(product, quantity)

    print("\nCart Contents")
    cart.display_cart()

    cart_total = cart.calculate_total()
    print(f"\nTotal Cart Value: ${cart_total:.2f}")

if __name__ == "__main__":
    main()