class Product:
    """Represents and manages a single product."""

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = 0
        self.update_stock(stock)  # reuse the validation in update_stock

    # --- Read-only access (getters) ---
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # --- Behaviour ---
    def update_stock(self, quantity):
        """Set the stock level. Rejects negative or non-integer values."""
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Stock must be a non-negative whole number.")
        self.__stock = quantity

    def display_information(self):
        print("ID:", self.__product_id, "| Name:", self.__name,
              "| Price: $" + str(self.__price), "| Stock:", self.__stock)

    # --- Conversion helpers (no file handling in here) ---
    def to_dict(self):
        return {"id": self.__product_id, "name": self.__name,
                "price": self.__price, "stock": self.__stock}

    @staticmethod
    def from_dict(data):
        return Product(data["id"], data["name"], data["price"], data["stock"])
