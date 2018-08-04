import requests
import json


def rebot(msg):
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    req_json = {"reqType": 0,
                "perception": {
                    "inputText": {"text": msg},
                    "inputImage": {"url": "imageUrl"},
                    "selfInfo": {"location": {
                        "city": "北京",
                        "province": "北京",
                        "street": "信息路"}}
                },
                "userInfo": {
                    "apiKey": "5efe0411b6504cfab550e7acacee2a41",
                    "userId": "303633"}
                }

    headers = {'content-type': 'application/json'}

    reponse = requests.post(url=url, data=json.dumps(req_json), headers=headers)

    receive_data = json.loads(reponse.text)
    print(receive_data['results'][0]['values'])
