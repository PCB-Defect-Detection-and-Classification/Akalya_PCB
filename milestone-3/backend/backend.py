import os
import cv2
import numpy as np
import tensorflow as tf
from . import config

IMG_SIZE = (128, 128)

# IMPORTANT:
# Replace this order with the exact output of print(train_ds.class_indices)
# Example only:
CLASS_NAMES = [
    "missing_hole",
    "mouse_bite",
    "open_circuit",
    "short",
    "spur",
    "spurious_copper"
]

def load_defect_model():
    if not os.path.exists(config.MODEL_PATH):
        raise FileNotFoundError(f"Model file not found: {config.MODEL_PATH}")
    model = tf.keras.models.load_model(config.MODEL_PATH)
    return model

def preprocess_image(img):
    # Handle empty ROI safely
    if img is None or img.size == 0:
        return None

    # Convert BGR to RGB because OpenCV reads BGR,
    # but training images were loaded as RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img, IMG_SIZE)
    img_resized = img_resized.astype("float32") / 255.0
    img_batch = np.expand_dims(img_resized, axis=0)
    return img_batch

def run_inspection(template_img, test_img, model, confidence_thresh=50):
    if template_img is None or test_img is None:
        raise ValueError("Template image or test image is None")

    # Keep copies
    aligned_img = test_img.copy()
    annotated_img = test_img.copy()
    defects = []

    # Resize both images to same size
    h, w = test_img.shape[:2]
    template_resized = cv2.resize(template_img, (w, h))

    # Convert to grayscale for comparison
    template_gray = cv2.cvtColor(template_resized, cv2.COLOR_BGR2GRAY)
    test_gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    # Difference
    diff = cv2.absdiff(test_gray, template_gray)

    # Blur to reduce noise
    diff = cv2.GaussianBlur(diff, (5, 5), 0)

    # Threshold
    _, thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Morphological cleanup
    kernel = np.ones((3, 3), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    thresh = cv2.dilate(thresh, kernel, iterations=1)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        # Ignore very tiny regions/noise
        if area < 20:
            continue

        x, y, bw, bh = cv2.boundingRect(cnt)

        # Add a small padding around ROI
        pad = 8
        x1 = max(0, x - pad)
        y1 = max(0, y - pad)
        x2 = min(test_img.shape[1], x + bw + pad)
        y2 = min(test_img.shape[0], y + bh + pad)

        roi = test_img[y1:y2, x1:x2]

        img_batch = preprocess_image(roi)
        if img_batch is None:
            continue

        preds = model.predict(img_batch, verbose=0)[0]
        pred_idx = int(np.argmax(preds))
        confidence = float(np.max(preds) * 100)

        if pred_idx < 0 or pred_idx >= len(CLASS_NAMES):
            pred_label = "unknown"
        else:
            pred_label = CLASS_NAMES[pred_idx]

        if confidence >= confidence_thresh:
            defects.append({
                "type": pred_label,
                "confidence": confidence,
                "bbox": [int(x1), int(y1), int(x2), int(y2)]
            })

            # Draw bounding box
            cv2.rectangle(annotated_img, (x1, y1), (x2, y2), (0, 0, 255), 2)

            # Draw label
            text = f"{pred_label} ({confidence:.1f}%)"
            text_y = y1 - 10 if y1 - 10 > 10 else y1 + 20
            cv2.putText(
                annotated_img,
                text,
                (x1, text_y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2
            )

    # If no contours found or no ROI crossed confidence threshold
    if len(defects) == 0:
        cv2.putText(
            annotated_img,
            "No defect detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    return aligned_img, annotated_img, defects
