import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "../models/pcb_defect_model.keras")
OUTPUT_DIR = os.path.join(BASE_DIR, "../output")
SAMPLE_IMAGES_DIR = os.path.join(BASE_DIR, "../sample_images")
