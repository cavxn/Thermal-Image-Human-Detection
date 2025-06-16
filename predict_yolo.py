from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train34/weights/best.pt")

results = model.predict(source="/Users/cavins/Desktop/project/Thermal-image-human-detection/dataset/test/images/210149.jpg", save=False)

for r in results:
    annotated_frame = r.plot()  

    cv2.imshow("YOLO Prediction", annotated_frame)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()

