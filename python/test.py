from PIL import Image
import PIL.ImageOps

# import numpy as np
# import Image
#
# im = Image.open('new_name.png')
# im = im.convert('RGBA')
# data = np.array(im)
#
# r1, g1, b1 = 224, 224, 224  # Original value
# r2, g2, b2, a2 = 255, 255, 255, 255  # Value that we want to replace it with
#
# red, green, blue, alpha = data[:, :, 0], data[:, :, 1], data[:, :, 2], data[:, :, 3]
# mask = (red == r1) & (green == g1) & (blue == b1)
# data[:, :, :4][mask] = [r2, g2, b2, a2]
#
# im = Image.fromarray(data)
# im.save('fig1_modified.png')


import os

for file in os.listdir("."):
    if file[-3:] == 'png':
        image = Image.open(file)
        inverted_image = PIL.ImageOps.invert(image)
        inverted_image.save('invert/' + file)
