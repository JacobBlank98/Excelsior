import os, tempfile
from google_images_search import GoogleImagesSearch
from Random_Location_Generator.random_location import random_location


# Google and download a picture
def GetGoogleImage(PathToDownload):

    gis = GoogleImagesSearch('AIzaSyBAcmq00cLgRfvmYsasuaqmuqKhe0HN6KI ', '004157383614410840261:hcpju7llgou')

    # GSImage gsImage

    # this will search, download and resize:
    while len(gis.results()) == 0:
        question = random_location()
        # define search params:
        _search_params = {
            'q': question,
            'num': 1,
            'safe': '',
            'fileType': 'jpg',
            'imgType': 'photo',
            'imgSize': '',
            'imgDominantColor': ''
        }
        gis.search(search_params=_search_params, path_to_dir=PathToDownload)

    return gis.results()[0].path, question

# Remove The file
def DeleteImage(imagePath):
    try:
        os.remove(imagePath)
        print("file removed")
    except:
        print("file not found")


# Use Functionality independently
if __name__ == "__main__":

    PathToDownload = input("Where should I download?")

    if os.path.isdir(PathToDownload) == 0:
        print("That's not a directory!")
    else:
        GetGoogleImage(PathToDownload)      
  
