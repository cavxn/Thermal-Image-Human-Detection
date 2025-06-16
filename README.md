Thermal Image Human Detection with YOLOv8

A deep learning project to detect humans in thermal images using the powerful YOLOv8 object detection framework. This project focuses on real-time detection and robust evaluation metrics on thermal datasets, enabling effective human presence recognition in low-light or obscured conditions.

Project Structure
Thermal-Image-Human-Detection/
├── runs/ # YOLOv8 training/validation outputs
├── dataset/ # Dataset folder with images & labels
├── models/ # Custom model weights or configs
├── preprocessing.ipynb # Image preprocessing & CLAHE
├── train.py # Training script
├── val.py # Validation/Evaluation script
├── results/ # Optional results directory
├── README.md # Project documentation


Features

-  YOLOv8-based object detection
-  Trained on thermal image datasets
-  Evaluation with precision, recall, mAP
-  Preprocessing: CLAHE, gamma correction, augmentation
-  Visual result inspection & metrics analysis

 Dataset Used

> Dataset: [Thermal Images for Human Detection](https://www.kaggle.com/datasets)

- Images captured using thermal cameras
- Labeled with bounding boxes for human presence
- Train/val/test split applied manually

---

Setup & Installation

git clone https://github.com/yourusername/Thermal-Image-Human-Detection.git
cd Thermal-Image-Human-Detection

Install dependencies
pip install -r requirements.txt

Or install Ultralytics YOLO
pip install ultralytics opencv-python matplotlib

Training the Model
yolo task=detect mode=train model=yolov8n.pt data=your_data.yaml epochs=50 imgsz=640
You can modify data.yaml to point to your thermal dataset and class names.

Validation & Evaluation
yolo task=detect mode=val model=runs/detect/train/weights/best.pt data=your_data.yaml
This outputs:

Metric	Value
Precision	0.91
Recall	0.85
mAP@0.5	0.94
mAP@0.5:0.95	0.60

Good performance on thermal imagery despite occlusion and noise.

Data Augmentations Used
mosaic: 1.0 → Diverse object layout
mixup: 0.1 → Slight blending of images
copy_paste: 0.1 → Simulate occlusion/overlap
fliplr: 0.5 → Flip horizontally
translate: 0.1, scale: 0.5 → Positional/zoom variation

Preprocessing
Done in preprocessing.ipynb:
CLAHE (Contrast Limited Adaptive Histogram Equalization)
Gamma correction
Histogram inspection

Future Work
Real-time webcam or FLIR camera support
Fine-tuning on real surveillance data
Per-image metric visualization

Contributing
Feel free to fork and open pull requests. Improvements to detection accuracy or data augmentation pipelines are welcome!

