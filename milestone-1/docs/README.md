# PCB Defect Detection and Classification System

An automated deep learning system for detecting and classifying defects in Printed Circuit Boards (PCBs) using computer vision and neural networks.

## Project Overview
This project implements a full pipeline for PCB quality inspection:

1. Dataset inspection and organization
2. Image alignment and preprocessing
3. Image subtraction to highlight defects
4. Thresholding using Otsu’s method
5. ROI extraction for defect localization
6. Sample outputs for visual validation
7. Deep learning classification (Module 2 onwards)

## Key Features
- Automatic template-test alignment
- Robust feature matching (ORB + RANSAC)
- Difference mask generation
- Adaptive thresholding
- ROI extraction and cropping
- Sample outputs included
- Future integration with PyTorch and Streamlit

## Tech Stack
- Python 3.8+
- OpenCV, NumPy, Matplotlib, tqdm
- PyTorch (upcoming)
- Streamlit (upcoming)

## Folder Structure
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
