
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix

MODEL_PATH = "/content/drive/MyDrive/pcb_defect_model.keras"
VAL_DIR   = "/content/drive/MyDrive/PCB_Training_Dataset_Split/val"
IMG_SIZE = (128, 128)
BATCH_SIZE = 32

# Load validation data
val_gen = tf.keras.utils.image_dataset_from_directory(
    VAL_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

class_names = val_gen.class_names
print("Classes:", class_names)

# Load model
model = tf.keras.models.load_model(MODEL_PATH)

# Predict on validation set
y_true = []
y_pred = []

for images, labels in val_gen:
    preds = model.predict(images, verbose=0)
    y_true.extend(labels.numpy())
    y_pred.extend(np.argmax(preds, axis=1))

# Classification report
print("\nCLASSIFICATION REPORT")
print(classification_report(y_true, y_pred, target_names=class_names))

# Confusion matrix
cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=class_names, yticklabels=class_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
