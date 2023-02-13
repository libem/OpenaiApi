#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_jwt import JWT, jwt_required, current_identity

import chatgpt
import config


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id


# 防数据库用户信息
users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]
username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and user.password.encode('utf-8') == password.encode('utf-8'):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


########################################################
app = Flask(__name__)
app.debug = config.debugger_model
app.config['SECRET_KEY'] = config.SECRET_KEY

jwt = JWT(app, authenticate, identity)


@app.route('/protected')
@jwt_required()
def protected():
    print
    "this protected is successed!!!"
    # return '%s' % current_identity
    return jsonify(code=0, msg="success", data='%s' % current_identity)


@app.route('/ask', methods=['POST'])
@jwt_required()
def request_ask():
    data = request.get_json()
    if "q" in data:
        question = data["q"]
        try:
            answer = chatgpt.get_response(question)
            return jsonify(code=0, msg="success", data=answer)
        except Exception as e:
            return jsonify(code=500, msg="error", err=e.args)
    else:
        return jsonify(code=500, msg="error", err="Missing key parameter (q)!")


########################################################
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.server_port)