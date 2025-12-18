# PCB Defect Detection Project Documentation

## Architecture Overview
1. Template & Test Images → Inspection & organization
2. Alignment & Preprocessing → ORB + RANSAC feature matching
3. Image Subtraction → Absolute difference computation
4. Thresholding → Otsu binary masks
5. ROI Extraction → Contour detection & crop
6. Sample Outputs → Aligned images, masks, ROI crops

## Quickstart
### Install Dependencies
`pip install -r requirements.txt`

### Run Module 1 Scripts
`python 01_align_preprocess.py`
`python 02_image_subtraction.py`
`python 03_thresholding.py`
`python 04_roi_extraction.py`

### Check Outputs
- Aligned images → processed/aligned_images/
- Difference masks → processed/difference_masks/
- Thresholded masks → processed/thresholded_masks/
- ROI crops → processed/defect_rois/
- Sample outputs → processed/samples/

## Project Roadmap
| Week | Module / Task                       | Status           |
|------|-----------------------------------|----------------|
| 1    | Dataset setup & preprocessing       | ✅ Complete     |
| 2    | ROI extraction & visualization      | 🔄 In progress |
| 3-4  | Deep learning model training        | 📋 Planned     |
| 5-6  | Frontend integration (Streamlit)   | 📋 Planned     |
| 7    | Optimization & export functionality | 📋 Planned     |
| 8    | Final documentation & presentation  | 📋 Planned     |
