class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
        
    def output_info(self):
        return f"Product name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def get_quantity(self):
        return self.quantity
    
    def add_quantity(self, amount):
        self.quantity += amount
        if self.quantity <= 0:
            print(f"Product cannot have a quantity equal or less than 0")