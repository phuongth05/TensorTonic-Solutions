def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here

    count_dict = {}
    sum_dict = {}
    mean_dict = {}

    for category, target in zip(categories, targets):
        count_dict[category] = count_dict.get(category, 0) + 1
        sum_dict[category] = sum_dict.get(category, 0) + target
        mean_dict[category] = sum_dict[category] / count_dict[category]

    return [mean_dict[category] for category in categories]