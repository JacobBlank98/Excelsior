import os
from PIL import Image 
from Googling.GoogleSearch import GetGoogleImage, DeleteImage
from Twitter.Image_and_Caption import post_image_and_caption
from Random_Location_Generator.random_location import random_location, random_image_path
from CopyPasting.CopyPaste import ResizeTopPicture, CopyPaste

# User Inputs for file/image paths
City_Path = ".\temp"
Troy_Abed_Path = ".\TroyandAbedPics"
Resized_Path = ".\temp\Resized.jpg"
Merged_Path = ".\temp\MergedPic.jpg"

# Google Query
query = random_location()  # random city name
caption = ("Troy and Abed telepoooorting! This time to {}.".format(query))  # caption to be posted

# top & bottom Images
bottom_image_path = GetGoogleImage(query, PathToDownload=City_Path)
print(bottom_image_path)
top_image_path = random_image_path(Troy_Abed_Path)

# resizing and merging
ResizeTopPicture(top_image_path, bottom_image_path, Resized_Path)
CopyPaste(top_image_path, bottom_image_path, Merged_Path)

# posting
post_image_and_caption(image=Merged_Path, caption=caption)

# deleting images
DeleteImage(imagePath=bottom_image_path)
DeleteImage(imagePath=Resized_Path)
DeleteImage(imagePath=Merged_Path)
