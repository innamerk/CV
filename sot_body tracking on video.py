import cv2
import os

#tracker = cv2.TrackerMIL_create()  # метод Multiple Instance Learning
#tracker = cv2.legacy.TrackerMOSSE_create()  # Minimum Output Sum of Squared Error
tracker = cv2.TrackerGOTURN_create() # нейросеть (требует веса)

Y=[]
cap = cv2.VideoCapture('150Э.mp4')
while True:
    timer = cv2.getTickCount()
    success, img = cap.read()
    cv2.imshow("Tracking", img)
    if not success:
        break
    if cv2.waitKey(50) & 0xff == ord('m'):
        break  
    
bbox = cv2.selectROI("Tracking", img)
tracker.init(img, bbox)

def drawBox():
    cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3])), (255, 0, 0), 3, 1)

while True:
    timer = cv2.getTickCount()
    success, img = cap.read()
    if not success:
        break
    success, bbox = tracker.update(img)
    if success:
        drawBox()
        Y.append(bbox[1]+bbox[3])
    else:
        cv2.putText(img, "Lost", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(img, str(int(fps)), (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow("Tracking", img)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import pandas as pd
df = pd.DataFrame(Y)
df.to_excel(excel_writer = "porh_Y_150_test.xlsx",)