from PIL import Image
import sys
from tkinter import Tk, filedialog
import os
from pathlib import Path

def convertionImage(imagePath="", finalDir=""):
    print(imagePath)
    image=Image.open(imagePath)
    if image.width > image.height:
        image=image.resize((512, int(image.height*512/image.width)))
    elif image.width < image.height:
        image=image.resize((int(image.width*512/image.height), 512))
    else:
        image=image.resize((512,512))
    print((finalDir+"/"+(os.path.basename(imagePath).rsplit(".")[0])))
    image.save(finalDir+"/"+(os.path.basename(imagePath).rsplit(".")[0])+".webp", "webp")


print(sys.argv)
if len(sys.argv) == 1:
    print("No filename/folder dropped.")
    containerDir =filedialog.askdirectory(title="Select directory containing all PNGs")
else:
    containerDir=sys.argv[1]
finalDir=os.path.join(containerDir,"stickers")
if not os.path.isdir(finalDir):
    os.mkdir(finalDir)
imagesList = next(os.walk(containerDir), (None, None, []))[2]  # [] if no file
for x in range(len(imagesList)):
    convertionImage(os.path.join(containerDir,imagesList[x]),finalDir)

    