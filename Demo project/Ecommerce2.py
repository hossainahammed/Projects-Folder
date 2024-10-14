import tkinter as tk

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, index):
        del self.items[index]

    def total_price(self):
        return sum(item.price for item in self.items)

class Recommender:
    def __init__(self, products):
        self.products = products

    def recommend_products(self, cart_items):
        cart_product_names = [item.name for item in cart_items]
        recommended_products = []

        for product in self.products:
            if product.name not in cart_product_names:
                recommended_products.append(product)

        return recommended_products[:2]

def add_to_cart(product):
    cart.add_item(product)
    update_cart_and_recommendations()

def remove_from_cart(index):
    cart.remove_item(index)
    update_cart_and_recommendations()

def update_cart_and_recommendations():
    update_cart()
    update_recommendations()

def update_cart():
    cart_contents.delete(1.0, tk.END)
    for index, item in enumerate(cart.items, start=1):
        product_label = tk.Label(cart_contents, text=f"{index}. {item.name} - ${item.price}")
        cart_contents.window_create(tk.END, window=product_label)
        remove_button = tk.Button(cart_contents, text="Remove", command=lambda i=index - 1: remove_from_cart(i))
        cart_contents.window_create(tk.END, window=remove_button)
        cart_contents.insert(tk.END, '\n')

    cart_contents.insert(tk.END, "-" * 40 + "\n")
    cart_contents.insert(tk.END, f"\nTotal Price: ${cart.total_price()}", 'bold')
    cart_contents.tag_configure('bold', font=('Arial', 12, 'bold'))

    cart_contents.see(tk.END)

def update_recommendations():
    recommended_products = recommender.recommend_products(cart.items)
    recommendations.delete(1.0, tk.END)
    for product in recommended_products:
        recommendations.insert(tk.END, f"{product.name} - ${product.price}\n")

products = [
    Product("Laptop", 1000),
    Product("Smartphone", 800),
    Product("Headphones", 100),
    Product("Tablet", 500)
]

cart = ShoppingCart()
recommender = Recommender(products)

root = tk.Tk()
root.title("Simple E-commerce App")

# Center the window on the screen
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

product_frame = tk.Frame(root)
product_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

product_label = tk.Label(product_frame, text="Available Products")
product_label.pack()

for product in products:
    button = tk.Button(product_frame, text=f"{product.name} - ${product.price}", command=lambda p=product: add_to_cart(p))
    button.pack(pady=5)

cart_frame = tk.Frame(root)
cart_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

cart_label = tk.Label(cart_frame, text="Shopping Cart")
cart_label.pack()

cart_contents = tk.Text(cart_frame, width=40, height=10)
cart_contents.pack(fill=tk.BOTH, expand=True)

recommendations_frame = tk.Frame(root)
recommendations_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

recommendations_label = tk.Label(recommendations_frame, text="Recommended Products")
recommendations_label.pack()

recommendations = tk.Text(recommendations_frame, width=40, height=10)
recommendations.pack(fill=tk.BOTH, expand=True)

recommend_button = tk.Button(recommendations_frame, text="Show Recommendations", command=update_recommendations)
recommend_button.pack(pady=10)

root.mainloop()

