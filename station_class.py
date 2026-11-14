class Station:
    def __init__(self, name):
        # creates the object station with attributes
        self.bike_list = []
        self.name = name


    def remove_bike(self, index):
        # віддати велосипед
        # зі спиcку bike_list забираємо елемент bike
        self.bike_list.pop(index)
        return None

    def receive_bike(self, bike):
        # повернути велосипед
        # до списку bike list додаємо елемент bike
        self.bike_list.append(bike)
        return None
