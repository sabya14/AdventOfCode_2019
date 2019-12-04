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
    for mass in data.split("\n"):
        fuel = int(int(mass)//3) - 2
        result = result + fuel
    return result


print(fuel_counter())