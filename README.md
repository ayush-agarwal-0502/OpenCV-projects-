# OpenCV-projects
Set of mini projects I did using an OpenCV , an image processing library in python

## Implementing Kalman Filter using opencv 
Skills : Probablistic robotics - recursive state estimation using a parametric filter known as extended kalman filter , image processing using opencv 

This deserves its own github page , hence here is the link : https://github.com/ayush-agarwal-0502/Kalman-filter-using-opencv

![image](https://user-images.githubusercontent.com/86561124/138936084-40a43619-69d0-4138-b186-f9c00936bd4b.png)

## Motion Detector using opencv 

Skills : OpenCV

Used OpenCV skills to build a motion detector for a video camera . Took in 2 images at very small time gap , took absolute difference of them , performed image processing ( like converting to grayscale , gaussian blur , dilating , blurring ) on the difference image , then used find contours function to detect the moving objects (since the moving objects will be at different positions in the 2 images , the difference will be non zero ) , also found number of contours , thresholded the detected contours based on a certain area value , then drew a rectangle around the objects . then using the puttext function , wrote the number of objects detected , also wrote "something is moving " or "something is not moving " , and also an additional feature of giving warning if the moving object is close to the camera ( which would be when the area of the contour is very large compared to that of the screen )

![image](https://user-images.githubusercontent.com/86561124/139123682-2cc6692a-dd6c-4473-b42b-a153a67efa2d.png)
(Would work better if this is deployed on cctv cameras as the moving objects will be smaller hence properly detected and enclosed in rectangles, in the picture , the hand moved more than the object (cube) hence got detected more.)


## Face detector using opencv and haar cascades 

Skills : Haar Cascades , OpenCV

Haar cascades source : https://github.com/anaustinbeing/haar-cascade-files

Haar Cascades documentation : https://docs.opencv.org/4.5.3/db/d28/tutorial_cascade_classifier.html

Haar Cascades is a library in python which is used along with opencv to detect face , eyes ... anything you want (and its haar cascade is availaible) in the image or video . 
This library internally consists of trained machine learning models to detect the features .

![image](https://user-images.githubusercontent.com/86561124/139127185-1447df21-8116-4fe7-ad8e-52442ebd8950.png)

## Image to text using opencv and pytesseract 

Skills: OpenCV , PyTesseract 

Pytesseract is a python library used to detect the words , characters in an image . I have printed the individual detected characters , as well as the complete words over the image .

![image](https://user-images.githubusercontent.com/86561124/147068012-3359a39b-6bdd-48e6-93e7-e387441f7c92.png)

