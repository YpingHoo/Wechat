from flask import request, make_response
from xml.etree import ElementTree as ET
import time


def get_request():
    rec = request.stream.read()
    xml_rec = ET.fromstring(rec)
    to_user = xml_rec.find('ToUserName').text
    from_user = xml_rec.find('FromUserName').text
    msg_type = xml_rec.find('MsgType').text

    data = dict()
    data['to_user'] = to_user
    data['from_user'] = from_user
    data['msg_type'] = msg_type

    if msg_type == 'text':
        content = xml_rec.find('Content').text
        data['content'] = content
    elif msg_type == 'image':
        pic_url = xml_rec.find('PicUrl').text
        media_id = xml_rec.find('MediaId').text
        data['pic_url'] = pic_url
        data['media_id'] = media_id
    print(msg_type)
    return data


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


def response_img(to_user='',from_user='',media_id=''):
    xml_rep = '''<xml>
                     <ToUserName><![CDATA[%s]]></ToUserName>
                     <FromUserName><![CDATA[%s]]></FromUserName>
                     <CreateTime>%s</CreateTime>
                     <MsgType><![CDATA[image]]></MsgType>
                     <Image>
                     <MediaId><![CDATA[%s]]></MediaId>
                     </Image>
                 </xml>'''

    response = make_response(xml_rep % (from_user, to_user, str(int(time.time())), media_id))
    response.content = 'application/xml'
    return response
