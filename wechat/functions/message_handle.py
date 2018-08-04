from flask import request, make_response
from xml.etree import ElementTree as ET
import time


def get_request():
    rec = request.stream.read()
    xml_rec = ET.fromstring(rec)
    to_user = xml_rec.find('ToUserName').text
    from_user = xml_rec.find('FromUserName').text
    content = xml_rec.find('Content').text
    msg_type = xml_rec.find('MsgType').text

    print(msg_type)
    return to_user, from_user, content


def response_text(to_user='', from_user='', msg=''):
    xml_rep = '''<xml>
                     <ToUserName><![CDATA[%s]]></ToUserName>
                     <FromUserName><![CDATA[%s]]></FromUserName>
                     <CreateTime>%s</CreateTime>
                     <MsgType><![CDATA[text]]></MsgType>
                     <Content><![CDATA[%s]]></Content>
                     <FuncFlag>0</FuncFlag>
                 </xml>'''

    response = make_response(xml_rep % (from_user, to_user, str(int(time.time())), msg))
    response.content_type = 'application/xml'
    return response


# def response_img(to_user='', from_user='', )
#     xml_rep = '''
#             '''
