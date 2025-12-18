import cv2
import os

diff_path = "PCB_DATASET/PCB_DATASET/processed/difference_masks"
threshold_path = "PCB_DATASET/PCB_DATASET/processed/thresholded_masks"
os.makedirs(threshold_path, exist_ok=True)

diff_files = sorted(os.listdir(diff_path))

for file in diff_files:
    img = cv2.imread(os.path.join(diff_path, file), 0)
    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite(os.path.join(threshold_path, f"thresh_{file}"), thresh)

print("Thresholding complete!")
