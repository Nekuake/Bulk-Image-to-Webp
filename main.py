from PIL import Image
import sys
from tkinter import filedialog
import os


def convertionImage(imagePath="", finalDir="", resize_images=False, quality=70):
    print(imagePath)
    image = Image.open(imagePath)
    if resize_images:
        if image.width > image.height:
            image = image.resize((512, int(image.height * 512 / image.width)))
        elif image.width < image.height:
            image = image.resize((int(image.width * 512 / image.height), 512))
        else:
            image = image.resize((512, 512))
    image.save(finalDir + "/" + (os.path.basename(imagePath).rsplit(".")[0]) + ".webp", "webp", quality=quality)


print(sys.argv)  # Might add drag-and-drop support
if len(sys.argv) == 1:
    print("No filename/folder dropped.")
    containerDir = filedialog.askdirectory(title="Select directory containing all PNGs")
else:
    containerDir = sys.argv[1]  # In case there's arguments like the folder path, just use them
finalDir = os.path.join(containerDir, "WebP")
if not os.path.isdir(finalDir):
    os.mkdir(finalDir)
imagesList = next(os.walk(containerDir), (None, None, []))[2]  # [] if no file
quality=int(input("Which quality? 0-100: ").strip())
for x in range(len(imagesList)):
    convertionImage(os.path.join(containerDir, imagesList[x]), finalDir,  quality)
