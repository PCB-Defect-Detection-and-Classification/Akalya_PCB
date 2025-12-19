
import os
import cv2
import pandas as pd
import datetime

def export_results(annotated_img, defects, output_dir):
    '''
    Saves:
    1. Annotated image (.jpg)
    2. Defect log (.csv)

    Returns:
        image_path, csv_path
    '''

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    image_path = os.path.join(output_dir, f"pcb_result_{timestamp}.jpg")
    csv_path = os.path.join(output_dir, f"pcb_log_{timestamp}.csv")

    # ---- SAVE IMAGE ----
    img_bgr = cv2.cvtColor(annotated_img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(image_path, img_bgr)

    # ---- SAVE CSV ----
    if defects:
        df = pd.DataFrame(defects)
        df.to_csv(csv_path, index=False)
    else:
        df = pd.DataFrame(columns=["type", "confidence", "bbox"])
        df.to_csv(csv_path, index=False)

    return image_path, csv_path
