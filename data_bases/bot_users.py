import sqlite3


class BibleData:
    def __init__(self, db_name='userbot.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_bible (
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id  INTEGER,
                first_name TEXT,
                user_name TEXT
            )
        ''')
        self.connection.commit()

    def insert_user(self, user_id, first_name, user_name):
        self.cursor.execute("SELECT user_id FROM user_bible WHERE user_id=?", (user_id,))
        existing_user = self.cursor.fetchone()

        if existing_user is None:
            self.cursor.execute('''
                INSERT INTO user_bible(user_id, first_name, user_name)
                VALUES (?, ?, ?)
                ''', (user_id, first_name, user_name))
            self.connection.commit()

    def get_users(self):
        ...

    def closed(self):
        self.connection.close()
