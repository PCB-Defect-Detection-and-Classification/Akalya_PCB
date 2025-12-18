import numpy as np

def load_defect_model():
    print("Model loaded (placeholder)")
    return None

def run_inspection(template_img, test_img, model, confidence_thresh=50):
    aligned_img = test_img.copy()
    annotated_img = test_img.copy()
    defects = [
        {"type": "Missing Hole", "confidence": 95},
        {"type": "Short", "confidence": 87}
    ]
    return aligned_img, annotated_img, defects
