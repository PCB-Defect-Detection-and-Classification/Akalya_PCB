
import streamlit as st
import numpy as np
from PIL import Image
import time
import os
import sys

# ---------------- ADD BACKEND TO PATH ----------------
BASE_DIR = "/content/drive/MyDrive/Akalya_PCB/milestone-4"
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
    layout="centered"
)

st.title("🧪 PCB Defect Inspector")
st.caption("Milestone-4: Testing, Evaluation & Export")

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

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Inspection Settings")
confidence = st.sidebar.slider(
    "Confidence Threshold (%)",
    min_value=30,
    max_value=100,
    value=50,
    step=5
)

# ---------------- IMAGE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "📤 Upload PCB Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)
    st.image(image, caption="Uploaded PCB Image", use_container_width=True)

    if st.button("🚀 Run Inspection"):
        with st.spinner("🔍 Inspecting PCB..."):
            start_time = time.time()
            annotated_img, defects = inspect_pcb(
                image=image_np,
                model=model,
                confidence_thresh=confidence
            )
            end_time = time.time()

        # ---------------- EXPORT RESULTS ----------------
        img_path, csv_path = export_results(
            annotated_img=annotated_img,
            defects=defects,
            output_dir=OUTPUT_DIR
        )

        # ---------------- DISPLAY RESULTS ----------------
        st.subheader("📌 Inspection Output")
        st.image(annotated_img, use_container_width=True)
        st.success(f"⏱️ Inspection completed in {end_time - start_time:.2f} seconds")

        if defects:
            st.subheader("🧾 Detected Defects")
            st.dataframe(defects, use_container_width=True)
        else:
            st.success("🎉 No defects detected. PCB is clean!")

        # ---------------- DOWNLOAD SECTION ----------------
        st.divider()
        st.subheader("📥 Download Results")

        with open(img_path, "rb") as f:
            st.download_button(
                "🖼️ Download Annotated Image",
                f,
                file_name=os.path.basename(img_path),
                mime="image/jpeg"
            )

        with open(csv_path, "rb") as f:
            st.download_button(
                "📄 Download Defect Log (CSV)",
                f,
                file_name=os.path.basename(csv_path),
                mime="text/csv"
            )

else:
    st.info("👆 Upload a PCB image to start inspection")

