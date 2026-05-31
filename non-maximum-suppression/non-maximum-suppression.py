import numpy as np

def nms(boxes, scores, iou_threshold):
    """
    Apply Non-Maximum Suppression.
    """
    # Write code here
    boxes = np.array(boxes)
    scores = np.array(scores)

    idx = np.argsort(-scores, kind="stable")

    output = []

    while len(idx) > 0:
        i = idx[0]
        output.append(int(i))

        curr_box = boxes[i]
        remain = idx[1:]

        IoUs = []
        for j in remain:
            x1_ = max(curr_box[0], boxes[j,0])
            y1_ = max(curr_box[1], boxes[j,1])
            
            x2_ = min(curr_box[2], boxes[j,2])
            y2_ = min(curr_box[3], boxes[j,3])

            area1 = (
                (curr_box[2] - curr_box[0]) *
                (curr_box[3] - curr_box[1])
            )
            area2 = (
                (boxes[j,2] - boxes[j,0]) *
                (boxes[j,3] - boxes[j,1])
            )

            intersection = max(0, x2_ - x1_) * max(0, y2_ - y1_)
            union = area1 + area2 - intersection
            if union == 0:
                IoU = 0
            else:
                IoU = intersection / union

            IoUs.append(IoU)

        IoUs = np.array(IoUs)
        idx = remain[IoUs < iou_threshold]

    return output
    pass