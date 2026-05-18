import math
import numpy as np

def roi_pool(feature_map, rois, output_size):
    """
    Apply ROI Pooling to extract fixed-size features.
    """
    # Write code here
    
    output = np.zeros((len(rois), output_size, output_size), dtype=int)
    feature_map = np.array(feature_map)
    
    for k in range(len(rois)):
        x1 = rois[k][0]
        y1 = rois[k][1]
        x2 = rois[k][2]
        y2 = rois[k][3]
        
        for i in range(output_size):
            for j in range(output_size):
                h_s = y1 + (int)((i * (y2 - y1)) / output_size)
                h_e = y1 + (int)(((i + 1) * (y2 - y1)) / output_size)
                w_s = x1 + (int)((j * (x2 - x1)) / output_size)
                w_e = x1 + (int)(((j + 1) * (x2 - x1)) / output_size)

                if h_s == h_e:
                    h_e += 1
                if w_s == w_e:
                    w_e += 1
                    
                max_val = np.max(feature_map[h_s:h_e, w_s:w_e])
                output[k, i, j] = max_val

    return output.tolist()
    pass