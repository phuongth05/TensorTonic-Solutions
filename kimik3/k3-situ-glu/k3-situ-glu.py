import torch

def situ_glu(input_tensor: torch.Tensor, gate_projection: torch.Tensor, up_projection: torch.Tensor, gate_cap: float = 4.0, up_cap: float = 25.0) -> torch.Tensor:
    """
    Returns the bounded element-wise gated activation tensor.
    """

    gate = input_tensor @ gate_projection.T
    up = input_tensor @ up_projection.T

    capped_gate = gate_cap * torch.tanh(gate / gate_cap)
    capped_up = up_cap * torch.tanh(up / up_cap)

    return capped_gate * torch.sigmoid(gate) * capped_up
    pass