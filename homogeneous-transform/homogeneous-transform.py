import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here

    T = np.array(T)
    points = np.array(points)

    if points.ndim == 1:
        points = points.reshape(1, -1)

    homogeneous_points = np.hstack((points, np.ones((points.shape[0], 1))))

    transformed_points = (T @ homogeneous_points.T).T

    result_points = transformed_points[:, :-1]

    if points.shape[0] == 1:
        result_points = result_points.reshape(3,)

    return result_points
    pass