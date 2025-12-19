
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
    if not os.path.exists(model_path):
        raise FileNotFoundError("❌ Model file not found")
    return tf.keras.models.load_model(model_path)


# ---- MAIN INSPECTION FUNCTION ----
def inspect_pcb(image, model, confidence_thresh=50):

    h, w, _ = image.shape
    annotated = image.copy()
    defects = []

    patch_size = 128
    stride = 64

    for y in range(0, h - patch_size, stride):
        for x in range(0, w - patch_size, stride):

            patch = image[y:y+patch_size, x:x+patch_size]
            patch_resized = cv2.resize(patch, IMG_SIZE)
            patch_norm = patch_resized / 255.0
            patch_input = np.expand_dims(patch_norm, axis=0)

            preds = model.predict(patch_input, verbose=0)
            conf = np.max(preds) * 100
            label_id = np.argmax(preds)
            label = CLASS_NAMES[label_id]

            if conf >= confidence_thresh:
                cv2.rectangle(
                    annotated,
                    (x, y),
                    (x + patch_size, y + patch_size),
                    (0, 0, 255),
                    2
                )
                cv2.putText(
                    annotated,
                    f"{label} {int(conf)}%",
                    (x, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.4,
                    (0, 0, 255),
                    1
                )

                defects.append({
                    "type": label,
                    "confidence": round(conf, 2),
                    "bbox": [x, y, x + patch_size, y + patch_size]
                })

    return annotated, defects
