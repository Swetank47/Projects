import cv2
import numpy as np

dratio={}
l=["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png","10.png"]

for j in l:
    #Creating image with only burnt area
    img=cv2.imread(j)
    img2=cv2.imread("burnt.png")
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower=np.array([1,0,0])
    upper=np.array([31,255,255])
    mask=cv2.inRange(imghsv,lower,upper)#creating mask with required parameters to select only burnt area
    imgresultburnt=cv2.bitwise_and(img2,img2,mask=mask)
    img=imgresultburnt.copy()

    #Finding number of homes in burnt area
    def getcont(img):
        cont,hier=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #getting contours
        global c
        c=0
        for i in cont:
            area=cv2.contourArea(i) #getting area
            if area>500: #to avoid noise
                cv2.drawContours(imgcont,i,-1,(255,0,0),1) #drawing all contours(i)
                peri=cv2.arcLength(i,True) #gettng perimeter of contour
                approx=cv2.approxPolyDP(i,0.02*peri,True)
                objcor=len(approx)
                x,y,w,h=cv2.boundingRect(approx)
                cv2.rectangle(imgcont,(x,y),(x+w,y+h),(92,213,40),30)
                if objcor==3:                
                    c=c+1
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#converting image to grayscale
    imgblur=cv2.GaussianBlur(imggray,(21,21),1)#blurring the grayscale image for canny function
    imgcanny=cv2.Canny(imgblur,150,150)
    imgcont=img.copy()
    getcont(imgcanny)
    burnttri=c

    #Creating image with only unburnt area
    img=cv2.imread(j)
    img2=cv2.imread("unburnt.png")
    lower=np.array([36,0,0])
    upper=np.array([179,254,255])
    mask=cv2.inRange(imghsv,lower,upper)#creating mask with required parameters to select only unburnt area
    imgresultunburnt=cv2.bitwise_and(img2,img2,mask=mask)

    #Finding number of homes in unburnt area
    def getcont(img):
        cont,hier=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #getting contours
        global c
        c=0
        for i in cont:
            area=cv2.contourArea(i) #getting area
            if area>500: #to avoid noise
                cv2.drawContours(imgcont,i,-1,(255,0,0),1) #drawing all contours(i)
                peri=cv2.arcLength(i,True) #gettng perimeter of contour
                approx=cv2.approxPolyDP(i,0.02*peri,True)
                objcor=len(approx)
                if objcor==3:                
                    c=c+1
    imggray=cv2.cvtColor(imgresultunburnt,cv2.COLOR_BGR2GRAY)
    imgblur=cv2.GaussianBlur(imggray,(21,21),1)
    imgcanny=cv2.Canny(imgblur,150,150)
    imgcont=img.copy()
    getcont(imgcanny)
    cv2.waitKey(0)
    unburnt=c

    #Creating image with only blue houses
    img=cv2.imread(j)
    img2=cv2.imread("blue.png")
    white=cv2.imread("white.png")
    lower=np.array([110,0,0])
    upper=np.array([179,255,255])
    mask=cv2.inRange(imghsv,lower,upper)#creating mask with required parameters to select only blue area
    imgresultblue=cv2.bitwise_and(img2,img2,mask=mask)
    imgcopy=cv2.bitwise_and(white,white,mask=mask)

    #Getting number of blue houses
    def getcont(img):
        cont,hier=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #getting contours
        global c
        c=0
        for i in cont:
            area=cv2.contourArea(i) #getting area
            if area>500: #to avoid noise
                cv2.drawContours(imgcont,i,-1,(255,0,0),1) #drawing all contours(i)
                peri=cv2.arcLength(i,True) #gettng perimeter of contour
                approx=cv2.approxPolyDP(i,0.02*peri,True)
                objcor=len(approx)
                x,y,w,h=cv2.boundingRect(approx)
                cv2.rectangle(imgcont,(x,y),(x+w,y+h),(92,213,40),30)
                if objcor==3:                
                    c=c+1
    imggray=cv2.cvtColor(imgcopy,cv2.COLOR_BGR2GRAY)
    imgblur=cv2.GaussianBlur(imggray,(21,21),1)
    imgcanny=cv2.Canny(imgblur,150,150)
    imgcont=img.copy()
    getcont(imgcanny)
    blue=c

    #Creating image with only red houses
    img=cv2.imread(j)
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img2=cv2.imread("red.png")
    lower=np.array([0,255,255])
    upper=np.array([62,255,255])
    mask=cv2.inRange(imghsv,lower,upper)#creating mask with required parameters to select only red houses
    imgresultred=cv2.bitwise_and(img2,img2,mask=mask)

    #Getting number of houses on burnt grass
    def getcont(img):
        cont,hier=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #getting contours
        global c
        c=0
        for i in cont:
            area=cv2.contourArea(i) #getting area
            if area>500: #to avoid noise
                cv2.drawContours(imgcont,i,-1,(255,0,0),1) #drawing all contours(i)
                peri=cv2.arcLength(i,True) #gettng perimeter of contour
                approx=cv2.approxPolyDP(i,0.02*peri,True)
                objcor=len(approx)
                x,y,w,h=cv2.boundingRect(approx)
                cv2.rectangle(imgcont,(x,y),(x+w,y+h),(92,213,40),30)
                if objcor==3:                
                    c=c+1
    imggray=cv2.cvtColor(imgresultred,cv2.COLOR_BGR2GRAY)
    imgblur=cv2.GaussianBlur(imggray,(21,21),1)
    imgcanny=cv2.Canny(imgblur,150,150)
    imgcont=img.copy()
    getcont(imgcanny)
    burnt=c

    img=imgcont.copy()
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([36,0,0])
    upper = np.array([179,255,255])
    mask = cv2.inRange(imgHsv,lower,upper)
    fakeimg=cv2.bitwise_and(white,white,mask=mask)

    #Getting number of blue houses on burnt grass
    def getcont(img):
        cont,hier=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #getting contours
        
        global c
        c=0
        for i in cont:
            area=cv2.contourArea(i) #getting area
            if area>500: #to avoid noise
                cv2.drawContours(imgcont,i,-1,(255,0,0),1) #drawing all contours(i)
                peri=cv2.arcLength(i,True) #gettng perimeter of contour
                approx=cv2.approxPolyDP(i,0.02*peri,True)
                objcor=len(approx)
                if objcor==3:                
                    c=c+1
    imggray=cv2.cvtColor(fakeimg,cv2.COLOR_BGR2GRAY)
    imgblur=cv2.GaussianBlur(imggray,(21,21),1)
    imgcanny=cv2.Canny(imgblur,150,150)
    imgcont=img.copy()
    getcont(imgcanny)
    blueburnt=c

    redburnt=burnt-blueburnt
    red=burnt+unburnt-blue
    blueunburnt=blue-blueburnt

    print("Details for",j,":-")

    lhouses=[burnt,unburnt]
    print("Houses on burnt grass:",lhouses[0],"; Houses on unburnt grass:",lhouses[1])
    
    #calculating and printing the total priorities in both areas
    lprior=[(blueburnt*2)+(redburnt),(blueunburnt*2)+(red-redburnt)]
    print("Priority of houses on burnt grass:",lprior[0],"; Priority of houses on unburnt grass:",lprior[1])

    #calculating and printing the rescue ratio
    ratio=((blueburnt*2)+(redburnt))/((blueunburnt*2)+(red-redburnt))
    dratio[j]=ratio#adding key and values(image name rescue ratio)
    print("Rescue Ratio=",ratio)
    print()

    #blending images together
    homes=cv2.addWeighted(imgresultred,1,imgresultblue,1,0)
    grass=cv2.addWeighted(imgresultburnt,1,imgresultunburnt,1,0)
    final=cv2.addWeighted(homes,1,grass,1,0)
    finalcrop=cv2.resize(final,(300,300))
    cv2.imshow(j,finalcrop)
    cv2.waitKey(0)

#Printing the imgage name in descending order of rescue ratio
sorted = sorted(dratio.items(), key=lambda x:x[1], reverse=True)
converted = dict(sorted)
print("Images sorted by rescue ratio:",end="")
for j in converted:
    print(j,", ",end="")