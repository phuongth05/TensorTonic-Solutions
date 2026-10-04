import torch
import torch.nn.functional as F

def sgns_loss(center_vec: torch.Tensor, pos_vec: torch.Tensor,
              neg_vecs: torch.Tensor) -> torch.Tensor:
    """
    Returns the scalar float64 SGNS loss.
    """

    pos_score = torch.dot(center_vec, pos_vec)

    neg_scores = neg_vecs @ center_vec

    loss = -F.logsigmoid(pos_score) - torch.sum(F.logsigmoid(- neg_scores))

    return loss.to(torch.float64)
    pass