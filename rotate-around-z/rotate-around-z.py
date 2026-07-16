import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    # Your code here

    if np.asarray(points).ndim == 1:
        x = points[0]
        y = points[1]
        z = points[2]

        _x = x*np.cos(theta) - y*np.sin(theta)
        _y = x*np.sin(theta) + y*np.cos(theta)
        _z = z

        return np.array([_x, _y, _z])

    output = []
        
        

    for point in points:
        x = point[0]
        y = point[1]
        z = point[2]

        _x = x*np.cos(theta) - y*np.sin(theta)
        _y = x*np.sin(theta) + y*np.cos(theta)
        _z = z

        output.append((_x, _y, _z))

    return np.array(output)
    pass