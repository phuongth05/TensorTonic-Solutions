def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here

    order_dict = {v: i for i, v in enumerate(ordering)}

    return [order_dict[v] for v in values]

    