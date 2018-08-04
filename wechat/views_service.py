from flask import Blueprint, request
from functions.token_verify import token_verify
from functions.message_handle import get_request, response_text, response_img
from functions.turing_rebot import rebot


service_blueprint = Blueprint('service', __name__)


@service_blueprint.route('/wx', methods=['GET', 'POST'])
def handle():
    if request.method == 'GET':
        token_verify("mrping")
    else:
        data = get_request()
        msg_type = data.get('msg_type')
        if msg_type == 'text':
            msg = rebot(data['content'])
            response = response_text(data['to_user'], data['from_user'], msg)
            return response
        elif msg_type == 'image':
            response = response_img(data['to_user'], data['from_user'], data['media_id'])
            return response
