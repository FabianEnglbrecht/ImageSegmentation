import skimage
skimage.__version__
import cv2
from skimage import io
import numpy as np
from skimage import measure, io, img_as_ubyte
import matplotlib.pyplot as plt
from skimage.color import label2rgb, rgb2gray

import matplotlib.pyplot as plt
from skimage import data

#img = data.coins()



#img = cv2.imread('org2.png')
img = img_as_ubyte(rgb2gray(io.imread("org2.png")))

#plt.imshow(img, cmap='gray')
#plt.show()


from skimage import feature
edges = skimage.feature.canny(img, sigma=1)

plt.imshow(edges)
plt.show()