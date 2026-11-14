import bike_class
import client_class
import network_class
import station_class

def main():
    bike_first = bike_class.Bike("first", "normal")
    bike_second = bike_class.Bike("second", "electrical")
    bike_third = bike_class.Bike("third", "normal")
    bike_four = bike_class.Bike("four", "electrical")
    bike_five = bike_class.Bike("five", "electrical")

    station_A = station_class.Stations([bike_first, bike_second], "A")
    station_B = station_class.Stations([bike_third, bike_four, bike_five], "B")

