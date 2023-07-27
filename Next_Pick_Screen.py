#python -m venv veclnv
#venv\Scripts\activate
#print(3+4)

import requests
import json

baseURL = "https://www.voodoodevices.com/" # or your Big Block server
apiURL = baseURL+"api/"
deviceEndpoint = apiURL+"device/"
deviceID = "DD8F5D:B775CB"
username = "girish.b@cartesiankinetics.com"
password = "Spirit1.heart"

session = requests.Session()

x = session.post(
    apiURL+"user/login/",
    json={
        'username': username,
        'password':password
    }
)

z = json.loads(x.text)

sessiondata = session.post(
    deviceEndpoint+deviceID+"/",
    headers = {
        'referer': baseURL,
        'x-csrf-token': z['token'],
    },
    json={
        'command':'flash',

        'line1':'Next Item',
        'line2':'Go To',
        'line3': '\\bcBarcode Number',
        'line4':'Gate #1',
        'line5':'\\icright',

   #     'command': 'flash',
       # 'line1': 'Hello',
        #'line2': 'There',
        #'line3': '\\ictop',
        #'line4': '\\bcmyspecialcode',
          'color':'gr',   #g-green,gr-Yellow,gb-Cyan,r-red,rb-Voilet,b-Blue
        'seconds': '30',
        'nonce': 'nonce'
    }
)

# Decode the byte string to a regular string
body_str = sessiondata.request.body.decode('utf-8')

# Create a JSON object from the string
body_json = json.loads(body_str)

# Convert the request to a string
request_string = f"{sessiondata.request.method} {sessiondata.request.url} HTTP/1.1\r\n"

for header in sessiondata.request.headers:
    request_string += f"{header}: {sessiondata.request.headers[header]}\r\n"

request_string += f"\r\n{json.dumps(body_json)}"

print(request_string)

#https://www.voodoodevices.com/api/device/E95B0E:D0C82F/