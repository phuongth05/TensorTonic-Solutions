def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here

    word_count_dict = {}

    for sentence in sentences:
        for word in sentence:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1

    return word_count_dict
    pass