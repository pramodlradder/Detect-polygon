import numpy as np
import cv2

img = cv2.imread('/path to image/polygon.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#np.set_printoptions(threshold=np.nan) print all array elements

ret,thresh = cv2.threshold(gray,200,255,0)#threshould value less than that will be 0 else max value(ret) 2 nd parameter
#print(ret,thresh)
contours,h = cv2.findContours(thresh,cv2.RETR_TREE,2)#tree hirarchical numbering  h number of counters 
copy = img.copy()
#3rd parameter contour number
#print(contours)
#print(h)

#image polygon.png for circle
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 1)
#print(circles)
for i in circles[0,:]:
    print("circle")
    cv2.circle(copy,(i[0],i[1]),i[2],(0,255,0),2)
    
    
#image other than circle
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    #print(len(approx))
    if len(approx)==4:
        print("square")
        cv2.drawContours(copy, [cnt],0, (0,255,0), 3) 
    elif len(approx)==3:
        print("triangle")
        cv2.drawContours(copy, [cnt],0, (255,0,0), 3)
    elif len(approx)==5:
        print("pentagon")
        cv2.drawContours(copy, [cnt],0, (255,0,255), 6)
    elif len(approx)==6:
        print("hexagon")
        cv2.drawContours(copy, [cnt],0, (25,55,0), 10)
    

cv2.imshow("origanal image",img)

cv2.imshow("gray image",gray)
cv2.imshow("threasimage",thresh)        
cv2.imshow("image",copy)
cv2.waitKey(0)
cv2.destroyAllWindows()











