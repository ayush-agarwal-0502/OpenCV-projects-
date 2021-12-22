#made by Ayush Agarwal
#importing the libraries
import cv2
import pytesseract
#calling in the tesseract library from the place where we stored it on the machine
pytesseract.pytesseract.tesseract_cmd = (r'C:/Program Files/Tesseract-OCR/tesseract.exe')
#bringing in the images
#img1 = cv2.imread('C:/Users/ayush/OneDrive/Desktop/image processing/text_image_sample_1.png')
img1 = cv2.imread('C:/Ayush_Data_/image processing and other python projects/text_image_sample_1.png')
img2 = cv2.imread('C:/Users/ayush/OneDrive/Desktop/image processing/text_image_sample_2.jpg')
img3 = cv2.imread('C:/Users/ayush/OneDrive/Desktop/image processing/text_image_sample_3.jfif')
#we are processing on 'img' , instead of changing it everywhere in the code we can easily put img=img1... etc
img = img1
#showing the unprocessed image
cv2.imshow("unprocessed image ",img)
#pytesseract works on rgb whereas opencv works on bgr so we need to convert to rgb
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#as usual , for better analysis we convert to grayscale
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#removing the noise via the blurring
img = cv2.medianBlur(img,5)
#thresholding to make the text darker
img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
#in the end we need it coloured so that we can see the colour of the rectangles
img=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)

#simple yet most important function in pytesseract
#gives the text in image as output in python
print(pytesseract.image_to_string(img,lang='eng'))
#function to get the version of pytesseract
print("pytesseract version used in this program is "+str(pytesseract.get_tesseract_version()))
#to get the total height and width of the image
W,H,_ = img.shape
#image to boxes is used for detecting the letters
boxes1 = pytesseract.image_to_boxes(img)
print(boxes1)
counter = 0
#splitlines splits the data according to the new lines between them
for box in boxes1.splitlines() :
    counter = counter + 1
    #in each line the data is split by a gap of a space , so we make them into groups of data
    # so that each detected letter has an array of data dedicated to it
    box = box.split(' ')
    x1,y1,w1,h1 = int(box[1]),int(box[2]),int(box[3]),int(box[4])
    #the problem is that in opencv the origin is at left top whereas in pytesseract it is at bottom left
    #so whenever we use their functions , they return coordinates according to their own origin
    #so we need to do the math and convert them properly
    #code to draw rectangles around each letter
    cv2.rectangle(img,((x1),(W-y1)),((w1),(W-h1)),(0,255,0),2)
    cv2.putText(img,box[0],((x1),(W-y1+20)),cv2.FONT_HERSHEY_SIMPLEX,1.25,(255,0,0),2)
boxes2 = pytesseract.image_to_data(img)
print(boxes2)
boxes2 = boxes2.splitlines()
print(boxes2)

for x,b in enumerate(boxes2):
    #since the first few outputs explain the data types returned , we need to get rid of the first subarray
    #hence we used enumerate
    if x!=0:
        #now further splitting the subaaray to get the data
        b = b.split()
        #print(b)
        if(len(b)==12):
            #intrestingly , the image_to_data function returns w and h as in opencv , and even returns as per the
            #coordinate system convention followed by opencv hence we can put these in
            x2,y2,w2,h2 = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            #drawing recatngles around the detected word
            cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),(0,0,255),3)
            #printing the detected text above the rectangle
            cv2.putText(img,b[11],(x2,y2-int((h2)/50)),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,0,0),2)
#displaying the number of words detected using the variable named counter
img = cv2.putText(img,"no of words detected "+str(counter),(0,15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
#showing the image after processing , word detection
cv2.imshow("image with text ",img)

cv2.waitKey(0)
cv2.destroyAllWindows()


