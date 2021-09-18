from flask import Flask
from flask import Response
from flask import request
import datetime
import hashlib


REF_HASH = b'\xe9\xa7T\x86sjU\n\xf4\xfe\xa8a\xe27\x83\x05\xc4\xa5U\xa0P\x94\xde\xe1\xdc\xa2\xf6\x8a\xfe\xa4\x9c\xc3\xa5\x0e\x8d\xe6\xea\x13\x1e\xa5!1\x1fMo\xb0T\xa1F\xe8(/\x8e5\xff.ch\xc1\xa6.\x90\x97\x16'
app = Flask(__name__)


def check_pass(password):
    try:
        h = hashlib.sha3_512(password.encode('ASCII'))
        if h.digest() == REF_HASH:
            return True
    except:
        pass
    return False


def handle_data(path, addr, args, auth):
    host = None
    user = auth.get('username', None)
    password = auth.get('password', None)

    log_str = f'{path} | {addr}'
    if 'host' in args:
        host = args['host']
        log_str = f'{log_str} | {host}'
    if user:
        log_str = f'{log_str} | {user}'
    print(log_str)

    if user == 'test_user' and password and check_pass(password) and host and host == 'test_host':
        save_ip(addr)


def save_ip(ip):
    lines = f'{ip}\n{datetime.datetime.now().isoformat()}'
    with open('addr', 'w') as f:
        f.write(lines)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def get_path(path):
    addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    handle_data(path, addr, request.args, request.authorization)
    return Response('ok')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50001)
