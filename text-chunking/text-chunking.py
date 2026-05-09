def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here

    step = chunk_size - overlap
    chunks = []
    N = len(tokens)

    for i in range(0, N, step):
        chunk = tokens[i:i + chunk_size]
        chunks.append(chunk)
        if (i + chunk_size >= N):
            break

    return chunks