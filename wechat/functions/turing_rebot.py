import requests
import json
from config import Config


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
                    "apiKey": Config.TURING_APIKEY,
                    "userId": Config.TURING_USERID}
                }

    headers = {'content-type': 'application/json'}

    reponse = requests.post(url=url, data=json.dumps(req_json), headers=headers)

    receive_data = json.loads(reponse.text)
    data = receive_data['results'][0]['values']['text']
    return data
