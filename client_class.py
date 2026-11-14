class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def do_ride(self, station_start, station_end, wanted_type, duration):
        length = len(station_start.bikes)
        chosen_bike = None
        chosen_index = None
        for i in range(length):
            curbike = station_start.bikes[i]

            if curbike.type == wanted_type:
                chosen_bike = curbike
                chosen_index = i
                break

        if (chosen_index == None):
            print(f"На станції {station_start.name} немає велосипеду потрібного типу.")
            return -1
        moneyspent = chosen_bike.price * duration
        if (moneyspent > self.balance):
            print(f"У клієнта {self.name} недостатньо коштів на балансі.")
            return -1

        station_start.bikes.pop(chosen_index)
        station_end.bikes.append(chosen_bike)

        self.balance -= moneyspent

        return moneyspent


