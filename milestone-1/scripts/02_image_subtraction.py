import cv2
import os

aligned_path = "PCB_DATASET/PCB_DATASET/processed/aligned_images"
diff_path = "PCB_DATASET/PCB_DATASET/processed/difference_masks"

os.makedirs(diff_path, exist_ok=True)

valid_exts = (".png", ".jpg", ".jpeg", ".bmp")
aligned_files = sorted([f for f in os.listdir(aligned_path) if f.lower().endswith(valid_exts)])

template_files = [f for f in aligned_files if f.startswith("template_")]
if not template_files:
    raise FileNotFoundError("No template image found in aligned_images folder")

template_file = template_files[0]
template = cv2.imread(os.path.join(aligned_path, template_file), 0)

if template is None:
    raise ValueError(f"Could not read template image: {template_file}")

for test_file in aligned_files:
    if test_file.startswith("test_"):
        test_img = cv2.imread(os.path.join(aligned_path, test_file), 0)

        if test_img is None:
            print(f"Skipping unreadable file: {test_file}")
            continue

        diff = cv2.absdiff(test_img, template)
        cv2.imwrite(os.path.join(diff_path, f"diff_{test_file}"), diff)

print("Image subtraction complete!")
