import os
from PIL import Image 
 
 
def ResizeTopPicture(TopImagePath, BottomImagePath, ResizedSavePath):
    
    BottomImage = Image.open(BottomImagePath)
    TopImage = Image.open(TopImagePath)
    
    BottomWidth, BottomHeight = BottomImage.size
    OldWidth, OldHeight = TopImage.size
    
    NewHeight = int(BottomHeight / 3)
    NewWidth = int(NewHeight * (OldWidth / OldHeight))
    
    NewTopImage = TopImage.resize((NewWidth, NewHeight))
    NewTopImage.save(ResizedSavePath)
 
 
def CopyPaste(TopImagePath, BottomImagePath, SavePath):

    # open the images, get their sizes and make a copies so they're not affected
    TopImage = Image.open(TopImagePath) 
    TopImageCopy = TopImage.copy() 
    TopWidth, TopHeight = TopImage.size   
    BottomImage = Image.open(BottomImagePath) 
    BottomWidth, BottomHeight = BottomImage.size
    BottomImageCopy = BottomImage.copy() 

    pasteWidth = int((BottomWidth / 2) - (TopWidth / 2))
    pasteHeight = int(BottomHeight - TopHeight)
    
    # paste image giving dimensions 
    BottomImageCopy.paste(TopImageCopy, (pasteWidth, pasteHeight), mask=TopImageCopy) 
    
    # save the image  
    BottomImageCopy.save(SavePath) 




if __name__ == "__main__":
    
    TopImagePath = input ("Enter Top Image path")
    BottomImagePath = input("Enter Bottom Image path")
    SavePath = input("Enter where to Save Image")
    
    if os.path.isfile(TopImagePath) == 0:
        print("TopImage Directory does not exist")
    elif os.path.isfile(BottomImagePath) == 0:
        print("BottomImagePath Directory does not exist")
    
    # CopyPaste(TopImagePath, BottomImagePath, SavePath)
    ResizeTopPicture(TopImagePath, BottomImagePath, SavePath)
