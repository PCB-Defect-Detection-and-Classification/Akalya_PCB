import os
import sys
import time
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
import cv2

# ---------------- ADD BACKEND TO PATH ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")
if BACKEND_DIR not in sys.path:
    sys.path.append(BACKEND_DIR)

from inspector import inspect_pcb, load_model
from exporter import export_results

# ---------------- PATHS ----------------
MODEL_PATH = os.path.join(BASE_DIR, "models", "pcb_model.keras")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------- STREAMLIT PAGE CONFIG ----------------
st.set_page_config(
    page_title="PCB Defect Inspector | Milestone 4",
    layout="wide"
)

st.title("🧪 PCB Defect Inspector - Milestone 4")
st.caption("Sliding Window PCB Inspection with Export")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Inspection Settings")
confidence = st.sidebar.slider("Confidence Threshold (%)", 50, 100, 85, step=5)
patch_size = st.sidebar.slider("Patch Size (px)", 64, 256, 128, step=32)
stride = st.sidebar.slider("Stride (px)", 32, 128, 64, step=16)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_cnn_model():
    if not os.path.exists(MODEL_PATH):
        st.error(f"❌ Model not found at {MODEL_PATH}")
        st.stop()
    return load_model(MODEL_PATH)

with st.spinner("🔄 Loading CNN model..."):
    model = load_cnn_model()
st.success("✅ Model loaded successfully")

# ---------------- IMAGE UPLOAD ----------------
uploaded_file = st.file_uploader("📤 Upload PCB Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)
    st.image(image_np, caption="Uploaded PCB Image", use_container_width=True)

    if st.button("🚀 Run Inspection"):
        with st.spinner("🔍 Inspecting PCB..."):
            start_time = time.time()
            annotated_img, defects = inspect_pcb(
                image=image_np,
                model=model,
                confidence_thresh=confidence,
                patch_size=patch_size,
                stride=stride
            )
            end_time = time.time()

        # ---------------- BOARD HEALTH SCORE ----------------
        score = max(0, 100 - len(defects) * 15)

        # ---------------- EXPORT RESULTS ----------------
        img_path, csv_path = export_results(
            annotated_img=annotated_img,
            defects=defects,
            output_dir=OUTPUT_DIR
        )

        # ---------------- DISPLAY RESULTS ----------------
        tab1, tab2, tab3 = st.tabs(["🖼 Annotated PCB", "🧾 Defect Log", "📥 Downloads"])

        with tab1:
            st.image(annotated_img, use_container_width=True)
            st.metric("Board Health Score", f"{score}/100")
            st.metric("Total Defects Detected", len(defects))
            st.success(f"⏱ Inspection completed in {end_time - start_time:.2f} seconds")

        with tab2:
            if defects:
                st.dataframe(pd.DataFrame(defects), use_container_width=True)
            else:
                st.success("🎉 No defects detected. PCB is clean!")

        with tab3:
            st.download_button(
                label="🖼 Download Annotated Image",
                data=open(img_path, "rb"),
                file_name=os.path.basename(img_path),
                mime="image/jpeg"
            )
            st.download_button(
                label="📄 Download Defect Log (CSV)",
                data=open(csv_path, "rb"),
                file_name=os.path.basename(csv_path),
                mime="text/csv"
            )

else:
    st.info("👆 Upload a PCB image to start inspection")
