import csv


class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_value(self):
        return sum(
            p.price * p.quantity
            for p in self.products
        )

    def find_product(self, name):
        for p in self.products:
            if p.name.lower() == name.lower():
                return p
        return None

    def save_to_csv(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(
                ["name", "price", "quantity"]
            )

            for p in self.products:
                writer.writerow(
                    [p.name, p.price, p.quantity]
                )

    def load_from_csv(self, filename):
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                self.products.append(
                    Product(
                        row["name"],
                        float(row["price"]),
                        int(row["quantity"])
                    )
                )


inventory = Inventory()

inventory.add_product(Product("Laptop", 50000, 2))
inventory.add_product(Product("Mouse", 500, 5))

print(inventory.total_value())