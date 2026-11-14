import bike_class
import client_class
import network_class
import station_class

def main():
    bike_first = bike_class.Bike(1, "normal")
    bike_second = bike_class.Bike(2, "electrical")
    bike_third = bike_class.Bike(3, "normal")
    bike_four = bike_class.Bike(4, "normal")
    bike_five = bike_class.Bike(5, "electrical")

    station_A = station_class.Station("A")
    station_B = station_class.Station("B")

    station_A.receive_bike(bike_first)
    station_A.receive_bike(bike_second)
    station_A.receive_bike(bike_third)
    station_B.receive_bike(bike_four)
    station_B.receive_bike(bike_five)

    client_1 = client_class.Client("client_1", 1000)
    client_2 = client_class.Client("client_2", 200)

    network = network_class.Network()

    income_1 = client_1.do_ride(station_A, station_A, "electrical", 90)
    income_2 = client_2.do_ride(station_B, station_A, "normal", 5)
    income_3 = client_2.do_ride(station_B, station_A, "electrical", 10)

    income_4 = client_2.do_ride(station_B, station_A, "normal", 10)

    income_list = [income_1, income_2, income_3, income_4]
    for income in income_list:
        if income == -1:
            print("На станції немає велосипеду потрібного типу.")
        elif income == -2:
            print("У клієнта недостатньо коштів на балансі.")
        elif income == -3:
            print("На станції всі електричні велосипеди розряджені")
        elif income == -4:
            print("Користувачу не вистачить заряду на поїздку")
        else:
            network.money += income

    discharged_bikes = []

    for station in [station_A, station_B]:
        print(f"На станції {station.name} {len(station.bike_list)} велосипедів")
        discharged_bikes.extend(station.get_discharged())


    print(f"Мережа заробила {network.money} грн")

    discharged_bikes_infos = {}

    for bike in discharged_bikes:
        for station in [station_A, station_B]:
            if bike in station.bike_list:
                discharged_bikes_infos[bike.number] = {"station": station.name, "charge": bike.charge}

    print(f"Список розряджених велосипедів: {discharged_bikes_infos}")



main()

