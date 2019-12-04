import math
import os
path = os.path.join(os.path.dirname((os.path.abspath(__file__))), "test_files")


def input_data():
    with open(os.path.join(path, "day_1.txt")) as file:
        data = file.read()
        return data


def fuel_counter():
    data = input_data()
    result = 0
    for fuel in data.split("\n"):
        new_fuel = int(int(fuel) // 3) - 2
        while 1:
            result = result + new_fuel
            new_fuel = int(int(new_fuel)//3) - 2
            if new_fuel <= 0:
                break
    return result


print(fuel_counter())