from flask import Blueprint, request
from functions.token_verify import token_verify
from functions.message_handle import get_request, response_text


service_blueprint = Blueprint('service', __name__)


@service_blueprint.route('/wx', methods=['GET', 'POST'])
def handle():
    if request.method == 'GET':
        token_verify("mrping")
    else:
        to_user, from_user, content = get_request()

        if content == "笑话":
            msg = "哈哈"
            response_text(to_user, from_user, msg)
