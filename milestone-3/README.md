# 🔬 PCB Defect Inspector – Milestone 3

### Frontend & Backend Integration for Intelligent PCB Inspection

**Project Name:** Intelligent PCB Defect Detection System  
**Milestone:** 3 – Web Application & System Integration  
**Developer:** Akalya  
**Platform:** Google Colab + Streamlit  

---

## 🎯 Objective

Milestone 3 focuses on integrating the **Computer Vision pipeline (Milestone 1)** and the **Deep Learning classifier (Milestone 2)** into a single, interactive **web-based inspection system**.

The application allows users to:

- Upload PCB images
- Detect and visualize defects
- Compare boards with a golden template
- Generate professional inspection reports

---

## 🧩 System Overview

This milestone combines three major components:

1. **Frontend (Streamlit)**
   - User-friendly dashboard
   - Image upload and visualization
   - Real-time defect inspection

2. **Backend Pipeline**
   - Image alignment and inspection logic
   - Model inference (placeholder / trained model)
   - Defect aggregation and scoring

3. **Reporting Module**
   - PDF-based inspection report
   - Visual proof of detected defects
   - Confidence and health metrics

---

## 📂 Folder Structure

milestone-3/
│
├── app.py # Streamlit frontend
├── README.md # Documentation
├── requirements.txt # Python dependencies
│
├── backend/
│ ├── backend.py # Inspection & inference logic
│ └── config.py # Paths and configuration
│
├── sample_images/
│ ├── template/ # Golden (defect-free) PCB images
│ └── test/ # Test PCB images
│
├── models/ # Trained model files (ignored in Git)
├── output/ # Generated images and PDF reports


---

## 🖼️ Template vs Test Image Explanation

### ✅ Template Image
- A **clean / golden PCB**
- Used as reference
- No defects expected

### ✅ Test Image
- PCB under inspection
- May contain one or more defects
- Compared against template image

⚠️ **Important:**  
Do **NOT** use cropped defect-only images.  
Always use **full PCB images** for correct alignment and inspection.

---

## ⚙️ Key Features

- Automatic PCB alignment
- Defect localization and visualization
- Confidence-based defect filtering
- Interactive **X-Ray comparison slider**
- Board health score calculation
- PDF inspection report generation

---

## 🚀 How to Run in Google Colab

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt

### 2️⃣ Run Streamlit App
streamlit run app.py


After running, Streamlit will show:
Local URL: http://localhost:8501

Use Cloudflare / Colab tunnel to access the app in browser.


###📊 Output Generated

1.Annotated PCB images with defect markings

2.Defect log table (type & confidence)

3.Downloadable PCB Inspection Report (PDF)

#All outputs are saved inside:

output/


##✅ Milestone Completion Status

| Milestone | Description                       | Status      |
| --------- | --------------------------------- | ----------- |
| M1        | Dataset Preparation & CV Pipeline | ✅ Completed |
| M2        | Model Training & Evaluation       | ✅ Completed |
| M3        | Web App & System Integration      | ✅ Completed |


###📝 Notes for Evaluation 

1.Backend currently supports placeholder inference

2.Architecture is modular and production-ready

3.Trained EfficientNet model can be plugged in easily

4.Designed for real-world PCB Quality Assurance

