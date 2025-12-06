import cv2
import os

# Paths
template_path = "PCB_DATASET/PCB_DATASET/PCB_USED"
test_base_path = "PCB_DATASET/PCB_DATASET/images"
aligned_path = "PCB_DATASET/PCB_DATASET/processed/aligned_images"
os.makedirs(aligned_path, exist_ok=True)

templates = sorted(os.listdir(template_path))
template_imgs = [cv2.imread(os.path.join(template_path, t), 0) for t in templates]

for defect_type in os.listdir(test_base_path):
    defect_folder = os.path.join(test_base_path, defect_type)
    for test_img_file in os.listdir(defect_folder):
        test_img_path = os.path.join(defect_folder, test_img_file)
        test_img = cv2.imread(test_img_path, 0)
        
        template = cv2.resize(template_imgs[0], (640, 640))
        test_img = cv2.resize(test_img, (640, 640))
        
        cv2.imwrite(os.path.join(aligned_path, f"template_{templates[0]}"), template)
        cv2.imwrite(os.path.join(aligned_path, f"test_{test_img_file}"), test_img)

# You can include subtraction, thresholding, and ROI extraction in separate scripts similarly
