import cv2
from ultralytics import YOLO
### This will download the weights
### Key- we don't want to download the weights every single time
##  Created a folder to store the weights and call the model on the image

#model=   YOLO('yolov8l.pt')
#results= model("../Images/1.png",show=True")
#cv2.waitKey(0)

#model=  YOLO("./Yolo-Weights/yolov8l.pt")
#results= model("../Images/1.png",show=True)
#cv2.waitKey(0)

#model=  YOLO("./Yolo-Weights/yolov8l.pt")
#results= model("../Images/2.png",show=True)
#cv2.waitKey(0)

model=  YOLO("./Yolo-Weights/yolov8n.pt")
results= model("../Images/3.png",show=True)
cv2.waitKey(0)