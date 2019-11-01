from datetime import datetime
import cv2

cam = cv2.VideoCapture(0) # select camera feed
cam.set(cv2.CAP_PROP_FPS, 15) # Set fram rate
cam.set(3, 1280) # set x resolution 1920
cam.set(4, 720) # # set y resolution 720p 1080p
font = cv2.FONT_HERSHEY_TRIPLEX

fourcc = cv2.VideoWriter_fourcc(*'XVID') # set codec (*'DIVX')

#                              filename     codecc FPS   output resolution
out = cv2.VideoWriter('output.avi', fourcc, 15, (1280, 720))

while True:
    re, img = cam.read()# setting the camera feed to return a image

    img = cv2.flip(img, 1) #flip to mirror view
    #           video           string                      position font  size  colour  stroke thickness
    cv2.putText(img, "You Got Caught Stealin",(300,400), font, 2, (0,0,255), 2, cv2.LINE_AA)
    cv2.putText(img, str(datetime.now()), (900, 600), font, .5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow('Newtons Video', img) # displays camera feed

    out.write(img)

    K = cv2.waitKey(27) & 0xff #
    if K == 27: # every escape key to end loop
        break #
cam.release()
cv2.destroyAllWindows()

