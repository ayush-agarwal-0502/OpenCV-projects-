#######################################
#made by Ayush Agarwal, Electronics engineering , IIT BHU Varanasi
#######################################
#importing the libraries
import cv2
import numpy as np
#getting the video
cap = cv2.VideoCapture(0)
#standard opencv way to start
while True :
    ret , frame1 = cap.read()
    if (ret == True ):
        #flipping it so that it is like my reflection , comfortable to use 
        frame1 = cv2.flip(frame1,100)
        #took 2 frame readings as we will need to find the difference between them to detect motion
        _ , frame2 = cap.read()
        #flipped both of them so that it is mirror mode of real me
        frame2 = cv2.flip(frame2,100)
        #took absolute difference as the motion will cause the diff in position of object in 2 images
        #and this diff will show up as white patches
        diff = cv2.absdiff(frame1,frame2)
        #changed it to grayscale for easier working
        diff = cv2.cvtColor(diff , cv2.COLOR_BGR2GRAY)
        #applied gaussian blur for smoothening
        diff = cv2.GaussianBlur(diff,(5,5),0)
        #threshold makes the minute absdiff become 255 which will properly show as full white colour hence
        # easier to find as a contour
        _,diff = cv2.threshold(diff,20,255,cv2.THRESH_BINARY)
        #small adjustments using dilate
        diff = cv2.dilate(diff,(5,5),iterations=3)
        #now we will find the contours in the diff , which will be the places in image where there was motion
        contours,_ = cv2.findContours(diff,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #j is a variable i used to count the objects
        j=0
        for contour in contours :
            #this if condition helps detect real objects and reduce noise(random small patches that get detected )
            if(cv2.contourArea(contour)>=700):
                x, y, w, h = cv2.boundingRect(contour)
                #putting a rectangle over the detected object
                cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),4)
                #this should draw outlines along the contours but somehow not working
                #cv2.drawContours(frame1,contours,j+1,(255,255,255),4)
                #printing the id no of the object and the coordinates of the center of the rectangle on the rectangle
                cv2.putText(frame1,str(j)+" , "+str((int(x+int(w/2)),int(y+int(h/2)))),(x,y+10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0),4)
                #when something approaches the camera , obviously its rectangle will get too big hence we give warning
                if(cv2.contourArea(contour)>=10000):
                    print("Danger!! , something very close to camera")
                j = j+1
        #no of objects detected will be j (no of contours with size more than the given size )
        cv2.putText(frame1,"no of objects detected = "+str(j) , (0,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),3)
        #if there is something moving detected , we print something moving and vice versa
        if(j>0):
            cv2.putText(frame1,"Something is moving ",(int(cap.get(3))-400 , int(cap.get(4))-20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,0),1)
        else :
            cv2.putText(frame1,"Nothing is moving ",(int(cap.get(3))-400 , int(cap.get(4))-20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,0),1)
        #showing the videos
        cv2.imshow("diff gray ",diff)
        cv2.imshow("webcam feed ",frame1)
        #shifting between the frames
        frame1=frame2
        frame2 = cap.read()
        #standard opencv trick to stop when q pressed
        if cv2.waitKey(5) == ord('q'):
            break
    else :
        print("Error in getting the video " )
cap.release()
cv2.destroyAllWindows()
