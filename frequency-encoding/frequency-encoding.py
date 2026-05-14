from collections import Counter

def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here

    frequent_dict = Counter(values)

    return [frequent_dict[v] / len(values) for v in values]

    