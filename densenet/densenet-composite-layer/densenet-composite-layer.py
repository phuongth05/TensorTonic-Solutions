import torch
import torch.nn.functional as F

def composite_layer(x: torch.Tensor, bn_gamma: torch.Tensor, bn_beta: torch.Tensor,
                    bn_mean: torch.Tensor, bn_var: torch.Tensor,
                    conv_weight: torch.Tensor, eps: float = 1e-5) -> torch.Tensor:
    """
    Returns the float64 output of the DenseNet composite transformation.
    """

    bn_gamma = bn_gamma.view(1, -1, 1, 1)
    bn_beta = bn_beta.view(1, -1, 1, 1)
    bn_mean = bn_mean.view(1, -1, 1, 1)
    bn_var = bn_var.view(1, -1, 1, 1)

    x = (x - bn_mean)/torch.sqrt(bn_var + eps)
    x = x * bn_gamma + bn_beta

    x = F.relu(x)

    x = F.conv2d(x, conv_weight, padding=1, bias=None)

    return x.to(torch.float64)
    pass