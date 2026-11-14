class Bike:
    def __init__(self, number, type):
        self.number = number
        self.type = type
        self.charge = 100
        self.ppm = 0
        if self.type == "electrical":
            self.ppm = 5
        elif self.type == "normal":
            self.ppm = 2