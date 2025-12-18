# PCB Defect Detection and Classification – Milestone 1

## 📌 Objective
Prepare the PCB dataset for defect analysis by aligning images, computing difference maps, thresholding, and extracting ROIs.

---

## ✅ Steps Completed

1. **Dataset Setup & Inspection**
   - Templates: 10 defect-free images
   - Test images: 6 defect categories
   - Total images processed: 1,386

2. **Image Alignment & Preprocessing**
   - ORB feature matching + RANSAC alignment
   - Resizing and normalization
   - Saved aligned images → `processed/aligned_images/`

3. **Image Subtraction**
   - Compute absolute difference between test and template → `processed/difference_masks/`

4. **Thresholding**
   - Apply Otsu’s method → `processed/thresholded_masks/`

5. **ROI Extraction**
   - Detect contours, crop defect regions → `processed/defect_rois/`

6. **Sample Outputs**
   - Selected subset → `processed/samples/`

---

## 🧰 Scripts

| Script | Purpose |
|--------|---------|
| `01_align_preprocess.py` | Alignment & preprocessing |
| `02_image_subtraction.py` | Difference computation |
| `03_thresholding.py` | Otsu thresholding |
| `04_roi_extraction.py` | Crop ROIs |

---

## 🏗 Architecture Overview

1. Template & Test Images → Inspection & organization  
2. Alignment & Preprocessing → ORB + RANSAC feature matching  
3. Image Subtraction → Absolute difference computation  
4. Thresholding → Otsu binary masks  
5. ROI Extraction → Contour detection & crop  
6. Sample Outputs → Aligned images, masks, ROI crops  

---

## ⚡ Quickstart

### Install Dependencies
```bash
pip install -r requirements.txt
Run Module 1 Scripts
python 01_align_preprocess.py
python 02_image_subtraction.py
python 03_thresholding.py
python 04_roi_extraction.py

Check Outputs

Aligned images → processed/aligned_images/

Difference masks → processed/difference_masks/

Thresholded masks → processed/thresholded_masks/

ROI crops → processed/defect_rois/

Sample outputs → processed/samples/

🗂 Folder Structure
PCB_DATASET/
├── PCB_USED/
├── images/
├── Annotations/
├── processed/
│   ├── aligned_images/
│   ├── difference_masks/
│   ├── thresholded_masks/
│   ├── defect_rois/
│   └── samples/
└── docs/

📊 Project Roadmap
Week	Module / Task	Status
1	Dataset setup & preprocessing	✅ Complete
2	ROI extraction & visualization	🔄 In progress
3-4	Deep learning model training	📋 Planned
5-6	Frontend integration (Streamlit)	📋 Planned
7	Optimization & export functionality	📋 Planned
8	Final documentation & presentation	📋 Planned
📈 Dataset Statistics

Templates: 10

Test images: 6 categories

Total processed images: 1,386

Sample ROIs per image: 3–12

🖼 Sample Outputs
Aligned Images

processed/samples/aligned1.jpg
processed/samples/aligned2.jpg

Difference Masks

processed/samples/diff1.jpg
processed/samples/diff2.jpg

Thresholded Masks

processed/samples/thresh1.jpg
processed/samples/thresh2.jpg

ROI Crops

processed/samples/roi1.png
processed/samples/roi2.png

📊 Metrics

Alignment success: 100%

Processing speed: ~0.5s per image

Defects extracted: 3–12 per test image

📦 Deliverables

Dataset setup & inspection ✅

Alignment & preprocessing ✅

Image subtraction & difference masks ✅

Thresholding ✅

ROI extraction ✅

Sample outputs ✅

👤 Author

Akalya S
PCB Defect Detection & Classification Project
