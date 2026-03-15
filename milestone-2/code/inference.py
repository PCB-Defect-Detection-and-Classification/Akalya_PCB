import os
import cv2
import numpy as np
import tensorflow as tf
import glob
from tensorflow.keras.preprocessing.image import ImageDataGenerator

MODEL_PATH = "/content/drive/MyDrive/pcb_defect_model.keras"
DATA_DIR = "/content/drive/MyDrive/PCB_Training_Dataset_Split/val"
OUTPUT_DIR = "/content/drive/MyDrive/Annotated_Test_Images"
IMG_SIZE = (128, 128)

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load model
model = tf.keras.models.load_model(MODEL_PATH)

# Get class names in the same order as training
data_gen = ImageDataGenerator(rescale=1./255)
temp_ds = data_gen.flow_from_directory(
    DATA_DIR,
    target_size=IMG_SIZE,
    batch_size=1,
    class_mode='sparse',
    shuffle=False
)
class_names = list(temp_ds.class_indices.keys())

for class_name in class_names:
    folder_path = os.path.join(DATA_DIR, class_name)
    images = glob.glob(os.path.join(folder_path, "*.jpg")) + glob.glob(os.path.join(folder_path, "*.png")) + glob.glob(os.path.join(folder_path, "*.jpeg"))
    
    if not images:
        continue

    img_path = images[0]  # first image from each class
    img = cv2.imread(img_path)

    if img is None:
        print(f"Could not read image: {img_path}")
        continue

    # Convert BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize and normalize
    img_resized = cv2.resize(img_rgb, IMG_SIZE)
    img_resized = img_resized.astype("float32") / 255.0
    img_batch = np.expand_dims(img_resized, axis=0)

    # Predict
    preds = model.predict(img_batch, verbose=0)
    pred_idx = np.argmax(preds)
    pred_label = class_names[pred_idx]
    score = np.max(preds) * 100

    # Annotate original image
    color = (0, 255, 0) if pred_label == class_name else (0, 0, 255)
    text = f"True: {class_name} | Pred: {pred_label} ({score:.1f}%)"
    cv2.putText(img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    save_path = os.path.join(OUTPUT_DIR, f"Pred_{class_name}.png")
    cv2.imwrite(save_path, img)
    print(f"Saved annotated image: {save_path}")
