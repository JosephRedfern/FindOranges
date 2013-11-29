import cv2

cv2.namedWindow("Webcam Feed", cv2.CV_WINDOW_AUTOSIZE)
#vc = cv2.VideoCapture(0)

#vc.set(3, 640)
#vc.set(4, 480)

needle = cv2.imread("WallyFace.jpg")
haystack = cv2.imread("WallyStack.jpg")

xoff = 0
yoff = 0

scores = cv2.matchTemplate(haystack, needle, cv2.TM_SQDIFF_NORMED)
minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(scores)

if minVal < 0.40:
    cv2.circle(haystack, minLoc, 40, (0, 0, 255), 10)
#    cv2.putText(haystack, "Wally?", minLoc, fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(20, 20, 155))
else:
    print minVal
    haystack = scores


newx,newy = haystack.shape[1]/3,haystack.shape[0]/3 #new size (w,h)
newimage = cv2.resize(haystack ,(newx,newy))
cv2.imshow("Webcam Feed", newimage)

while True:
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
