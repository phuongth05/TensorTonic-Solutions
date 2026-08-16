import numpy as np

def softmax(x, axis=-1):
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e_x / np.sum(e_x, axis=axis, keepdims=True)

def multi_head_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray,
                         W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray,
                         W_o: np.ndarray, num_heads: int) -> np.ndarray:
    """
    Compute multi-head attention.
    """
    # Your code here

    Q_proq = np.dot(Q, W_q)
    K_proq = np.dot(K, W_k)
    V_proq = np.dot(V, W_v)

    batch, seq, d_model = Q_proq.shape
    d_k = d_model // num_heads

    Q_proq = Q_proq.reshape(batch, seq, num_heads, d_k).transpose(0, 2, 1, 3)
    K_proq = K_proq.reshape(batch, seq, num_heads, d_k).transpose(0, 2, 1, 3)
    V_proq = V_proq.reshape(batch, seq, num_heads, d_k).transpose(0, 2, 1, 3)

    
    Attention = softmax(np.matmul(Q_proq, K_proq.transpose(0, 1, 3, 2))/np.sqrt(d_k), axis=-1) @ V_proq

    return np.dot(Attention.transpose(0, 2, 1, 3).reshape(batch, seq, d_model), W_o)
    pass