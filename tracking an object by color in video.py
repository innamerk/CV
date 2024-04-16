import cv2
import numpy as np
if __name__ == '__main__':
    def nothing(*arg):
        pass

cv2.namedWindow( "result" ) # создаем главное окно
cv2.namedWindow( "settings" ) # создаем окно настроек

cap = cv2.VideoCapture('150Э.mp4')
# создаем 6 бегунков для настройки начального и конечного цвета фильтра
cv2.createTrackbar('h1', 'settings', 0, 255, nothing)
cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
cv2.createTrackbar('v2', 'settings', 255, 255, nothing)
crange = [0,0,0, 0,0,0]

while True:
    flag, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
 
    # считываем значения бегунков
    h1 = cv2.getTrackbarPos('h1', 'settings')
    s1 = cv2.getTrackbarPos('s1', 'settings')
    v1 = cv2.getTrackbarPos('v1', 'settings')
    h2 = cv2.getTrackbarPos('h2', 'settings')
    s2 = cv2.getTrackbarPos('s2', 'settings')
    v2 = cv2.getTrackbarPos('v2', 'settings')

    # формируем начальный и конечный цвет фильтра
    hsv_min = np.array((h1, s1, v1), np.uint8)
    hsv_max = np.array((h2, s2, v2), np.uint8)

    # накладываем фильтр на кадр в модели HSV
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)

    cv2.imshow('result', thresh) 
 
    if cv2.waitKey(50) & 0xff == ord('q'):
        break  

cap.release()
cv2.destroyAllWindows()

X=496# х-координата середины желтой части поршня
cap = cv2.VideoCapture('150Э.mp4')
#hsv_min = np.array((21, 0, 0), np.uint8)
#hsv_max = np.array((123, 177, 187), np.uint8)
Y=[]

color_yellow = (0,255,255)
while True:
    flag, img = cap.read()
    if flag ==False:
        break
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)
    cv2.imshow('result', thresh) 
    for i in range(480,800):
        if thresh[X][i]==255:
            Y.append(i)
            print(i)
            cv2.circle(img, (X, i), 5, color_yellow, 2)
            break
    cv2.circle(img, (X, 480), 3, (0,255,0), 2)
    cv2.circle(img, (X, 800), 3, (0,255,0), 2)
    cv2.imshow('result', img) 
    if cv2.waitKey(50) & 0xff == ord('m'):
        break  
print(thresh)    
cap.release()
cv2.destroyAllWindows()
import pandas as pd
df = pd.DataFrame(Y)
df.to_excel(excel_writer = "porh_Y_150_hsv1.xlsx",)