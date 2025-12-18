import cv2
import os

mask_path = "PCB_DATASET/PCB_DATASET/processed/thresholded_masks"
roi_path = "PCB_DATASET/PCB_DATASET/processed/defect_rois"
os.makedirs(roi_path, exist_ok=True)

for mask_file in os.listdir(mask_path):
    mask = cv2.imread(os.path.join(mask_path, mask_file), 0)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for i, cnt in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cnt)
        roi = mask[y:y+h, x:x+w]
        cv2.imwrite(os.path.join(roi_path, f"{mask_file}_roi_{i}.png"), roi)

print("ROI extraction complete!")
