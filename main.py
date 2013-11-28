import cv2

cv2.namedWindow("Webcam Feed")
vc = cv2.VideoCapture(0)

vc.set(3, 640)
vc.set(4, 480)

rval, frame = vc.read()

me = cv2.imread("orange.png")

xoff = 0
yoff = 0

while True:
    if rval:
        scores = cv2.matchTemplate(frame, me, cv2.TM_SQDIFF_NORMED)
        minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(scores)

        if minVal < 0.42:
            cv2.circle(frame, (minLoc[0]+60+xoff, minLoc[1]+60+yoff), 50, (255, 255, 255), 2)
            cv2.putText(frame, "Orange.", (minLoc[0]+xoff+10, minLoc[1]+yoff+140), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(20, 20, 155))
        else:
            print minVal
        cv2.imshow("Webcam Feed", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 0:
        yoff += 5
        print "x: %s, y: %s" % (xoff, yoff)
    elif key == 1:
        yoff -= 5
        print "x: %s, y: %s" % (xoff, yoff)
    elif key == 2:
        xoff += 5
        print "x: %s, y: %s" % (xoff, yoff)
    elif key == 3:
        xoff -= 5
        print "x: %s, y: %s" % (xoff, yoff)
    elif key == ord('q'):
        break



    rval, frame = vc.read()