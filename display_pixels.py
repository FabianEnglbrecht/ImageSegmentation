from PIL import Image
import numpy as np


pixels = [
   [(54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167)],
   [(204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93)],
   [(71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122)],
   [(168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)]
]

# Convert the pixels into an array using numpy
array = np.array(pixels, dtype=np.uint8)

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image.save('new.png')


pixels2=[
[(1.8775214e-02, 5.3827547e-02, 9.2739731e-01)],
[(2.9763652e-02, 1.6886963e-01, 8.0136669e-01)],
[(4.7682825e-02, 4.2931017e-01, 5.2300698e-01)]
   ]

# Convert the pixels into an array using numpy
array = np.array(pixels2, dtype=np.uint8)

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image.save('new2.png')