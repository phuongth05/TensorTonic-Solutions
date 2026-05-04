def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here

    image_matrix = [0]*256

    for row in image:
        for pix in row:
            image_matrix[pix] += 1

    return image_matrix