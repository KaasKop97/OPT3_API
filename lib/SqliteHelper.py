import sqlite3
from flask import jsonify


class SqliteHelper:
    db_name = "OPT3_API.db"

    def __init__(self):
        with sqlite3.connect(self.db_name) as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS users ("
                "id integer primary key autoincrement, "
                "username varchar not null, "
                "password varchar not null"
                ")")

            db.execute(
                "CREATE TABLE IF NOT EXISTS Customer ("
                "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                "name varchar not null, "
                "email_address varchar not null, "
                "telephone_number varchar not null, "
                "type varchar not null"
                ")")

            db.execute(
                "CREATE TABLE IF NOT EXISTS Address ("
                "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                "street varchar not null, "
                "street_number varchar not null, "
                "postal_code varchar not null, "
                "city varchar not null"
                ")")

            db.execute(
                "CREATE TABLE IF NOT EXISTS Consumer ("
                "ID integer primary key autoincrement,"
                "teamviewer_id integer,"
                "teamviewer_password varchar"
                ")")

            db.execute(
                "create table if not exists Company (ID integer primary key autoincrement, "
                "name varchar not null, "
                "kvk_number varchar not null, "
                "contact_person varchar not null"
                ")")
            db.execute(
                "create table if not exists Customer_Data ("
                "ID integer primary key autoincrement, "
                "customer_id integer, "
                "address_id integer, "
                "company_id integer, "
                "consumer_id integer,"
                "foreign key (customer_id) references Customer(ID),"
                "foreign key (address_id) references Address(ID),"
                "foreign key (company_id) references Company(ID),"
                "foreign key (consumer_id) references Consumer(ID)"
                ")")
            db.commit()

    def verify_user(self, username, password):
        with sqlite3.connect(self.db_name) as db:
            user_exists = db.execute("SELECT username FROM users WHERE username=?", (username,)).fetchall()
            print(user_exists)
            if len(user_exists) == 1:
                does_pw_match = db.execute("SELECT password FROM users WHERE username=? AND password=?",
                                           (username, password)).fetchall()
                print(does_pw_match)
                if len(does_pw_match) == 1:
                    return True
        return False

    def get_customer_associated_ids(self, customer_id):
        with sqlite3.connect(self.db_name) as db:
            get_customer_associated_tables = db.execute(
                "SELECT customer_id, address_id, company_id from Customer_Data where customer_id=?",
                customer_id).fetchall()
            return get_customer_associated_tables

    def get_address_by_id(self, address_id):
        with sqlite3.connect(self.db_name) as db:
            return db.execute("SELECT * FROM Address WHERE ID=?", address_id).fetchall()

    def get_company_by_id(self, company_id):
        with sqlite3.connect(self.db_name) as db:
            get_companies = db.execute("SELECT * FROM Company WHERE ID=?", company_id).fetchall()
            if len(get_companies) != 0:
                return get_companies
            else:
                return {"DB_ERROR": "Error no company associated with that ID"}

    def get_customer_by_id(self, customer_id):
        with sqlite3.connect(self.db_name) as db:
            return db.execute("SELECT * FROM Customer WHERE ID=?", customer_id).fetchall()

    def get_consumer_by_id(self, customer_id):
        with sqlite3.connect(self.db_name) as db:
            return db.execute("SELECT * FROM Consumer WHERE ID=?", customer_id).fetchall()
