class Bike:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def price_per_minute(self):
        if self.type == "electrical":
            return 5
        elif self.type == "normal":
            return 2