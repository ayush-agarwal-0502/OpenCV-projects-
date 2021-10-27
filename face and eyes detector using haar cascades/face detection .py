########################################################################
#made by Ayush Agarwal, Electronics engineering , IIT BHU Varanasi
#Face and eyes detector using haar cascades
########################################################################
#importing the libraries
import cv2
import numpy as np
#getting the cascades, which are availaible on github easily
face_cascade = cv2.CascadeClassifier('C:/Users/ayush/PycharmProjects/image processing/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier("C:/Users/ayush/PycharmProjects/image processing/haarcascade_eye.xml")
body_cascade = cv2.CascadeClassifier("C:/Users/ayush/PycharmProjects/image processing/haarcascade_upperbody.xml")
#setting up the input from the camera
capture = cv2.VideoCapture(0)
while True :
    returnvalue , frame = capture.read()
    frame = cv2.flip(frame,100)
    if(returnvalue==True):
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #method to detect the cascades using the cascade library given above
        faces = face_cascade.detectMultiScale(gray,1.1,5)
        bodies = body_cascade.detectMultiScale(gray,1.05,5)
        #the detectmultiscale function returns a list of rectangles , its parameters are img , scalefactors and minneighbours
        #scalefactor is complicated , but the more it is to 1 , the faster code will run but more faces it will miss
        #drawing rectangles around the detected bodies
        for (bx,by,bw,bh) in bodies :
            cv2.rectangle(frame,(bx,by),(bx+bw,by+bh),(0,0,255),4)
            #drawing the rectangles around the face detected
        for (x,y,w,h) in faces :
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
            #writing "face" over the detected face
            cv2.putText(frame,"Face",(x+5,y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),4)
            #detecting the eyes inside the detected face
            eyes = eye_cascade.detectMultiScale(gray[y:y+h , x:x+w],1.1,5)
            for (ex,ey,ew,eh) in eyes :
                #cv2.rectangle(frame[y:y+h , x:x+w],(ex,ey),(ex+ew,ey+eh),(255,0,0),3)
                #drawing the circle around the eyes
                cv2.circle(frame[y:y+h , x:x+w],(ex+int(ew/2),ey+int(eh/2)),(int((ew+eh)/4)),(255,0,0),2)
        #the video display stops when the q button is pressed , standard opencv way to stop the video
        if cv2.waitKey(5) == ord('q'):
            break
        cv2.imshow("webcam feed ",frame)
    else :
        print("ERROR in loading the video ")
capture.release()
cv2.destroyAllWindows()
