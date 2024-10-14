class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        self.items.remove(product)

    def total_price(self):
        return sum(item.price for item in self.items)

class Recommender:
    def __init__(self, products):
        self.products = products

    def recommend_products(self):
        # Dummy recommendation logic - simply suggest first 2 products
        return self.products[:2]

def main():
    # Sample products
    products = [
        Product(1, "Laptop", 1000),
        Product(2, "Smartphone", 800),
        Product(3, "Headphones", 100),
        Product(4, "Tablet", 500)
    ]

    cart = ShoppingCart()
    recommender = Recommender(products)

    while True:
        print("Available Products:")
        for product in products:
            print(f"{product.id}. {product.name} - ${product.price}")

        choice = input("Enter product ID to add to cart (or 'r' to see recommendations, 'c' to view cart, 'q' to quit): ")

        if choice == 'q':
            break
        elif choice == 'r':
            recommended_products = recommender.recommend_products()
            print("Recommended Products:")
            for product in recommended_products:
                print(f"{product.name} - ${product.price}")
        elif choice == 'c':
            print("Shopping Cart:")
            for item in cart.items:
                print(f"{item.name} - ${item.price}")
            print(f"Total Price: ${cart.total_price()}")
        else:
            product_id = int(choice)
            selected_product = next((product for product in products if product.id == product_id), None)
            if selected_product:
                cart.add_item(selected_product)
                print(f"{selected_product.name} added to cart.")
            else:
                print("Invalid product ID. Please try again.")

if __name__ == "__main__":
    main()
