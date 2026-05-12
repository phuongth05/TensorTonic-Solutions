import numpy as np

def naive_bayes_bernoulli(X_train, y_train, X_test):
    """
    Compute log-likelihood P(y|x) for Bernoulli Naive Bayes.
    """
    # Write code here

    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = np.array(X_test)
    alpha = 1

    result = []

    classes = np.unique(y_train)

    for x in X_test:
        scores = []

        for cls in classes:
            X_c = X_train[y_train == cls]

            prior = np.log(len(X_c) / len(X_train))

            probs =  (np.sum(X_c, axis=0) + 1)/(len(X_c) + 2)

            likelihood = np.sum(x*np.log(probs) + (1-x)*np.log(1- probs))

            scores.append(prior + likelihood)

        result.append(scores)

    return result
    pass