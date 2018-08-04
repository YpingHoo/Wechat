import requests
import json
from config import Config


def get_access_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token?' \
          'grant_type=client_credential&appid=%s&secret=%s' % (Config.WECHAT_APPID, Config.WECHAT_APPSECRET)

    response = requests.get(url)
    receive_data = json.loads(response.text)
    return receive_data['access_token']