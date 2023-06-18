#opencv 2.4.13

import cv2
import numpy as np
#import serial
import time
import subprocess
import urllib
import json
import base64
import requests
import sms

USER1 = 500
USER2 = 500
USER3 = 500
USER4 = 500

haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'  #All the faces data will be present this folder

face_cascade = cv2.CascadeClassifier(haar_file)
count = 1
MIN_MATCH_COUNT=40
lt=1;
gt=1;
detector=cv2.SIFT()

FLANN_INDEX_KDITREE=0
flannParam=dict(algorithm=FLANN_INDEX_KDITREE,tree=5)
flann=cv2.FlannBasedMatcher(flannParam,{})

trainImg=cv2.imread("11.jpg",0)
trainImg2=cv2.imread("22.jpg",0)

trainKP1,trainDesc1=detector.detectAndCompute(trainImg,None)
trainKP2,trainDesc2=detector.detectAndCompute(trainImg2,None)
url="http://192.168.43.1:8080/shot.jpg"
FLAG=1
while True:
    FLAG=0
    imgPath=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
    QueryImgBGR=cv2.imdecode(imgNp,-1)
    
    QueryImg=cv2.cvtColor(QueryImgBGR,cv2.COLOR_BGR2GRAY)
    queryKP,queryDesc=detector.detectAndCompute(QueryImg,None)
    matches1=flann.knnMatch(queryDesc,trainDesc1,k=2)
    matches2=flann.knnMatch(queryDesc,trainDesc2,k=2)
    
    for i in range(1,3):
        if i==1:
            matches=matches1;
            trainKP=trainKP1;
            trainDesc=trainDesc1;
        elif i==2:
            matches=matches2;
            trainKP=trainKP2;
            trainDesc=trainDesc2;
        goodMatch=[]
        for m,n in matches:
            if(m.distance<0.75*n.distance):
                goodMatch.append(m)
        if(len(goodMatch)>MIN_MATCH_COUNT):
            tp=[]
            qp=[]
            for m in goodMatch:
                tp.append(trainKP[m.trainIdx].pt)
                qp.append(queryKP[m.queryIdx].pt)
            tp,qp=np.float32((tp,qp))
            H,status=cv2.findHomography(tp,qp,cv2.RANSAC,3.0)
            h,w=trainImg.shape
            trainBorder=np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
            queryBorder=cv2.perspectiveTransform(trainBorder,H)
            if i==1:
                cv2.putText(QueryImgBGR, "HELMET DETECTED ", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                print('#############  HELMET DETECTED  ############')
                FLAG=1
                time.sleep(2)
            elif i==2:
                cv2.putText(QueryImgBGR, "HELMET DETECTED", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                print('#############  HELMET DETECTED  ############')
                time.sleep(2)
                FLAG=1
        else:
            print "Scanning"
        if FLAG==0:
            x=y=w=h=0
            gray = cv2.cvtColor(QueryImgBGR, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 4)
            for (x,y,w,h) in faces:
                cv2.rectangle(QueryImgBGR,(x,y),(x+w,y+h),(255,0,0),2)
                face = gray[y:y + h, x:x + w]
                face_resize = cv2.resize(face, (w, h))
                face_resize
            count += 1
            if x>0:
                print ('Alert !! Face Detected the person Didnt Wear Helmet')
                print ('Recognizing Licence Plate')
                print"Captured..."
                time.sleep(10)
                imgPath=urllib.urlopen(url)
                imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
                QueryImgBGR=cv2.imdecode(imgNp,-1)
                img=QueryImgBGR;
                cv2.imwrite("first.jpg",img)       
                time.sleep(5)        
                IMAGE_PATH = 'first.jpg'
                SECRET_KEY = 'sk_c97f03fb6a6ba32bfe28407b'

                with open(IMAGE_PATH, 'rb') as image_file:
                    img_base64 = base64.b64encode(image_file.read())

                url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
                r = requests.post(url, data = img_base64)

                num_plate=(json.dumps(r.json(), indent=2))
                #print(num_plate)
                info=(list(num_plate.split("candidates")))
                plate=info[1]
                plate=plate.split(',')[0:3]
                p=plate[1]
                p1= p.split(":")
                number=p1[1]
                number=number.replace('"','')
                number=number.lstrip()
                print number        

                if number == "1B70440":
                    print"----------------------------"    
                    print"Owner Name: RAHUL"
                    print"Vehicle Nmuber: %s"%number
                    print"Address: Chennai"        
                    if(USER1 < 200):
                        print(" Low Balance !!!!!!!!!")
                        data = "Low Balance !!!!!!!!!"
                        f=open('log.txt','w')
                        f.write(data)
                        f.close()
                    elif(USER1 <= 300):
                        USER1 = USER1-100
                        print(USER1)
                        print(" Alert Plz Recharge.........")
                        data = "Alert Plz Recharge.........\n   RS:100 debited your account\n Remaing amount: %d"%USER1
                        f=open('log.txt','w')
                        f.write(data)
                        f.close()
                        sms.call()
                    else:
                        USER1 = USER1-100
                        print(USER1)
                        data = "RS:100 debited your account\n Remaing amount: %d"%USER1
                        f=open('log.txt','w')
                        f.write(data)
                        f.close()
                        sms.call()
                elif number == "AWEB8S4":
                    print"----------------------------"     
                    print"Owner Name: Bharath"
                    print"Vehicle Nmuber: %s"%number
                    print"Address: Chennai"
                    if(USER2 < 200):
                        print(" Low Balance !!!!!!!!!")
                        data = "Low Balance !!!!!!!!!"
                        f=open('log.txt','w')
                        f.write(data)
                        f.close()
                    elif(USER2 <= 300):
                        USER2 = USER2-100
                        print(USER2)
                        print(" Alert Plz Recharge.........")
                        data = "Alert Plz Recharge.........\n   RS:100 debited your account\n Remaing amount: %d"%USER2
                        f=open('log.txt','w')
                        f.write(data)
                        f.close()
                        sms.call()
                    else:
                        USER2 = USER2-100
                        print(USER2)
                        data = "RS:100 debited your account\n Remaing amount: %d"%USER2
                        f=open('log.txt','w')
                        f.write(data)
                        f.close()
                        sms.call()

                elif number == "8R61147":
                    print"----------------------------" 
                    print"Owner Name: Kumar"
                    print"Vehicle Nmuber: %s"%number
                    print"Address: Chennai"
                    if(USER3 < 200):
                        print(" Low Balance !!!!!!!!!")
                        data = "Low Balance !!!!!!!!!"
                        f=open('log.txt','w')
                        f.write(data)
                        f.close()
                    elif(USER3 < 300):
                        USER3 = USER3-100
                        print(USER3)
                        print(" Alert Plz Recharge.........")
                        data = "Alert Plz Recharge.........\n   RS:100 debited your account\n Remaing amount: %d"%USER3
                        f=open('log.txt','w')
                        f.write(data)
                        f.close()
                        sms.call()
                    else:
                        USER3 = USER3-100
                        print(USER3)
                        data = "RS:100 debited your account\n Remaing amount: %d"%USER3
                        f=open('log.txt','w')
                        f.write(data)
                        f.close()
                        sms.call()

                elif number == "MXT4696":

                    print"----------------------------"     
                    print"Owner Name: sankar"
                    print"Vehicle Nmuber: %s"%number
                    print"Address: Chennai"
                    if(USER4 < 200):
                        print(" Low Balance !!!!!!!!!")
                        data = "Low Balance !!!!!!!!!"
                        f=open('log.txt','w')
                        f.write(data)
                        f.close()
                    elif(USER4 < 300):
                        USER4 = USER4-100
                        print(USER4)
                        print(" Alert Plz Recharge.........")
                        data = "Alert Plz Recharge.........\n   RS:100 debited your account\n Remaing amount: %d"%USER4
                        f=open('log.txt','w')
                        f.write(data)
                        f.close()
                        sms.call()
                    else:
                        USER4 = USER4-100
                        print(USER4)
                        data = "RS:100 debited your account\n Remaing amount: %d"%USER4
                        f=open('log.txt','w')
                        f.write(data)
                        f.close()
                        sms.call()
    cv2.imshow('result',QueryImgBGR)
    if cv2.waitKey(10)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()


