import cv2
from cvzone.HandTrackingModule import HandDetector 

Detector=HandDetector(maxHands=1,detectionCon=0.8,)
cap=cv2.VideoCapture(0)
cap.set(3,1000)
cap.set(4,1000)
cap.set(10,100)
mypoints=[]

def draw(img,mypoints):
    for points in mypoints:
        cv2.circle(img,(points[0],points[1]),10,(255,0,0),cv2.FILLED)
while True:
    succes,img=cap.read()
    img=cv2.flip(img,1)
    hands,img=Detector.findHands(img,flipType=True,draw=False)
    if hands:
        lmList=hands[0]["lmList"]
        fingers=Detector.fingersUp(hands[0])
        if fingers[1]==1 and fingers.count(1)==1:
           mypoints.append(lmList[8][0:2])
    if len(mypoints)!=0:
        draw(img,mypoints)   
    cv2.imshow("IMG",img)
    if cv2.waitKey(1)==ord("q"):
        break
