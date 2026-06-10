import numpy as np
import math

def rotate_image(image, angle_degrees):
    """
    Rotate the image counterclockwise by the given angle using nearest neighbor interpolation.
    """
    # Write code here
    image = np.array(image)
    H, W = image.shape

    radian_degree = math.radians(angle_degrees)
    
    c_y = 1.0*(H - 1) / 2
    c_x = 1.0*(W - 1) / 2

    output = np.zeros_like(image)

    for i in range(H):
        for j in range(W):
            d_y = i - c_y
            d_x = j - c_x

            src_y = round(c_y 
                    + d_y * math.cos(radian_degree) 
                    + d_x * math.sin(radian_degree))
            src_x = round(c_x 
                    - d_y * math.sin(radian_degree) 
                    + d_x * math.cos(radian_degree))

            if (0 <= src_y < H and 0 <= src_x < W):
                output[i, j] = image[src_y, src_x]

    return output.tolist()