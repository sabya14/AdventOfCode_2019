import math
import os

path = os.path.join(os.path.dirname((os.path.abspath(__file__))), "test_files")


def input_data():
    with open(os.path.join(path, "day_2.txt")) as file:
        data = file.read()
        return data


def op_code():
    data = list(map(int, input_data().split(",")))
    data[1] = 12
    data[2] = 2
    for i in range(0, len(data), 4):
        if data[i] == 1:
            data[data[i + 3]] = data[data[i + 2]] + data[data[i + 1]]
        elif data[i] == 2:
            data[data[i + 3]] = data[data[i + 2]] * data[data[i + 1]]
        elif data[i] == 99:
            break
    return data


print(op_code())
