import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    if matrix is None:
        return None
        
    matrix = np.array(matrix)
    
    if axis is not None and (axis < 0 or axis >= matrix.ndim):
        return None
    if matrix.ndim != 2:
        return None
        
    abs_matrix = np.abs(matrix)

    if (norm_type == 'l1'):
        division = np.sum(abs_matrix, axis=axis, keepdims=True) 
    elif (norm_type == 'max'):
        division = np.max(abs_matrix, axis=axis, keepdims=True)
    elif (norm_type == 'l2'):
        division = np.sqrt(np.sum(matrix**2, axis=axis, keepdims=True))
    else:
        return None

    division[division==0] = 1
    norm_matrix = matrix / division
    return norm_matrix
    pass