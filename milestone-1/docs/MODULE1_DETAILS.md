# Module 1: Dataset Setup & Image Preprocessing Pipeline

## Objective
Prepare the PCB dataset for defect analysis by aligning images, computing difference maps, thresholding, and extracting ROIs.

## Steps Completed
1. Dataset Setup & Inspection
   - Templates: 10 defect-free images
   - Test images: 6 defect categories
   - Total images processed: 1,386

2. Image Alignment & Preprocessing
   - ORB feature matching + RANSAC alignment
   - Resizing, normalization
   - Saved aligned images → processed/aligned_images/

3. Image Subtraction
   - Compute absolute difference between test and template → processed/difference_masks/

4. Thresholding
   - Apply Otsu’s method → processed/thresholded_masks/

5. ROI Extraction
   - Detect contours, crop defect regions → processed/defect_rois/

6. Sample Outputs
   - Selected subset → processed/samples/

## Scripts
- 01_align_preprocess.py → Alignment & preprocessing
- 02_image_subtraction.py → Difference computation
- 03_thresholding.py → Otsu thresholding
- 04_roi_extraction.py → Crop ROIs
