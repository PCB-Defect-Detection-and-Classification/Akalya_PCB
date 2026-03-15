import cv2
import os

diff_path = "PCB_DATASET/PCB_DATASET/processed/difference_masks"
threshold_path = "PCB_DATASET/PCB_DATASET/processed/thresholded_masks"

os.makedirs(threshold_path, exist_ok=True)

valid_exts = (".png", ".jpg", ".jpeg", ".bmp")
diff_files = sorted([f for f in os.listdir(diff_path) if f.lower().endswith(valid_exts)])

for file in diff_files:
    img_path = os.path.join(diff_path, file)
    img = cv2.imread(img_path, 0)

    if img is None:
        print(f"Skipping unreadable file: {img_path}")
        continue

    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite(os.path.join(threshold_path, f"thresh_{file}"), thresh)

print("Thresholding complete!")
