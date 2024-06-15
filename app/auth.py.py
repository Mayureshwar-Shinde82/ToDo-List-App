from flask import request, _request_ctx_stack
from jose import jwt
from functools import wraps
import requests

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return {'message': 'Token is missing!'}, 403

        try:
            token = token.split()[1]
            response = requests.get(current_app.config['KEYCLOAK_SERVER_URL'] + 'realms/' + current_app.config['KEYCLOAK_REALM'] + '/protocol/openid-connect/userinfo', headers={'Authorization': 'Bearer ' + token})
            if response.status_code != 200:
                return {'message': 'Token is invalid!'}, 403
            user_info = response.json()
            _request_ctx_stack.top.user_info = user_info
            _request_ctx_stack.top.user_id = user_info['sub']
        except Exception as e:
            return {'message': 'Token is invalid!'}, 403

        return f(*args, **kwargs)
    return decorated
