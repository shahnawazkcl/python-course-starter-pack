
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)


# Usage example
product1 = Product("Book", 10.99)
product2 = Product("Pen", 0.99)

customer = Customer("John Doe")

customer.add_to_cart(product1)
customer.add_to_cart(product2)

print([product.name for product in customer.cart])  # Should print: ['Book', 'Pen']
