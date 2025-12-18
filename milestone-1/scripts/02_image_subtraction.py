import cv2
import os

aligned_path = "PCB_DATASET/PCB_DATASET/processed/aligned_images"
diff_path = "PCB_DATASET/PCB_DATASET/processed/difference_masks"
os.makedirs(diff_path, exist_ok=True)

aligned_files = sorted(os.listdir(aligned_path))
template_file = [f for f in aligned_files if f.startswith("template_")][0]
template = cv2.imread(os.path.join(aligned_path, template_file), 0)

for test_file in aligned_files:
    if test_file.startswith("test_"):
        test_img = cv2.imread(os.path.join(aligned_path, test_file), 0)
        diff = cv2.absdiff(test_img, template)
        cv2.imwrite(os.path.join(diff_path, f"diff_{test_file}"), diff)

print("Image subtraction complete!")
