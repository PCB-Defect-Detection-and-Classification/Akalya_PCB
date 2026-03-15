import cv2
import numpy as np
import tensorflow as tf
import os

# ---- LABEL MAP ----
CLASS_NAMES = [
    "Missing Hole",
    "Mouse Bite",
    "Open Circuit",
    "Short",
    "Spur",
    "Spurious Copper"
]

IMG_SIZE = (128, 128)

# ---- MODEL LOADER ----
def load_model(model_path):
    """
    Loads the TensorFlow/Keras model from given path
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    return tf.keras.models.load_model(model_path)

# ---- MAIN INSPECTION FUNCTION ----
def inspect_pcb(image, model, confidence_thresh=85, patch_size=128, stride=64):
    h, w, _ = image.shape
    annotated = image.copy()
    defects = []

    for y in range(0, h - patch_size + 1, stride):
        for x in range(0, w - patch_size + 1, stride):
            patch = image[y:y + patch_size, x:x + patch_size]

            gray = cv2.cvtColor(patch, cv2.COLOR_RGB2GRAY)
            if np.std(gray) < 15:
                continue

            patch_resized = cv2.resize(patch, IMG_SIZE)
            patch_norm = patch_resized.astype(np.float32) / 255.0
            patch_input = np.expand_dims(patch_norm, axis=0)

            preds = model.predict(patch_input, verbose=0)[0]
            conf = float(np.max(preds) * 100)
            label = CLASS_NAMES[int(np.argmax(preds))]

            if conf >= confidence_thresh:
                cv2.rectangle(annotated, (x, y), (x + patch_size, y + patch_size), (0,0,255), 2)
                cv2.putText(
                    annotated, f"{label} {int(conf)}%", (x, max(y-5, 15)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1
                )
                defects.append({
                    "type": label,
                    "confidence": round(conf,2),
                    "bbox":[x, y, x + patch_size, y + patch_size]
                })

    return annotated, defects
