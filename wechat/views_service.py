from flask import Blueprint, request, make_response
import hashlib
from xml.etree import ElementTree as ET
import time

service_blueprint = Blueprint('service', __name__)


@service_blueprint.route('/wx', methods=['GET', 'POST'])
def handle():
    if request.method == 'GET':
        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')
        token = 'mrping'

        if not all([signature, timestamp, nonce, echostr]):
            print("Not get all information")

        verify_list = [token, timestamp, nonce]
        list.sort()
        verify_str = ''.join(verify_list).encode()
        hashcode = hashlib.sha1(verify_str).hexdigest()
        print("handle/GET func: hashcode, signature: ", hashcode, signature)

        if hashcode == signature:
            return echostr
        else:
            return ""

    else:
        rec = request.stream.read()
        xml_rec = ET.fromstring(rec)
        to_user = xml_rec.find('ToUserName').text
        from_user = xml_rec.find('FromUserName').text
        content = xml_rec.find('Content').text
        xml_rep = '''<xml>
                     <ToUserName><![CDATA[%s]]></ToUserName>
                     <FromUserName><![CDATA[%s]]></FromUserName>
                     <CreateTime>%s</CreateTime>
                     <MsgType><![CDATA[text]]></MsgType>
                     <Content><![CDATA[%s]]></Content>
                     <FuncFlag>0</FuncFlag>
                     </xml>'''

        if content == "笑话":
            response = make_response(xml_rep % (from_user, to_user, str(int(time.time())), "哈哈"))
            response.content_type = 'application/xml'
            return response
