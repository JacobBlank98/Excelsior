import os, tempfile
from google_images_search import GoogleImagesSearch

CurrentPath = str(os.getcwd())

# if you don't enter api key and cx, the package will try to search
# them from environment variables GCS_DEVELOPER_KEY and GCS_CX
query = input("What Picture do you want to download?")



gis = GoogleImagesSearch('AIzaSyBAcmq00cLgRfvmYsasuaqmuqKhe0HN6KI ', '004157383614410840261:hcpju7llgou')

# example: GoogleImagesSearch('ABcDeFGhiJKLmnopqweRty5asdfghGfdSaS4abC', '012345678987654321012:abcde_fghij')

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


# this will search and download:
gis.search(search_params=_search_params, path_to_dir= CurrentPath +  '/DownloadedPics/')

# this will only search for images:
#gis.search(search_params=_search_params)


# this will search, download and resize:
# gis.search(search_params=_search_params, path_to_dir='/path/', width=500, height=500)

# search first, then download and resize afterwards:
#gis.search(search_params=_search_params)
# for image in gis.results():
    # image.download('/path/')
    # image.resize(500, 500)