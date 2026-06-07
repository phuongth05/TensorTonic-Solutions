import numpy as np

def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here

    recommendations = [item for row in recommendations for item in row]
    
    unique = np.unique(recommendations)
    

    return len(unique) / n_items