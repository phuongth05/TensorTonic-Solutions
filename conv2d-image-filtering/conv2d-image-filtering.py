import numpy as np

def conv2d(image, kernel, stride=1, padding=0):
    """
    Apply 2D convolution to a single-channel image.
    """
    # Write code here
    image = np.array(image)
    kernel = np.array(kernel)
    
    pad_image = np.pad(image, pad_width=((padding, padding), (padding, padding)), mode='constant', constant_values=0)

    img_h, img_w = pad_image.shape
    ker_h, ker_w = kernel.shape

    out_h = (img_h - ker_h) // stride + 1
    out_w = (img_w - ker_w) // stride + 1

    out_img = np.zeros((out_h, out_w))

    for i in range(out_h):
        for j in range(out_w):
            row = i * stride
            col = j * stride
            apply = pad_image[row:row+ker_h, col:col+ker_w]

            out_img[i, j] = np.sum(apply * kernel)
    
    return out_img.tolist()
    pass