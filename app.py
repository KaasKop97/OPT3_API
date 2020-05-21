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

        if sqliteHelper.verify_user(username, password):
            return jsonify({"result": "true"})

    return jsonify({"result": "false"})


@app.route("/customer/customer_ids/<customer_id>", methods=["get"])
def get_customer_ids(customer_id):
    if is_authenticated():
        xd = sqliteHelper.get_customer_associated_ids(customer_id)
        print(xd)
    return jsonify({"status": "error"})


@app.route("/customer/address/<address_id>")
def get_address(address_id):
    if is_authenticated():
        test = sqliteHelper.get_address_by_id(address_id)
        return jsonify({"status": "success"}, test)
    return jsonify({"status": "error"})


@app.route("/customer/company/<company_id>")
def get_company(company_id):
    if is_authenticated():
        get_company = sqliteHelper.get_company_by_id(company_id)
        return jsonify({"status": "success"}, get_company)
    return jsonify({"status": "error"})

@app.route("/customer/consumer/<customer_id>")
def get_consumer(customer_id):
    if is_authenticated():
        get_company = sqliteHelper.get_consumer_by_id(customer_id)
        return jsonify({"status": "success"}, get_company)
    return jsonify({"status": "error"})

def is_authenticated():
    api_key = open("api_key", "r").read()
    if request.headers["api_key"] == api_key:
        return True
    return False


if __name__ == '__main__':
    app.run()
