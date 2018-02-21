#!/usr/bin/python3

import requests

def hodor_1024(id):
    URL = "http://158.69.76.135/level0.php"
    payload = {
        'id': id,
        'holdthedoor': 'Submit'
    }
    for i in range(1024):
        r = requests.post(URL, data=payload)

hodor_1024("110")
