import numpy as np

def decision_tree_split(X, y):
    """
    Find the best feature and threshold to split the data.
    """
    X = np.array(X)
    y = np.array(y)

    m, n = X.shape
    if m <= 1:
        return 0, 0.0

    def Gini_func(labels):
        if len(labels) == 0:
            return 0.0
            
        _, counts = np.unique(labels, return_counts=True)
        p = counts / len(labels)
        return 1.0 - np.sum(p**2)

    current_gini = Gini_func(y)
    best_gain = -1.0
    best_feature = 0
    best_threshold = 0.0

    for feat in range(n):
        features = X[:, feat]
        unique_values = np.unique(features)

        if len(unique_values) <= 1:
            continue

        sorted_unique = np.sort(unique_values)
        thresholds = (sorted_unique[:-1] + sorted_unique[1:]) / 2.0
        
        for threshold in thresholds:
            left_mask = features <= threshold
            right_mask = ~left_mask
            
            y_left = y[left_mask]
            y_right = y[right_mask]
            
            if len(y_left) == 0 or len(y_right) == 0:
                continue
                
            gini_left = Gini_func(y_left)
            gini_right = Gini_func(y_right)
            
            gini_split = (len(y_left) / m) * gini_left + (len(y_right) / m) * gini_right
            gain = current_gini - gini_split
            
            if gain > best_gain + 1e-9:
                best_gain = gain
                best_feature = feat
                best_threshold = threshold
            elif abs(gain - best_gain) < 1e-9:
                if feat < best_feature:
                    best_gain = gain
                    best_feature = feat
                    best_threshold = threshold
                elif feat == best_feature:
                    if threshold < best_threshold:
                        best_threshold = threshold
                        
    return best_feature, best_threshold
