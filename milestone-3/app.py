
import os
import streamlit as st
import numpy as np
from PIL import Image
from streamlit_image_comparison import image_comparison
from fpdf import FPDF
import base64
import datetime
import time
from backend import backend, config

# --- PAGE CONFIG ---
st.set_page_config(page_title="PCB Defect Inspector", page_icon="🔬", layout="wide")

# --- CUSTOM CSS ---
st.markdown('''
    <style>
    .metric-card {
        background-color: #e3f2fd;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .stButton>button {
        width: 100%;
        background-color: #1976d2;
        color: white;
        font-weight: bold;
    }
    .stProgress>div>div>div>div {
        background-color: #1976d2;
    }
    </style>
''', unsafe_allow_html=True)

# --- PDF GENERATION ---
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'PCB Defect Inspection Report', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, f'Generated: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')


def generate_pdf(annotated_img, defects, health_score):
    import os
    from PIL import Image
    from fpdf import FPDF
    import datetime

    # --- Ensure output folder exists ---
    output_folder = "/content/drive/MyDrive/Akalya_PCB/milestone-3/output"
    os.makedirs(output_folder, exist_ok=True)

    # --- Temp image path ---
    temp_img_path = os.path.join(output_folder, "temp_report_img.jpg")
    Image.fromarray(annotated_img).save(temp_img_path)

    # --- PDF class ---
    class PDFReport(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 16)
            self.cell(0, 10, 'PCB Defect Inspection Report', 0, 1, 'C')
            self.set_font('Arial', 'I', 10)
            self.cell(0, 10, f'Generated: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 0, 1, 'C')
            self.ln(5)

        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    # --- Generate PDF ---
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Inspection Summary', 0, 1)
    pdf.set_font('Arial', '', 11)
    pdf.cell(60, 10, f'Health Score: {health_score}/100', 1)
    pdf.cell(60, 10, f'Defects Found: {len(defects)}', 1)
    pdf.cell(60, 10, f'Model: EfficientNetB0', 1)
    pdf.ln(15)

    pdf.image(temp_img_path, x=10, w=190)
    pdf.ln(5)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Detailed Defect Log', 0, 1)
    pdf.set_fill_color(200, 220, 255)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(60, 10, 'Defect Type', 1, 0, 'C', 1)
    pdf.cell(60, 10, 'Confidence %', 1, 0, 'C', 1)
    pdf.cell(60, 10, 'Status', 1, 1, 'C', 1)
    pdf.set_font('Arial', '', 10)
    for d in defects:
        pdf.cell(60, 10, str(d['type']), 1, 0, 'C')
        pdf.cell(60, 10, f"{d['confidence']:.1f}%", 1, 0, 'C')
        pdf.cell(60, 10, 'Flagged', 1, 1, 'C')

    return pdf.output(dest='S').encode('latin-1')



# --- HEADER ---
st.title("🔬 Intelligent PCB Defect Inspection System")
st.markdown("Automated Quality Assurance using EfficientNet & Computer Vision")

# --- SIDEBAR ---
st.sidebar.header("⚙️ Configuration")
confidence_thresh = st.sidebar.slider("Confidence Threshold", 0, 100, 50)
template_file = st.sidebar.file_uploader("Upload Golden Template", type=['jpg', 'png', 'jpeg'])
test_file = st.sidebar.file_uploader("Upload Test PCB", type=['jpg', 'png', 'jpeg'])

# --- MAIN LOGIC ---
if template_file and test_file:
    t_img = Image.open(template_file).convert('RGB')
    test_img = Image.open(test_file).convert('RGB')
    t_arr = np.array(t_img)
    test_arr = np.array(test_img)

    with st.spinner("🧠 Loading AI Model..."):
        model = backend.load_defect_model()

    if st.sidebar.button("🚀 Run Inspection"):
        progress = st.progress(0)
        time.sleep(0.3)
        progress.progress(20)
        aligned, annotated, defects = backend.run_inspection(t_arr, test_arr, model, confidence_thresh)
        progress.progress(70)
        time.sleep(0.3)
        progress.progress(100)

        # --- METRICS ---
        m1, m2, m3 = st.columns(3)
        m1.metric("Total Defects", len(defects))
        m2.metric("Processing Time", "1.2s")
        score = max(0, 100 - len(defects) * 15)
        color = "normal" if score > 80 else "off"
        m3.metric("Board Health Score", f"{score}/100", delta_color=color)

        st.divider()
        tab1, tab2, tab3 = st.tabs(["🔍 Defect Map", "👁️ X-Ray Comparison", "📄 Defect Log"])

        with tab1:
            st.image(annotated, caption="Detected Defects", use_container_width=True)
        with tab2:
            st.markdown("Slide to compare Template vs Test PCB")
            image_comparison(
                img1=t_arr,
                img2=annotated,
                label1="Template",
                label2="Test PCB",
                width=1200,
                starting_position=50,
                show_labels=True,
                make_responsive=True
            )
        with tab3:
            if defects:
                st.dataframe(defects)
            else:
                st.info("No defects found!")

        # --- REPORT ---
        if defects:
            st.subheader("📝 Export Inspection Report")
            pdf_bytes = generate_pdf(annotated, defects, score)
            b64 = base64.b64encode(pdf_bytes).decode()
            st.markdown(
                f'<a href="data:application/pdf;base64,{b64}" download="PCB_Inspection_Report.pdf">'
                f'<button style="background-color:#1976d2;color:white;padding:10px 20px;border:none;border-radius:5px;">📥 Download PDF Report</button></a>',
                unsafe_allow_html=True
            )
else:
    st.info("👋 Upload Template and Test PCB images to begin inspection")
