import cv2

cv2.namedWindow("TheresWally")
vc = cv2.VideoCapture(0)

rval, frame = vc.read()

me = cv2.imread("wally.png")

xoff = 0
yoff = 0

while True:
    if rval:
        scores = cv2.matchTemplate(frame, me, cv2.TM_SQDIFF_NORMED)
        minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(scores)

        if minVal < 0.2:
            cv2.rectangle(frame, minLoc, (minLoc[0]+40+xoff , minLoc[1]+40+yoff), thickness=4 ,color=(0 , 0, 255))
            cv2.putText(frame, "Wally?", (minLoc[0]+xoff+10, minLoc[1]+yoff+60), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0, 0, 255))
        else:
            print minVal
        cv2.imshow("TheresWally", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 81:
        yoff += 5
        print "x: %s, y: %s" % (xoff, yoff)
    elif key == 83:
        yoff -= 5
        print "x: %s, y: %s" % (xoff, yoff)
    elif key == 85:
        xoff += 5
        print "x: %s, y: %s" % (xoff, yoff)
    elif key == 84:
        xoff -= 5
        print "x: %s, y: %s" % (xoff, yoff)
    elif key == ord('q'):
        break
    rval, frame = vc.read()
