def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here

    grayscale = []
    
    for row in image:
        gray_row = []
        for pix in row:
            r, g, b = pix
            gray_row.append(0.299 * r + 0.587 * g + 0.114 * b)
        grayscale.append(gray_row)
        
    return grayscale