import pandas as pd
import random

data = pd.read_csv("world-cities.csv")


def random_location():
    index = random.choice(range(len(data)))
    complete_name = str(data['name'][index]) + ', ' + str(data['country'][index])
    return complete_name


if __name__ == "__main__":
    random_location()

