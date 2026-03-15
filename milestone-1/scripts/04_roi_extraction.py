import cv2
import os

mask_path = "PCB_DATASET/PCB_DATASET/processed/thresholded_masks"
roi_path = "PCB_DATASET/PCB_DATASET/processed/defect_rois"

os.makedirs(roi_path, exist_ok=True)

valid_exts = (".png", ".jpg", ".jpeg", ".bmp")

for mask_file in os.listdir(mask_path):
    if not mask_file.lower().endswith(valid_exts):
        continue

    mask_file_path = os.path.join(mask_path, mask_file)
    mask = cv2.imread(mask_file_path, 0)

    if mask is None:
        print(f"Skipping unreadable file: {mask_file_path}")
        continue

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    roi_count = 0
    for i, cnt in enumerate(contours):
        if cv2.contourArea(cnt) < 20:
            continue

        x, y, w, h = cv2.boundingRect(cnt)
        roi = mask[y:y+h, x:x+w]

        roi_filename = f"{os.path.splitext(mask_file)[0]}_roi_{roi_count}.png"
        cv2.imwrite(os.path.join(roi_path, roi_filename), roi)
        roi_count += 1

print("ROI extraction complete!")
