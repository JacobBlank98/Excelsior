from GoogleSearch import GetGoogleImage, DeleteImage, return_absolute_image_reference
from Image_and_Caption import post_image_and_caption
from random_location import random_location, random_image_path
from CopyPaste import ResizeTopPicture, CopyPaste

# User Inputs for file/image paths
City_Path = input("Enter directory of file to save background/city photos to.")
Troy_Abed_Path = input("Enter directory of file to save foreground/TroyAbed")
Resized_Path = input("Enter absolute path for resized image.")
Merged_Path = input("Enter absolute path for merged image.")

# Google Query
query = random_location()  # random city name
caption = ("Troy and Abed telepoooorting! This time to {}.".format(query))  # caption to be posted

# top & bottom Images
bottom_image_path = GetGoogleImage(query, PathToDownload=City_Path)
top_image_path = random_image_path(Troy_Abed_Path)

# resizing and merging
ResizeTopPicture(top_image_path, bottom_image_path, Resized_Path)
CopyPaste(top_image_path, bottom_image_path, Merged_Path)

# posting
post_image_and_caption(image=Merged_Path, caption=caption)

# deleting images
DeleteImage(imagePath=City_Path)
DeleteImage(imagePath=Resized_Path)
DeleteImage(imagePath=Merged_Path)
