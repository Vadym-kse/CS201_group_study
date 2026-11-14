class Bike:
    def __init__(self, type):
        self.type = type
        self.ppm = 0
        if self.type == "electrical":
            self.ppm = 5
        elif self.type == "normal":
            self.ppm = 2