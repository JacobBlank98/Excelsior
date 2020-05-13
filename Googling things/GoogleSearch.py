import os, tempfile
from google_images_search import GoogleImagesSearch



def GetGoogleImage(query, PathToDownload):

    # if you don't enter api key and cx, the package will try to search
    # them from environment variables GCS_DEVELOPER_KEY and GCS_CX
    # query = input("What Picture do you want to download?")
    
    gis = GoogleImagesSearch('AIzaSyBAcmq00cLgRfvmYsasuaqmuqKhe0HN6KI ', '004157383614410840261:hcpju7llgou')
    
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
    gis.search(search_params=_search_params, path_to_dir= PathToDownload, width=1000, height=500)

def DeleteImage(imagePath):
    try:
        os.remove(imagePath)
        print("file removed")
    except:
        print("file not found")

# os.remove(file) for file in os.listdir(CurrentPath) if file.endswith('.jpg')
# this will search and download:
#gis.search(search_params=_search_params, path_to_dir= CurrentPath +  '/DownloadedPics/')
# 
# this will only search for images:
#gis.search(search_params=_search_params)
# # search first, then download and resize afterwards:
# gis.search(search_params=_search_params)
# for image in gis.results():
    # image.download(CurrentPath +  '/DownloadedPics/')
    # image.resize(1000, 500)
    

    
