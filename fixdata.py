import os

image_dir = 'dataset/train/images'
label_dir = 'dataset/train/labels'

image_filenames = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]

for image in image_filenames:
    base = os.path.splitext(image)[0]  # e.g. enhanced_250242
    numeric_part = base.split('_')[-1]  # e.g. 250242
    old_label_path = os.path.join(label_dir, f"{numeric_part}.txt")
    new_label_path = os.path.join(label_dir, base + '.txt')

    if os.path.exists(old_label_path):
        os.rename(old_label_path, new_label_path)
        print(f"✅ Renamed: {old_label_path} -> {new_label_path}")
    else:
        print(f"⚠️ No label found for: {image}")
