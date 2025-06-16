from ultralytics import YOLO

model = YOLO("runs/detect/train8/weights/best.pt")

results = model.val(data="thermal_dataset.yaml", imgsz=412, batch=16)

print("Validation results:")
print(f"Precision: {results.precision:.4f}")
print(f"Recall: {results.recall:.4f}")
print(f"mAP@0.5: {results.map50:.4f}")
print(f"mAP@0.5:0.95: {results.map:.4f}")
