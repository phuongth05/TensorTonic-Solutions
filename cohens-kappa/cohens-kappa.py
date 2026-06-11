import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    n = len(rater1)

    uniques = np.unique((rater1, rater2))

    agreements = 0

    for rater_1, rater_2 in zip(rater1, rater2):
        for unique in uniques:
            if rater_1 == unique and rater_2 == unique:
                agreements += 1
    p_o = agreements / n
    p_e = 0
    for unique in uniques:
        p_e += np.sum(rater1 == unique)/n * np.sum(rater2 == unique)/n
    
      
    
    return (p_o - p_e) / (1 - p_e)  if p_e != 1 else 1.0
    pass