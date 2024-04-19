class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product_info(self):
        print(f"Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}")

    def calculate_cost(self):
        return self.price * self.quantity


class Electronics(Product):
    def __init__(self, name, price, quantity, brand):
        super().__init__(name, price, quantity)
        self.brand = brand

    def display_product_info(self):
        super().display_product_info()
        print(f"Brand: {self.brand}")