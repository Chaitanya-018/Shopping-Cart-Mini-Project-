class ShoppingCart:
    def __init__(self):
        self.products = [
            {"id": 1, "name": "Laptop", "price": 45000},
            {"id": 2, "name": "Smartphone", "price": 15000},
            {"id": 3, "name": "Headphones", "price": 2000},
            {"id": 4, "name": "Keyboard", "price": 1200},
            {"id": 5, "name": "Mouse", "price": 800},
            {"id": 6, "name": "Charger", "price": 500},
            {"id": 7, "name": "USB Cable", "price": 300},
            {"id": 8, "name": "Backpack", "price": 2500}
        ]
        self.cart = []

    # 1. View products
    def view_products(self):
        print("\n===== Available Products =====")
        for p in self.products:
            print(f"{p['id']}. {p['name']} - ₹{p['price']}")
        print("==============================\n")

    # 2. Add product to cart
    def add_to_cart(self, product_id, quantity):
        # Check total quantity in cart
        total_quantity = sum(item["quantity"] for item in self.cart)
        if total_quantity + quantity > 8:
            print("Cart limit reached! You can only have up to 8 items in total.")
            return

        # Find product
        product = None
        for p in self.products:
            if p["id"] == product_id:
                product = p
                break

        if product is None:
            print("Invalid Product ID.")
            return

        # If product already in cart  increase quantity
        for item in self.cart:
            if item["id"] == product_id:
                item["quantity"] += quantity
                print(f"Updated {product['name']} quantity to {item['quantity']}")
                return

        # Otherwise add new product
        self.cart.append({
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })
        print(f"{product['name']} added to cart.")

    # 3. View cart
    def view_cart(self):
        if not self.cart:
            print("\n🛒 Cart is empty.\n")
            return

        print("\n===== Your Cart =====")
        total = 0
        for item in self.cart:
            subtotal = item["price"] * item["quantity"]
            print(f"{item['id']}. {item['name']} - ₹{item['price']} x {item['quantity']} = ₹{subtotal}")
            total += subtotal
        print("-----------------------")
        print(f"Total Amount: ₹{total}")
        print("=======================\n")

    # 4. Update cart
    def update_cart(self, product_id, quantity):
        for item in self.cart:
            if item["id"] == product_id:
                item["quantity"] = quantity
                print(f"{item['name']} quantity updated to {quantity}")
                return
        print("Product not found in cart.")

    # 5. Remove from cart
    def remove_from_cart(self, product_id):
        for item in self.cart:
            if item["id"] == product_id:
                self.cart.remove(item)
                print(f"{item['name']} removed from cart.")
                return
        print("Product not found in cart.")

    # 6. Checkout
    def checkout(self):
        if not self.cart:
            print("\nCart is empty. Nothing to checkout.\n")
            return

        print("\n===== Checkout Bill =====")
        total = 0
        for item in self.cart:
            subtotal = item["price"] * item["quantity"]
            print(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{subtotal}")
            total += subtotal
        print("---------------------------")
        print(f"Grand Total: ₹{total}")
        print("===========================")
        print("Thank you for shopping with us!\n")

        self.cart.clear()  # empty cart after checkout

    # 7. Menu
    def menu(self):
        while True:
            print("===== Shopping Cart =====")
            print("1. View Products")
            print("2. Add to Cart")
            print("3. View Cart")
            print("4. Update Cart")
            print("5. Remove from Cart")
            print("6. Checkout")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_products()
            elif choice == "2":
                try:
                    pid = int(input("Enter Product ID: "))
                    qty = int(input("Enter Quantity: "))
                    self.add_to_cart(pid, qty)
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
            elif choice == "3":
                self.view_cart()
            elif choice == "4":
                try:
                    pid = int(input("Enter Product ID to update: "))
                    qty = int(input("Enter new Quantity: "))
                    self.update_cart(pid, qty)
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
            elif choice == "5":
                try:
                    pid = int(input("Enter Product ID to remove: "))
                    self.remove_from_cart(pid)
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
            elif choice == "6":
                self.checkout()
            elif choice == "7":
                print("Exiting... Goodbye!")
                break
            else:
                print("invalid choice. Try again.")


# Run program

app = ShoppingCart()
app.menu()
