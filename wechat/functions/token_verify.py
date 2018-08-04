from flask import request
import hashlib


def token_verify(token):
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')
    token = token

    if not all([signature, timestamp, nonce, echostr]):
        print("Not get all information")

    verify_list = [token, timestamp, nonce]
    verify_list.sort()
    verify_str = ''.join(verify_list).encode()
    hashcode = hashlib.sha1(verify_str).hexdigest()
    print("handle/GET func: hashcode, signature: ", hashcode, signature)

    if hashcode == signature:
        return echostr
    else:
        return ""
