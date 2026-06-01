import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    # Write code here
    label = np.unique(np.concatenate([y_pred, y_true]))
    classes = len(label)
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    cm = np.zeros((classes, classes), dtype=int)

    for i in label:
        for j in label:
            cm[i, j] = np.sum((y_true == i) & (y_pred==j))

    class_metric = []
    for i in label:
        if average == "binary":
            if i != pos_label:
                continue
                
        TP = cm[i, i]
        FN = np.sum(cm[i, :]) - cm[i, i]
        FP = np.sum(cm[:, i]) - cm[i, i]

        precision = TP / (TP + FP) if TP + FP > 0 else 0
        recall = TP / (TP + FN) if TP + FN > 0 else 0

        if average == "binary":
            return {
                "accuracy" : (np.trace(cm) / np.sum(cm)),
                "precision" : precision,
                "recall" : recall,
                "f1" : (2*precision*recall)/(precision+recall)
            }

        class_metric.append([TP, FP, FN])
        
    class_metric = np.array(class_metric)
    
    if average == "micro":
        TP = np.sum(class_metric[:, 0])
        FP = np.sum(class_metric[:, 1])
        FN = np.sum(class_metric[:, 2])

        precision = TP / (TP + FP) if TP + FP > 0 else 0
        recall = TP / (TP + FN) if TP + FN > 0 else 0
        return {
            "accuracy" : (np.trace(cm) / np.sum(cm)),
            "precision" : precision,
            "recall" : recall,
            "f1" : (2 * precision * recall) / (precision + recall)
        }
        
    elif average == "macro":
        TP = class_metric[:, 0]
        FP = class_metric[:, 1]
        FN = class_metric[:, 2]
    
        accuracy = np.trace(cm) / np.sum(cm)
    
        precision_per_class = np.divide(
            TP,
            TP + FP,
            out=np.zeros_like(TP, dtype=float),
            where=(TP + FP) != 0
        )
    
        recall_per_class = np.divide(
            TP,
            TP + FN,
            out=np.zeros_like(TP, dtype=float),
            where=(TP + FN) != 0
        )
    
        f1_per_class = np.divide(
            2 * precision_per_class * recall_per_class,
            precision_per_class + recall_per_class,
            out=np.zeros_like(precision_per_class, dtype=float),
            where=(precision_per_class + recall_per_class) != 0
        )
    
        precision = np.mean(precision_per_class)
        recall = np.mean(recall_per_class)
        f1 = np.mean(f1_per_class)
    
        return {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1
        }

    elif average == "weighted":
        support = class_metric[:, 0] + class_metric[:, 2]
        weights = support/np.sum(support)

        TP = class_metric[:, 0]
        FP = class_metric[:, 1]
        FN = class_metric[:, 2]
        accuracy = np.trace(cm)/np.sum(cm)
        precision = np.divide(
            TP,
            TP + FP,
            out=np.zeros_like(TP, dtype=float),
            where=(TP + FP) != 0
        )
        
        recall = np.divide(
            TP,
            TP + FN,
            out=np.zeros_like(TP, dtype=float),
            where=(TP + FN) != 0
        )
        
        f1 = np.divide(
            2 * precision * recall,
            precision + recall,
            out=np.zeros_like(precision, dtype=float),
            where=(precision + recall) != 0
        )

        precision_ = np.sum(weights * precision)
        recall_ = np.sum(weights * recall)
        f1_ = np.sum(weights * f1)

        return {
            "accuracy" : accuracy,
            "precision" : precision_,
            "recall" : recall_,
            "f1" : f1_
        }
    else:
        return None                      
    pass
