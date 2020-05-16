import pandas as pd
import random, os 


def random_location():
    data = pd.read_csv("world-cities.csv")
    index = random.choice(range(len(data)))
    complete_name = str(data['name'][index]) + ' city, ' + str(data['country'][index])
    return complete_name

def random_image_path(file_directory):
    choice = random.choice(os.listdir(str(file_directory)))
    image_path = file_directory + '/' + choice
    return image_path

if __name__ == "__main__":
    random_location()

