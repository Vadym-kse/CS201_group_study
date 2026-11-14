class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def do_ride(self, station_start, station_end, wanted_type, duration):
        length = len(station_start.bike_list)
        chosen_bike = None
        chosen_index = None

        electrical_present = False
        allowed_electrical_present = False
        found_electrical = False


        if wanted_type == "normal":
            for i in range(length):
                curbike = station_start.bike_list[i]

                if curbike.type == wanted_type:
                    chosen_bike = curbike
                    chosen_index = i
                    break
        else:
            for i in range(length):
                curbike = station_start.bike_list[i]

                if curbike.type == wanted_type:
                    electrical_present = True
                    if (curbike.charge < 20):
                        continue
                    allowed_electrical_present = True
                    if (curbike.charge < duration):
                        continue
                    found_electrical = True

                    chosen_bike = curbike
                    chosen_index = i
                    break

        if chosen_index == None and (wanted_type == "normal" or not electrical_present):
            return -1 #нема велосипеду потрібного типу
        moneyspent = chosen_bike.ppm * duration
        if (moneyspent > self.balance):
            return -2 #недостаньо грошей для поїздки
        if (electrical_present == True and not allowed_electrical_present):
            return -3 #є електричні велосипеди, але у всіх менше 20%
        if (allowed_electrical_present and not found_electrical):
            return -4 #є електричні велосипеди, але у жодного не вистачить на поїздку

        station_start.remove_bike(chosen_index)
        station_end.receive_bike(chosen_bike)

        self.balance -= moneyspent

        return moneyspent


