import numpy as np

def histogram_equalize(image):
    """
    Apply histogram equalization to enhance image contrast.
    """
    # Write code here
    image = np.array(image)
    flatten_img = image.flatten()

    histogram = np.zeros(256, dtype=int)

    for i in range(256):
        histogram[i] = np.sum(flatten_img == i)

    cdf =  np.zeros_like(histogram)

    for i in range(256):
        cdf[i] = np.sum([histogram[j] for j in range(0, i + 1)])

    cdf_min = np.min(cdf[cdf != 0])

    output = np.zeros_like(image)

    if np.all(len(flatten_img) == cdf_min):
        return output.tolist()

    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            output[i, j] = np.round((cdf[image[i, j]] - cdf_min)
                                / (len(flatten_img) - cdf_min)
                                * 255)
    return output.tolist()
        

    