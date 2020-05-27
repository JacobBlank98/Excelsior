import os
from Googling.GoogleSearch import GetGoogleImage
from Twitter.Image_and_Caption import post_image_and_caption
from Random_Location_Generator.random_location import random_location, random_image_path
from CopyPasting.CopyPaste import ResizeTopPicture, CopyPaste

# file/image paths
cwd = os.getcwd()
City_Path = "{}/temp".format(cwd) 
Troy_Abed_Path = "{}/TroyandAbedPics".format(cwd)
Resized_Path = "{}/temp/Resized.png".format(cwd)
Merged_Path = "{}/temp/MergedPic.jpg".format(cwd)

# top & bottom Images
bottom_image_path, query = GetGoogleImage(PathToDownload=City_Path)
top_image_path = random_image_path(Troy_Abed_Path)

# Google Query
modified_query = query.replace(" city,", ",")
caption = ("Troy and Abed telepoooorting! This time to {}.".format(modified_query))

# resizing and merging
ResizeTopPicture(top_image_path, bottom_image_path, Resized_Path)
CopyPaste(Resized_Path, bottom_image_path, Merged_Path)

# posting
post_image_and_caption(image=Merged_Path, caption=caption)

# deleting images
os.remove(bottom_image_path)
os.remove(Resized_Path)
os.remove(Merged_Path)
os.rmdir(City_Path)
