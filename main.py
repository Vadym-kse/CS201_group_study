import bike_class
import client_class
import network_class
import station_class

def main():
    bike_first = bike_class.Bike(1, "normal", 100)
    bike_second = bike_class.Bike(2, "electrical", 80)
    bike_third = bike_class.Bike(3, "normal", 75)
    bike_four = bike_class.Bike(4, "electrical", 67)
    bike_five = bike_class.Bike(5, "electrical", 42)

    station_A = station_class.Station("A")
    station_B = station_class.Station("B")

    station_A.receive_bike(bike_first)
    station_A.receive_bike(bike_second)
    station_A.receive_bike(bike_third)
    station_B.receive_bike(bike_four)
    station_B.receive_bike(bike_five)

    client_1 = client_class.Client("client_1", 100)
    client_2 = client_class.Client("client_2", 200)

    network = network_class.Network()

    income_1 = client_1.do_ride(station_A, station_B, "normal", 10)
    income_2 = client_2.do_ride(station_B, station_A, "normal", 5)
    income_3 = client_2.do_ride(station_B, station_B, "electrical", 10)

    income_4 = client_2.do_ride(station_B, station_A, "normal", 10)

    income_list = [income_1, income_2, income_3, income_4]
    for income in income_list:
        if income == -1:
            print("На станції недостатньо немає велосипеду потрібного типу.")
        elif income == -2:
            print("У клієнта недостатньо коштів на балансі.")
        elif income == -3:
            print("На станції всі електричні велосипеди розряджені")
        else:
            network.money += income

    print(f"На станції {station_A.name} {len(station_A.bike_list)} велосипедів, на станції {station_B.name} {len(station_B.bike_list)} велосипедів")
    print(f"Мережа заробила {network.money} грн")

main()

