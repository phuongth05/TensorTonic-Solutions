import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    # tp: 1 = 1
    #fp: pred 1 true 0
    # fn: pred 0 true 1
    # tn: 0 = 0

    TP = 0
    FP = 0
    FN = 0
    TN = 0

    uniques = np.unique([y_pred, y_true])

    for unique in uniques:
        for true, pred in zip(y_true, y_pred):
            if pred == unique:
                if true == unique:
                    TP += 1
                elif true != unique:
                    FP += 1
            elif pred != unique:
                if true == unique:
                    FN += 1
                elif true != unique:
                    TN += 1

    return (2.0 * TP) / (2*TP + FP + FN)
    pass