class Stations:
    def __init__(self, bike_list, name):
        # creates the object station with attributes
        self.bike_list = bike_list
        self.name = name


    def give_bike(self):
        # віддати велосипед
        # зі спиcку bike_list забираємо елемент bike
        bike_given = self.bike_list.pop()
        return bike_given

    def return_away(self, bike_given):
        # повернути велосипед
        # до списку bike list додаємо елемент bike
        return self.bike_list.append(bike_given)
