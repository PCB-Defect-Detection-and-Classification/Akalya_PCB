
🧪 PCB Defect Detection and Classification System – Complete Project Documentation
--
Project Statement
-
The objective of this project is to develop an automated PCB defect detection and classification system using image processing and deep learning techniques.

The system integrates:
-
1.Template-based image subtraction for defect highlighting

2.Contour extraction for ROI detection

3.CNN-based classification for defect labeling

4.A Streamlit-based frontend enables users to upload PCB images, view annotated results, and export defect logs (CSV) and annotated images (JPG) for documentation and reporting.

Project Objectives
-

🔹 Detect and localize PCB defects accurately

🔹 Classify defects into six predefined categories:

               1.Missing Hole 🕳️

               2.Mouse Bite 🐭

               3.Open Circuit ⚡

               4.Short 🔗

               5.Spur 🌱

               6.Spurious Copper 🟦

               
🔹 Train a robust CNN model (EfficientNet) with high accuracy

🔹 Develop a user-friendly frontend for image upload and visualization

🔹 Implement a modular backend for image inference and processing

🔹 Enable export of annotated images, defect logs, and reports

Dataset
-

Source:  
- 
     DeepPCB dataset

Structure: 
-
      Paired template and test images, with annotations for defects

Processing:
-
              1.Image alignment using ORB + RANSAC

              2.Image subtraction for defect highlighting

              3.Thresholding with Otsu’s method

              4.ROI extraction for CNN input

Folder Structure:
-

PCB_DATASET/
├── train/
│   ├── missing_hole/
│   ├── mouse_bite/
│   ├── open_circuit/
│   ├── short/
│   ├── spur/
│   └── spurious_copper/
├── val/
│   ├── missing_hole/
│   ├── mouse_bite/
│   ├── open_circuit/
│   ├── short/
│   ├── spur/
│   └── spurious_copper/
├── processed/
│   ├── aligned_images/
│   ├── difference_masks/
│   ├── thresholded_masks/
│   ├── defect_rois/
│   └── samples/
└── docs/


Methodology
-

1️⃣ Image Preprocessing
-
       Convert images to grayscale and normalize

       Align test images with template using ORB feature matching + RANSAC

       Apply Gaussian blur to reduce noise

       Perform image subtraction to highlight defect regions
       

2️⃣ Contour Detection & ROI Extraction
-
      Detect defect contours using OpenCV

      Crop Regions of Interest (ROI) for classification

      Label and save ROIs for training the CNN
      

3️⃣ CNN-based Classification
-
       Backbone: EfficientNetB0 (pretrained on ImageNet)

       Input: 128x128 pixels RGB

       Loss: Categorical Cross-Entropy

       Optimizer: Adam

       Training:

            1.Freeze EfficientNet base

            2.Train custom classification head

            3.Runtime data augmentation (rotation, flips, zooms)

      Output: Defect type + confidence score
      

4️⃣ Backend Pipeline
-

Modular Python functions handle:

Alignment and subtraction

ROI extraction

Model inference

Returns annotated images and defect logs


5️⃣ Frontend UI
- 
Built with Streamlit

Features:
-
Image upload for template & test PCBs

Annotated visualization of defects

Adjustable confidence threshold

Download annotated images & CSV logs


Project Milestones
-

Milestone 1: Dataset Preparation & CV Pipeline
-
Dataset alignment, subtraction, thresholding, ROI extraction

Deliverables: Processed images, defect masks, ROI crops
-
Metrics: Alignment accuracy 100%, defect extraction 3–12 per image
-

Milestone 2: Model Training & Evaluation
-
CNN training with EfficientNet, validation & confusion matrix

Deliverables: Trained model, accuracy metrics (96% validation)
-
Metrics: High precision & recall, minimal misclassification
-

Milestone 3: Web App & System Integration
-
Streamlit frontend + modular backend pipeline

Deliverables: Interactive app with defect visualization
-
Metrics: Responsive UI, accurate defect detection, export-ready
-

Milestone 4: Finalization & Delivery
-
Export results, optimize processing, final documentation

Deliverables: Final web app, annotated images, CSV logs, PDF report
-
Metrics: Fully functional system, ready for demonstration
-

Evaluation Metrics
-

| Metric                     | Description                    | Target |
| -------------------------- | ------------------------------ | ------ |
| Detection Accuracy ✅       | Correctly detected defects     | ≥95%   |
| Classification Accuracy 🎯 | Correct defect type prediction | ≥95%   |
| ROI Precision 📐           | Bounding box coverage          | High   |
| Processing Time ⏱️         | Time per image                 | ≤3s    |
| Export Quality 💾          | Correct image & CSV generation | 100%   |

Tech Stack
-

| Area                   | Tools / Libraries          |
| --------------------   | -------------------------- |
| Image Processing 🖼️   | OpenCV, Numpy              |
| Deep Learning 🤖      | TensorFlow, Keras, PyTorch |
| Dataset 📂            | DeepPCB                    |
| Frontend 🌐           | Streamlit                  |
| Backend 🛠️            | Python, Modular Functions  |
| Evaluation 📊         | Accuracy, Confusion Matrix |
| Export 📦             | CSV, Annotated Image, PDF  |



Project Outputs
-
1.Annotated PCB images with bounding boxes

2.CSV logs of defects (type & confidence)

3.Visual reports and PDF export (optional)

4.Trained EfficientNet CNN model

5.Streamlit web application for inspection


Usage Guide
-
1.Mount Google Drive (for Colab):

from google.colab import drive
drive.mount('/content/drive')


2.Install dependencies:

!pip install streamlit opencv-python-headless tensorflow pillow pandas


3.Run Streamlit app:

!streamlit run /content/drive/MyDrive/Akalya_PCB/milestone-4/app.py


4.Upload PCB image, adjust confidence, run inspection

5.View annotated output and download CSV/image


Future Enhancements
-

Real-time PCB inspection using camera input

Industrial deployment with higher resolution support

Semi-supervised learning for unannotated defects

Expanded defect categories and multi-board inspection


Author
-

Akalya S. – SASTRA University

PCB Defect Detection & Classification System – Full Project (Milestone 1–4)


Highlights
-

Transfer learning using EfficientNet 🧠

Patch-based scanning for high detection accuracy 🔎

Modular backend + interactive frontend 🖥️

Exportable CSV and annotated images for professional reporting 💾

Validation accuracy: 96% across six defect classes ✅

Summary:
-

This documentation combines:

Milestone 1 (Dataset & preprocessing)

Milestone 2 (Model training & evaluation)

Milestone 3 (Frontend & backend integration)

Milestone 4 (Finalization, export, and presentation)
