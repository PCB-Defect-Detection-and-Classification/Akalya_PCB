# 🧪 PCB Defect Inspector - Milestone 4

Welcome to the **Milestone 4 version** of the **PCB Defect Detection System**!  
This is an **AI-powered inspection tool** for automated quality assurance of printed circuit boards.

---

## ✨ Key Features

- 📤 Upload PCB images for inspection  
- 🤖 Automated defect detection with CNN  
- 🔎 Patch-based scanning for high accuracy  
- 🖼️ Annotated output images with bounding boxes  
- 🎚️ Adjustable confidence threshold  
- 💾 Export results as **JPG** & **CSV**  
- 🖥️ Streamlit web interface for easy usage  

---

## 📁 Directory Structure

milestone-4/
├── app.py # Streamlit app
├── backend/
│ ├── inspector.py # Core inspection logic
│ └── exporter.py # Export results (JPG + CSV)
├── models/
│ └── pcb_model.keras # Trained CNN model
├── sample_images/
│ ├── template/ # Golden PCB templates
│ └── test/ # Test PCB images
├── output/ # Results (images + logs)
├── README.md
└── .gitignore

---
## 🛠️ Modules Overview

### Module 3: PCB Defect Detection Prototype


**Tasks:**
- 🧩 Developed patch-based CNN for PCB defects  
- ⚡ Backend logic in `inspector.py` for:
  - Image alignment  
  - Patch scanning  
  - Defect classification  
- 💾 Export functionality (`exporter.py`) for annotated images & CSV logs  
- 🖥️ Prototype Streamlit app for testing  

**Deliverables:**
- Prototype web app  
- Sample annotated images  
- CSV defect logs  

**Evaluation:**
- ✅ Accuracy of defect detection  
- ✅ Integration of model with prototype  
- ✅ UI responsiveness  

---

### Module 4: Finalization & Delivery

**Tasks:**
- 🖥️ Integrate modules into final Streamlit app  
- 📥 Add export feature for images & defect logs  
- 🔍 Test app on multiple PCB images  
- ⚡ Optimize processing for speed  
- 📝 Prepare technical documentation & README  
- 🎥 Prepare demo video / slides  

**Deliverables:**
- ✅ Final web app with export functionality  
- ✅ Annotated PCB images & CSV logs  
- ✅ Documentation PDF  
- ✅ Organized GitHub repo  
- ✅ Recorded demo / slides  

**Evaluation:**
- ✅ Fully functional UI  
- ✅ Robust defect detection across test cases  
- ✅ Clear documentation  
- ✅ Demo-ready presentation  

---

## 🚀 How to Run in Google Colab

1️⃣ Mount your Google Drive:
from google.colab import drive
drive.mount('/content/drive')

2️⃣ Install dependencies:
!pip install streamlit opencv-python-headless tensorflow pillow pandas

3️⃣ Run the Streamlit app:
!streamlit run /content/drive/MyDrive/Akalya_PCB/milestone-4/app.py



##📝 Usage Guide :
---
1.Upload a PCB image via the sidebar

2.Adjust confidence threshold (default 50%)

3.Click Run Inspection

4.View annotated results with defect boxes

5.Download:

🖼️ Annotated image

📄 CSV defect log


##⚠️ Notes
--
Ensure models/pcb_model.keras exists sample_images/template & sample_images/test must contain images
output/ folder will auto-create for storing results


##👩‍💻 Author
--
Akalya S.
SASTRA University
