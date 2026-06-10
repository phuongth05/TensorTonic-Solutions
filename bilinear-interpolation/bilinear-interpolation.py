import numpy as np
import math

def bilinear_resize(image, new_h, new_w):
    """
    Resize a 2D grid using bilinear interpolation.
    """
    # Write code here
    image = np.array(image)
    h, w = image.shape
    
    output = np.zeros((new_h, new_w))

    for i in range(new_h):
        for j in range(new_w):
            src_y = i * (h - 1)/(new_h - 1) if new_h > 1 else 0.0
            src_x = j * (w - 1)/(new_w - 1) if new_w > 1 else 0.0

            d_y, y0 = math.modf(src_y)
            d_x, x0 = math.modf(src_x)
            y0, x0 = int(y0), int(x0)
            y1 = min(y0 + 1, h - 1)
            x1 = min(x0 + 1, w - 1)
            
            out = float(image[y0, x0] * (1 - d_y) * (1 - d_x)
                    + image[y1, x0] * d_y * (1 - d_x)
                    + image[y0, x1] * (1 - d_y) * d_x
                    + image[y1, x1] * d_y * d_x)

            output[i, j] = out

    return output.tolist()
    pass