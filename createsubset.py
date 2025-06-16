import os
import shutil

# Path to original dataset root
base_path = "/Users/cavins/Desktop/project/Thermal-image-human-detection"

NUM_SAMPLES = 2000

# Source test folders (original test dataset)
source_images = os.path.join(base_path, "dataset/test/images")
source_labels = os.path.join(base_path, "dataset/test/labels")

# Destination test folders (subset inside "dataaset")
dest_root = os.path.join(base_path, "dataaset/test")  # note the typo "dataaset"
dest_images = os.path.join(dest_root, "images")
dest_labels = os.path.join(dest_root, "labels")

# Create destination folders if they don't exist
os.makedirs(dest_images, exist_ok=True)
os.makedirs(dest_labels, exist_ok=True)

# Get sorted list of test images
try:
    image_files = sorted(
        f for f in os.listdir(source_images) if f.lower().endswith((".jpg", ".png"))
    )
except FileNotFoundError:
    print(f"❌ Source folder not found: {source_images}")
    exit(1)

# Take first NUM_SAMPLES images
selected_images = image_files[:NUM_SAMPLES]

copied = 0
for img_file in selected_images:
    label_file = os.path.splitext(img_file)[0] + ".txt"

    src_img_path = os.path.join(source_images, img_file)
    src_lbl_path = os.path.join(source_labels, label_file)

    dst_img_path = os.path.join(dest_images, img_file)
    dst_lbl_path = os.path.join(dest_labels, label_file)

    if os.path.exists(src_lbl_path):
        shutil.copy2(src_img_path, dst_img_path)
        shutil.copy2(src_lbl_path, dst_lbl_path)
        copied += 1
    else:
        print(f"⚠️ Skipping {img_file} — label not found: {label_file}")

print(f"\n✅ Done! Copied {copied} image-label pairs to: {dest_root}")
