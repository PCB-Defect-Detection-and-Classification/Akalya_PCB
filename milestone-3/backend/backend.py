import os
import cv2
import numpy as np
import tensorflow as tf
from . import config

IMG_SIZE = (128, 128)

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
    img_resized = cv2.resize(img, IMG_SIZE)
    img_resized = img_resized.astype("float32") / 255.0
    img_batch = np.expand_dims(img_resized, axis=0)
    return img_batch

def run_inspection(template_img, test_img, model, confidence_thresh=50):
    aligned_img = test_img.copy()
    annotated_img = test_img.copy()

    # preprocess
    img_batch = preprocess_image(test_img)

    # prediction
    preds = model.predict(img_batch, verbose=0)[0]
    pred_idx = int(np.argmax(preds))
    pred_label = CLASS_NAMES[pred_idx]
    confidence = float(np.max(preds) * 100)

    defects = []

    # if confidence passes threshold, show as detected defect
    if confidence >= confidence_thresh:
        defects.append({
            "type": pred_label,
            "confidence": confidence
        })

        # simple annotation
        text = f"{pred_label} ({confidence:.1f}%)"
        cv2.putText(
            annotated_img,
            text,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        cv2.rectangle(
            annotated_img,
            (10, 10),
            (annotated_img.shape[1] - 10, annotated_img.shape[0] - 10),
            (255, 0, 0),
            3
        )

    return aligned_img, annotated_img, defects
