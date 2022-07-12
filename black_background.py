from PIL import Image
import os

# Declare path and filetype of thresholded images
items = os.listdir("./11_Otsu")
newlist = []
for names in items:
    if names.endswith("otsu.png"):
        newlist.append(names)
b = len(newlist)
print(b)
a = 1

pixellist = []


# Declare path and filetype of microscopy images
img = Image.open("./11_Otsu/otsu.png")

# Create a pixel map for each image
pixels = img.load()

# Change the value of each pixel to (0,0,0)
for i in range(img.size[0]):  # for every pixel:
    for j in range(img.size[1]):
        if pixels[i, j] != (0):  # if not black:

            pixels[i, j] = (0)  # change to black

# Export the image (background)
img.save("./Background/frame_black.png")

