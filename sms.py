import requests
def call():
    url = "https://www.fast2sms.com/dev/bulk"   # SMS service

    API_KEY = "MFdvoWxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"     # Add API_KEY
    to_num = "98765xxxxx"       # Add registered phone number

    f=open('log.txt','r')
    msg = f.read()
    f.close

    payload = "sender_id=FSTSMS&message="+msg+"&language=english&route=p&numbers="+to_num
    headers = {
    'authorization': API_KEY,
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print("SMS has been sent...")
