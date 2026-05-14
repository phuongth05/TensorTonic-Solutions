import numpy as np
def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    pass
    box_a = np.array(box_a)
    box_b = np.array(box_b)

    if (box_b[0] > box_a[2] and box_b[1] > box_a[3]):
        return 0.0
    if (box_a[0] > box_b[2] and box_a[1] > box_b[3]):
        return 0.0

    point_1 = max(box_a[0], box_b[0])
    point_2 = max(box_a[1], box_b[1])
    point_3 = min(box_a[2], box_b[2])
    point_4 = min(box_a[3], box_b[3])

    intersection = np.abs((point_3 - point_1) * (point_4 - point_2))

    area_a = np.abs((box_a[2] - box_a[0]) * (box_a[3] - box_a[1]))
    area_b = np.abs((box_b[2] - box_b[0]) * (box_b[3] - box_b[1]))

    union = area_a + area_b - intersection

    return float(intersection/union)

    
