import os, tempfile
from google_images_search import GoogleImagesSearch
from GoogleSearch import GetGoogleImage, DeleteImage
from Image_and_Caption import post_image_and_caption
from random_location import random_location
import os
import tweepy
import pandas as pd

# only works if there is a single picture in file
# must delete picture from file after using it

def return_absolute_image_reference(dir):
    for filename in os.listdir(dir):
        absolute_image_reference = str(dir) + '/' + str(filename)
        return absolute_image_reference


img_dir = input("What's the directory of the google_picture_downloads file?")
query = random_location()
PathToDownload = img_dir

if os.path.isdir(PathToDownload) == 0:
    print("That's not a directory!")
else:
    GetGoogleImage(query, PathToDownload)

absolute_image_reference = return_absolute_image_reference(dir=img_dir)  # absolute directory of image (sometimes
# returns NoneType ??? )

caption = ("Hi from {}.".format(query))  # caption to be posted

post_image_and_caption(image=absolute_image_reference, caption=caption)

DeleteImage(absolute_image_reference)  # Deletes image from google_images download file
