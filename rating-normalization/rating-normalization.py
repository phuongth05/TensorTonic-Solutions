import numpy as np

def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    # Write code here

    matrix = np.array(matrix, dtype=float)
    rows, columns = matrix.shape

    output = np.zeros_like(matrix)

    for row in range(rows):
        n_count = len(np.where(matrix[row] > 0)[0])
        if n_count == 0:
            output[row, :] = 0.0
            continue
        r_mean = 1/n_count * np.sum(matrix[row])

        for col in range(columns):
            if matrix[row, col] == 0:
                output[row, col] = 0
                continue
    
            output[row, col] = matrix[row, col] - r_mean

    return output.tolist()