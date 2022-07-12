from skimage import measure, io, img_as_ubyte
import matplotlib.pyplot as plt
from skimage.color import label2rgb, rgb2gray
import numpy as np

image = img_as_ubyte(rgb2gray(io.imread("org2.png")))

from skimage.filters import threshold_otsu
threshold = threshold_otsu(image)
#print(threshold)

label_image = measure.label(image < threshold, connectivity=image.ndim)
#print(label_image)
#plt.imshow(label_image)

image_label_overlay = label2rgb(label_image, image=image)
plt.imshow(image_label_overlay)
props = measure.regionprops_table(label_image, image, properties=['label','area','bbox','equivalent_diameter','mean_intensity'])

import pandas as pd
df = pd.DataFrame(props)
print(df)



plt.show()
