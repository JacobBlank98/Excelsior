import os, tempfile
from google_images_search import GoogleImagesSearch


#Google and download a picture
def GetGoogleImage(query, PathToDownload):
 
    gis = GoogleImagesSearch('AIzaSyBAcmq00cLgRfvmYsasuaqmuqKhe0HN6KI ', '004157383614410840261:hcpju7llgou')
    
    # GSImage gsImage
    
    # define search params:
    _search_params = {
        'q': query,
        'num': 1,
        'safe': '',
        'fileType': 'jpg',
        'imgType': 'photo',
        'imgSize': '',
        'imgDominantColor': ''
    }
    
    # this will search, download and resize:
    gis.search(search_params=_search_params, path_to_dir = PathToDownload)
    for image in gis.results():
        print(" \n" + image.path)
        return image.path  
        
    
#Remove The file
def DeleteImage(imagePath):
    try:
        os.remove(imagePath)
        print("file removed")
    except:
        print("file not found")


#Use Functionality independently
if __name__ == "__main__":

    query = input("What image do you want to download?")
    PathToDownload = input("Where should I download?")
    
    if os.path.isdir(PathToDownload) == 0:
        print("That's not a directory!")
    else:
        GetGoogleImage(query, PathToDownload)      
    
  
