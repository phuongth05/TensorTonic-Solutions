import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    # Write code here

    Z1 = np.array(Z1)
    Z2 = np.array(Z2)

    similarity_matrix = np.dot(Z1, Z2.T)/temperature

    s_stable = similarity_matrix - np.max(similarity_matrix)

    s_diag = np.diag(s_stable)
    

    loss = - np.mean(np.log(np.exp(s_diag)/np.sum(np.exp(s_stable), axis=1)))

    return loss
    pass