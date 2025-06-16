import os
from ultralytics import YOLO
from tqdm import tqdm

def main():
    model = YOLO("runs/detect/train8/weights/best.pt")
    image_dir = "/Users/cavins/Desktop/project/Thermal-image-human-detection/dataset/test/images"
    image_paths = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.png'))]

    print(f"Found {len(image_paths)} images.")

    for image_path in tqdm(image_paths, desc="Predicting"):
        results = model.predict(source=image_path, conf=0.25, verbose=False)

    print(f"✅ Finished testing {len(image_paths)} images.")

if __name__ == "__main__":
    main()
