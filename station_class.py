class Station:
    def __init__(self, name):
        self.bike_list = []
        self.name = name

    def remove_bike(self, index):
        self.bike_list.pop(index)
        return None

    def receive_bike(self, bike):
        self.bike_list.append(bike)
        return None

    def get_discharged(self):
        discharged = [bike.number for bike in self.bike_list if bike.charge < 20]
        return discharged

