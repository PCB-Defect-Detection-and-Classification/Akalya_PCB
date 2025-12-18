
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from backend.backend import load_defect_model, run_inspection

# Paths
TEMPLATE_DIR = "/content/Akalya_PCB/milestone-3/sample_images/template"
TEST_DIR = "/content/Akalya_PCB/milestone-3/sample_images/test"

# Pick one image from each folder
template_img_path = os.path.join(TEMPLATE_DIR, os.listdir(TEMPLATE_DIR)[0])
test_img_path = os.path.join(TEST_DIR, os.listdir(TEST_DIR)[0])

# Load images
template_img = cv2.imread(template_img_path)
test_img = cv2.imread(test_img_path)

template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2RGB)
test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)

# Load model (placeholder or real)
model = load_defect_model()

# Run inspection
aligned, annotated, defects = run_inspection(
    template_img,
    test_img,
    model,
    confidence_thresh=50
)

print("Detected Defects:", defects)

# Visualize results
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
