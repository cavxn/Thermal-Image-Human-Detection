import cv2
from ultralytics import YOLO

model = YOLO("runs/detect/train27/weights/best.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    gray_enhanced = clahe.apply(gray)

    gray_3ch = cv2.cvtColor(gray_enhanced, cv2.COLOR_GRAY2BGR)

    
    results = model.predict(source=gray_3ch, save=False, verbose=False, conf=0.25)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Grayscale Thermal Simulation", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
