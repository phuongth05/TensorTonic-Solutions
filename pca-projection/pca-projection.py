import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    # Write code here

    X = np.array(X)

    means = np.mean(X, axis=0)
    
    X_c = X - means

    C = (X_c.T @ X_c) / (X.shape[0]-1)

    eigenvalues, eigenvectors = np.linalg.eigh(C)

    # np.argsort can only provide lowest to highest; use [::-1] to reverse the list
    order_of_importance = np.argsort(eigenvalues)[::-1] 
    
    # utilize the sort order to sort eigenvalues and eigenvectors
    sorted_eigenvalues = eigenvalues[order_of_importance]
    sorted_eigenvectors = eigenvectors[:,order_of_importance] # sort the columns

    W = sorted_eigenvectors[:, :k]

    X_pca = X_c @ W

    return X_pca

    