import numpy as np

def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    points = np.array(points)
    centroids = np.array(centroids)
    output = []
    
    for point in points:
        _min = 10000
        cen_idx = -1
        for i, cen in enumerate(centroids):
            _sum = np.sum([((point[d] - cen[d])**2) for d in range(len(point))])
            if _sum < _min:
                _min = _sum
                cen_idx = i
        
        output.append(cen_idx)

    return output