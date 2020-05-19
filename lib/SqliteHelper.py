import sqlite3


class SqliteHelper:
    db_name = "OPT3_API.db"

    def __init__(self):
        with sqlite3.connect(self.db_name) as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS users (id integer primary key autoincrement, username varchar not null, password varchar not null)")
            db.commit()

    def verify_user(self, username, password):
        with sqlite3.connect(self.db_name) as db:
            user_exists = db.execute("SELECT username FROM users WHERE username=?", (username,)).fetchall()
            print(user_exists)
            if len(user_exists) > 0:
                does_pw_match = db.execute("SELECT username FROM users WHERE username=? AND password=?",
                                           (username, password)).fetchall()
                if len(does_pw_match) > 0:
                    return True
        return False
