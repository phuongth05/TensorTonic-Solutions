import numpy as np

def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here

    values = np.array(values)
    n = len(values)

    ord = np.argsort(values)
    rank = np.zeros(n, dtype=float)

    i = 0
    while i < n:
        j = i

        while j + 1 < n and values[ord[j + 1]] == values[ord[i]]:
            j += 1

        avg_rank = (i + 1 + j + 1) / 2.0

        for k in range(i, j + 1):
            rank[ord[k]] = avg_rank

        i = j + 1

    return rank.tolist()
    

    