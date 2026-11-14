class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def do_ride(self, station_start, station_end, wanted_type, duration):
        length = len(station_start.bike_list)
        chosen_bike = None
        chosen_index = None
        for i in range(length):
            curbike = station_start.bike_list[i]

            if curbike.type == wanted_type:
                chosen_bike = curbike
                chosen_index = i
                break

        if (chosen_index == None):
            return -1
        moneyspent = chosen_bike.ppm * duration
        if (moneyspent > self.balance):
            return -2

        station_start.remove_bike(chosen_index)
        station_end.receive_bike(chosen_bike)

        self.balance -= moneyspent

        return moneyspent


