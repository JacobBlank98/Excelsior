import pandas as pd
import random


def random_location():
    data = pd.read_csv("world-cities.csv")
    index = random.choice(range(len(data)))
    complete_name = str(data['name'][index]) + ' city, ' + str(data['country'][index])
    return complete_name


if __name__ == "__main__":
    random_location()
