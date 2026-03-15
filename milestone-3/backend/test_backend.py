import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from backend import backend, config

# --- Paths ---
TEMPLATE_DIR = os.path.join(config.SAMPLE_IMAGES_DIR, "template")
TEST_DIR = os.path.join(config.SAMPLE_IMAGES_DIR, "test")

# --- Pick first image from each folder ---
template_img_path = os.path.join(TEMPLATE_DIR, os.listdir(TEMPLATE_DIR)[0])
test_img_path = os.path.join(TEST_DIR, os.listdir(TEST_DIR)[0])

# --- Load images ---
template_img = cv2.imread(template_img_path)
test_img = cv2.imread(test_img_path)

# OpenCV loads in BGR, convert to RGB
template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2RGB)
test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)

# --- Load model ---
model = backend.load_defect_model()

# --- Run inspection ---
aligned, annotated, defects = backend.run_inspection(template_img, test_img, model, confidence_thresh=50)

# --- Print defects ---
print("Detected Defects:", defects)

# --- Visualize results ---
plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.title("Template Image")
plt.imshow(template_img)
plt.axis("off")

plt.subplot(1,3,2)
plt.title("Aligned Test Image")
plt.imshow(aligned)
plt.axis("off")

plt.subplot(1,3,3)
plt.title("Annotated Output")
plt.imshow(annotated)
plt.axis("off")

plt.show()
