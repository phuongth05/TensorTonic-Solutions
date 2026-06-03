import numpy as np

def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    N = len(actual_tokens)
    H = []

    for i in range(N):
        H.append(prob_distributions[i][actual_tokens[i]])

    PP = np.exp(-1.0/N * np.sum(np.log(H)))

    return PP