import numpy as np

def sobel_edges(image):
    """
    Apply the Sobel operator to detect edges.
    """
    # Write code here

    image = np.array(image)

    pad_image = np.pad(image, pad_width=((1, 1), (1, 1)), mode='constant', constant_values='0')

    k_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    k_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    img_h, img_w = pad_image.shape
    output = np.zeros((img_h - 3 + 1, img_w - 3 + 1))
    out_h, out_w = output.shape
    
    for i in range(out_h):
        for j in range(out_w):
            apply = pad_image[i:i+3, j:j+3]
            g_x = apply * k_x
            g_y = apply * k_y

            sum_x = np.sum(g_x)
            sum_y = np.sum(g_y)

            mag = np.sqrt(sum_x**2 + sum_y**2)
            output[i, j] = mag

    return output.tolist()