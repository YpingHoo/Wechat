from flask import Blueprint, request
import hashlib

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

        list = [token, timestamp, nonce]
        list.sort()

        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print("handle/GET func: hashcode, signature: ", hashcode, signature)

        if hashcode == signature:
            return echostr
        else:
            return ""
