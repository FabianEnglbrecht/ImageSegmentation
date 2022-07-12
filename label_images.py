import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage import data, measure, io, img_as_ubyte
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb, rgb2gray

image = img_as_ubyte(rgb2gray(io.imread("Samuel_organoid_segment_thresholded.jpg")))
#image = data.coins()[50:-50, 50:-50]

# apply threshold
thresh = threshold_otsu(image)
print(thresh)
bw = closing(image > thresh, square(3))

# remove artifacts connected to image border
cleared = clear_border(bw)

# label image regions
label_image = label(cleared)
#print(label_image)
image_label_overlay = label2rgb(label_image, image=image)

props = measure.regionprops_table(label_image, image, properties=['label','area','bbox','equivalent_diameter','mean_intensity'])

import pandas as pd
df = pd.DataFrame(props)
#pd.set_option("display.max_rows", None, "display.max_columns", None)
#f= open("output.txt","w+")
#f.write(str(df))
#f.close()

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(image_label_overlay)

#for region in regionprops(label_image):
#    # take regions with large enough areas
#    if region.area >= 70:
#        # draw rectangle around segmented coins
#        minr, minc, maxr, maxc = region.bbox
#        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr, fill=False, edgecolor='red', linewidth=1)
#        ax.add_patch(rect)



#ax.set_axis_off()
plt.tight_layout()
plt.show()

# box output: y1,x1,y2,x2
#   554     457     571     476