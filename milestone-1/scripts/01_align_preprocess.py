import cv2
import os

template_path = "PCB_DATASET/PCB_DATASET/PCB_USED"
test_base_path = "PCB_DATASET/PCB_DATASET/images"
aligned_path = "PCB_DATASET/PCB_DATASET/processed/aligned_images"

os.makedirs(aligned_path, exist_ok=True)

valid_exts = (".png", ".jpg", ".jpeg", ".bmp")

templates = sorted([f for f in os.listdir(template_path) if f.lower().endswith(valid_exts)])

if not templates:
    raise FileNotFoundError(f"No template images found in {template_path}")

template_img = cv2.imread(os.path.join(template_path, templates[0]), 0)
if template_img is None:
    raise ValueError(f"Could not read template image: {templates[0]}")

template_img = cv2.resize(template_img, (640, 640))

for defect_type in os.listdir(test_base_path):
    defect_folder = os.path.join(test_base_path, defect_type)

    if not os.path.isdir(defect_folder):
        continue

    for test_img_file in os.listdir(defect_folder):
        if not test_img_file.lower().endswith(valid_exts):
            continue

        test_img_path = os.path.join(defect_folder, test_img_file)
        test_img = cv2.imread(test_img_path, 0)

        if test_img is None:
            print(f"Skipping unreadable file: {test_img_path}")
            continue

        test_img = cv2.resize(test_img, (640, 640))

        cv2.imwrite(os.path.join(aligned_path, f"template_{templates[0]}"), template_img)
        cv2.imwrite(os.path.join(aligned_path, f"test_{test_img_file}"), test_img)

print("Alignment & Preprocessing Done!")
