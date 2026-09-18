import numpy as np

def bert_embeddings(token_ids: np.ndarray, segment_ids: np.ndarray,
                    token_embeddings: np.ndarray, position_embeddings: np.ndarray,
                    segment_embeddings: np.ndarray) -> np.ndarray:
    """
    Retcurns the float64 BERT input embeddings with shape (B, S, H).
    """
    tokens = token_embeddings[token_ids]
    segment = segment_embeddings[segment_ids]

    positions = np.arange(token_ids.shape[1])
    position = position_embeddings[positions]

    return tokens + segment + position
    
    pass