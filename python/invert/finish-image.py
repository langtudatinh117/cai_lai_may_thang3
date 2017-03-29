import numpy as np
import Image
import os

for file in os.listdir("."):
    if file[-3:] == 'png':
        im = Image.open(file)
        im = im.convert('RGBA')
        data = np.array(im)

        r1, g1, b1 = 224, 224, 224  # Original value
        r2, g2, b2, a2 = 255, 255, 255, 255  # Value that we want to replace it with

        red, green, blue, alpha = data[:, :, 0], data[:, :, 1], data[:, :, 2], data[:, :, 3]
        mask = (red == r1) & (green == g1) & (blue == b1)
        data[:, :, :4][mask] = [r2, g2, b2, a2]

        im = Image.fromarray(data)
        im.save('done/' + file)
