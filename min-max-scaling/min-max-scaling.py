import numpy as np
def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here

    data = np.array(data)
    N = data.shape[0]
    M = data.shape[1]

    result = np.zeros((N, M), dtype=float)

    for j in range(M):
        column = data[:, j]
        col_min = np.min(column)
        col_max = np.max(column)
        col_range = col_max - col_min

        if col_range == 0:
            result[:, j] = 0.0
            continue 
            
        for i in range(N):
            result[i, j] = (data[i, j] - col_min)/col_range

    return result.tolist()