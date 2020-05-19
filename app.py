from flask import Flask, jsonify, request
import base64

from lib.SqliteHelper import SqliteHelper

app = Flask(__name__)

sqliteHelper = SqliteHelper()


@app.route("/")
def index():
    return "Hello world!"


@app.route("/login", methods=["post"])
def login():
    if is_authenticated():
        authentication_header = request.headers["Authentication"][6::]
        delimiter = authentication_header.find(":")
        username = base64.b64decode(authentication_header[:delimiter]).decode("utf-8")
        password = base64.b64decode(authentication_header[delimiter:]).decode("utf-8")

        print("Logging in with " + username + " pw: " + password)
        if sqliteHelper.verify_user(username, password):
            return jsonify({"result": "true"})

    return jsonify({"result": "false"})


def is_authenticated():
    api_key = open("api_key", "r").read()
    if request.headers["api_key"] == api_key:
        return True
    return False


if __name__ == '__main__':
    app.run()
