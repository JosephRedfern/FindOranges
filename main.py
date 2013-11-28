import cv2

cv2.namedWindow("Webcam Feed")
vc = cv2.VideoCapture(0)

#vc.set(3, 240)
#vc.set(4, 360)

rval, frame = vc.read()

me = cv2.imread("pencil.png")


while True:
    if rval:
        scores = cv2.matchTemplate(frame, me, cv2.TM_CCOEFF_NORMED)
        minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(scores)
        cv2.rectangle(frame, (minLoc[0]+me.shape[1], minLoc[1]-me.shape[0]), (minLoc[0], minLoc[1]), color=(0,0,255), thickness=-1)
        cv2.imshow("Webcam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    rval, frame = vc.read()