from flask import Flask, jsonify, request
import base64
import json

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
            return jsonify({"status": "success", "result": "true"})

    return jsonify({"status": "success", "result": "false"})


@app.route("/customer/customer_ids/<customer_id>", methods=["get"])
def get_customer_ids(customer_id):
    if is_authenticated():
        get_customer_ass_ids = sqliteHelper.get_customer_associated_ids(customer_id)
        return jsonify({"status": "success", "result": get_customer_ass_ids})
    return jsonify({"status": "error"})


@app.route("/customer/address/<address_id>")
def get_address(address_id):
    if is_authenticated():
        test = sqliteHelper.get_address_by_id(address_id)
        return jsonify({"status": "success", "result": test})
    return jsonify({"status": "error"})


@app.route("/customer/company/<company_id>")
def get_company(company_id):
    if is_authenticated():
        get_company = sqliteHelper.get_company_by_id(company_id)
        return jsonify({"status": "success", "result": get_company})

    return jsonify({"status": "error"})


@app.route("/customer/consumer/<customer_id>")
def get_consumer(customer_id):
    if is_authenticated():
        get_company = sqliteHelper.get_consumer_by_id(customer_id)
        return jsonify({"status": "success", "result": get_company})

    return jsonify({"status": "error"})


@app.route("/customer/company/get_all", methods=["get"])
def get_all_companies():
    if is_authenticated():
        get_companies = sqliteHelper.get_all_companies()
        print(get_companies[0])
        return jsonify({"status": "success", "result": get_companies})


@app.route("/customer/consumer/get_all", methods=["get"])
def get_all_consumers():
    if is_authenticated():
        get_consumers = sqliteHelper.get_all_consumers()
        print(get_consumers)
        return jsonify({"status": "success", "result": get_consumers})


@app.route("/customer/consumer/edit", methods=["POST"])
def edit_consumer():
    if is_authenticated():
        json_body = request.json
        print(json_body)
        sqliteHelper.update_consumer(json_body)
        return jsonify({"status": "success"})


@app.route("/customer/address/edit", methods=["POST"])
def edit_address():
    if is_authenticated():
        json_body = request.json
        sqliteHelper.update_address(json_body)
        return jsonify(status="success")


def is_authenticated():
    api_key = open("api_key", "r").read()
    if request.headers["api_key"] == api_key:
        return True
    return False


if __name__ == '__main__':
    app.run()
