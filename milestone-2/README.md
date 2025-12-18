# PCB Defect Detection and Classification using EfficientNet

## 📌 Project Overview

This project focuses on **automatic detection and classification of Printed Circuit Board (PCB) defects** using deep learning. A **6‑class image classification model** is built using **EfficientNet** as the backbone and trained on a realistic PCB defect dataset.

The goal is to develop a robust system that can accurately identify common PCB manufacturing defects, helping improve quality control in electronics production.

---

## 🎯 Problem Statement

Manual inspection of PCBs is:

* Time‑consuming
* Error‑prone
* Difficult to scale

This project automates PCB defect inspection by leveraging **transfer learning** and **runtime data augmentation**, achieving **high classification accuracy** on unseen validation images.

---

## 🧩 Defect Classes

The model classifies PCB images into the following **6 defect categories**:

1. Missing Hole
2. Mouse Bite
3. Open Circuit
4. Short
5. Spur
6. Spurious Copper

---

## 📂 Dataset Structure

The dataset is organized in a standard image‑classification format:

```
PCB_DATASET/
├── train/
│   ├── missing_hole/
│   ├── mouse_bite/
│   ├── open_circuit/
│   ├── short/
│   ├── spur/
│   └── spurious_copper/
└── val/
    ├── missing_hole/
    ├── mouse_bite/
    ├── open_circuit/
    ├── short/
    ├── spur/
    └── spurious_copper/
```

Each class contains real PCB images provided for training and validation.

---

## 🏗️ Model Architecture

* **Backbone:** EfficientNet (pretrained on ImageNet)
* **Input Size:** 128 × 128 × 3
* **Loss Function:** Sparse Categorical Cross‑Entropy
* **Optimizer:** Adam
* **Training Strategy:**

  * Freeze EfficientNet base
  * Train custom classification head
  * Runtime data augmentation

---

## 🔁 Data Augmentation

Runtime augmentation is applied during training to improve generalization:

* Random rotation
* Width & height shifts
* Zoom
* Horizontal flip

This helps the model handle real‑world PCB variations.

---

## 📊 Results

### ✅ Validation Performance

* **Overall Accuracy:** **96%**

### 📌 Classification Report

* High precision and recall across all defect classes
* Strong performance even on visually similar defects

### 📉 Confusion Matrix

* Minimal misclassification
* Most errors occur between visually overlapping defect patterns

Both the **confusion matrix** and **classification report** are saved in the output folder.

---

## 🖼️ Inference & Visualization

* The trained model is used to predict defects on real validation images
* One annotated image per class is generated
* Each image shows:

  * Ground truth label
  * Predicted label
  * Confidence score

Annotated images are stored for visual verification.

---

## 📁 Repository Structure

```
Akalya_PCB/
├── milestone-1/
├── milestone-2/
│   ├── code/
│   │   ├── train_effinet.py
│   │   ├── evaluation.py
│   │   └── inference.py
│   ├── output/
│   │   ├── Annotated_Test_Images/
│   │   ├── confusion_matrix.png
│   │   └── classification_report.txt
│   ├── requirements.txt
│   └── .gitignore
```

---

## ⚙️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Train the Model

```bash
python train_effinet.py
```

### 3️⃣ Evaluate the Model

```bash
python evaluation.py
```

### 4️⃣ Run Inference

```bash
python inference.py
```

---

## 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* EfficientNet
* OpenCV
* NumPy
* Matplotlib
* Google Colab

---

## 🌟 Key Highlights

* Transfer learning with EfficientNet
* Clean and modular code structure
* Strong validation accuracy (96%)
* Visual interpretability using annotated predictions

---

## 📌 Conclusion

This project demonstrates how deep learning can significantly improve PCB defect inspection accuracy. The trained model performs reliably across multiple defect types and can be extended for industrial‑scale inspection systems.

---

## 👤 Author

**Akalya S**
PCB Defect Detection & Classification Project

