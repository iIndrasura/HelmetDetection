#!/usr/bin/python

import os
import cv2
import time
import json
import base64
import urllib
import imutils
import requests
import numpy as np
import subprocess

USER1 = 500
USER2 = 500
USER3 = 500
USER4 = 500

def camera():
    
    url="http://192.168.43.108:8080//shot.jpg"
    imgPath=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    img=imutils.resize(img,width=600)
    cv2.imshow("frame",img)
    return img



while True:
    
    img = camera()
    key = cv2.waitKey(5) & 0xff
    
    if ( key == ord('q')):
        
        cv2.destroyAllWindows()       
        print"Captured..."
        cv2.imwrite("first.jpg",img)       
        time.sleep(5)        
        IMAGE_PATH = 'first.jpg'
        SECRET_KEY = 'sk_DEMODEMODEMODEMODEMODEMO'

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
            print"Address: Hyderabad"        
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
                subprocess.Popen('python sms.py',shell=True).communicate()
            else:
                USER1 = USER1-100
                print(USER1)
                data = "RS:100 debited your account\n Remaing amount: %d"%USER1
                f=open('log.txt','w')
                f.write(data)
                f.close()
                subprocess.Popen('python sms.py',shell=True).communicate()
         

        elif number == "AWEB8S4":

            print"----------------------------"     
            print"Owner Name: Bharath"
            print"Vehicle Nmuber: %s"%number
            print"Address: Hyderabad"
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
                subprocess.Popen('python sms.py',shell=True).communicate()
            else:
                USER2 = USER2-100
                print(USER2)
                data = "RS:100 debited your account\n Remaing amount: %d"%USER2
                f=open('log.txt','w')
                f.write(data)
                f.close()
                subprocess.Popen('python sms.py',shell=True).communicate()


        elif number == "8R61147":

            print"----------------------------" 
            print"Owner Name: Kumar"
            print"Vehicle Nmuber: %s"%number
            print"Address: Hyderabad"
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
                subprocess.Popen('python sms.py',shell=True).communicate()
            else:
                USER3 = USER3-100
                print(USER3)
                data = "RS:100 debited your account\n Remaing amount: %d"%USER3
                f=open('log.txt','w')
                f.write(data)
                f.close()
                subprocess.Popen('python sms.py',shell=True).communicate()

                

        elif number == "MXT4696":

            print"----------------------------"     
            print"Owner Name: sankar"
            print"Vehicle Nmuber: %s"%number
            print"Address: Hyderabad"
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
                subprocess.Popen('python sms.py',shell=True).communicate()
            else:
                USER4 = USER4-100
                print(USER4)
                data = "RS:100 debited your account\n Remaing amount: %d"%USER4
                f=open('log.txt','w')
                f.write(data)
                f.close()
                subprocess.Popen('python sms.py',shell=True).communicate()
