class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        self.items.remove(product)

    def total_price(self):
        return sum(item.price for item in self.items)

class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

def display_products(products):
    print("Available Products:")
    for i, product in enumerate(products, 1):
        print(f"{i}. {product.name} - ${product.price}")

def main():
    # Create some sample products
    products = [Product("Product A", 10), Product("Product B", 15), Product("Product C", 20)]

    # Create a user
    user = User("John Doe")

    # Display available products
    display_products(products)

    while True:
        choice = input("\nEnter the product number to add to cart (q to quit): ")
        if choice == 'q':
            break
        elif choice.isnumeric() and 1 <= int(choice) <= len(products):
            product = products[int(choice) - 1]
            user.cart.add_item(product)
            print(f"{product.name} added to cart.")
        else:
            print("Invalid choice. Please try again.")

    # Display cart contents and total price
    print(f"\nItems in {user.name}'s Cart:")
    for item in user.cart.items:
        print(f"{item.name} - ${item.price}")
    print(f"Total Price: ${user.cart.total_price()}")

if __name__ == '__main__':
    main()
