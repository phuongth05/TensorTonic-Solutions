import numpy as np

def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    reference_counts = np.array(reference_counts)
    production_counts = np.array(production_counts)

    reference_counts = reference_counts/np.sum(reference_counts)
    production_counts = production_counts/np.sum(production_counts)

    TVD = (0.5 * np.sum([np.abs(p - q) for p, q in zip(reference_counts, production_counts)])).item()
    drift = True if (TVD > threshold) else False
    return {
        "score" : TVD,
        "drift_detected" : drift
    }
    
    pass