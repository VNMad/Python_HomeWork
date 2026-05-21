#____________________________________________________________________
#1. Создание базы
#____________________________________________________________________
import os
import pymysql
from dotenv import load_dotenv


load_dotenv('.env')


config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
}


class NotesAppDatabase:
    CREATE_DATABASE_QUERY = """
        CREATE DATABASE IF NOT EXISTS notes_app_121225_ptm_vnmad
    """

    USE_DATABASE_QUERY = """
        USE notes_app_121225_ptm_vnmad
    """

    def __init__(self, cur):
        self.cur = cur

    def create_database(self):
        self.cur.execute(self.CREATE_DATABASE_QUERY)

    def use_database(self):
        self.cur.execute(self.USE_DATABASE_QUERY)


def main():
    try:
        with pymysql.connect(**config) as connection:
            with connection.cursor() as cursor:
                notes_database = NotesAppDatabase(cursor)
                notes_database.create_database()
                notes_database.use_database()
                print("Database 'notes_app_121225_ptm_vnmad' created or already exists.")
    except pymysql.MySQLError as e:
        print(f'Database error: {e}')


if __name__ == '__main__':
    main()

#____________________________________________________________________
#2. Создание базы
#____________________________________________________________________
import os

import pymysql
from dotenv import load_dotenv
from pymysql.cursors import DictCursor


load_dotenv('.env')


config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
}


class NotesAppDatabase:
    CREATE_DATABASE_QUERY = """
        CREATE DATABASE IF NOT EXISTS notes_app_121225_ptm_vnmad
    """

    USE_DATABASE_QUERY = """
        USE notes_app_121225_ptm_vnmad
    """

    CREATE_NOTES_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS notes (id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL, content TEXT NOT NULL)
    """

    INSERT_NOTE_QUERY = """
        INSERT INTO notes (title, content) VALUES (%s, %s)
    """

    SELECT_NOTES_QUERY = """
        SELECT id, title, content FROM notes
    """

    def __init__(self, cur):
        self.cur = cur

    def create_database(self):
        self.cur.execute(self.CREATE_DATABASE_QUERY)

    def use_database(self):
        self.cur.execute(self.USE_DATABASE_QUERY)

    def create_notes_table(self):
        self.cur.execute(self.CREATE_NOTES_TABLE_QUERY)

    def add_note(self, title, content):
        self.cur.execute(self.INSERT_NOTE_QUERY, (title, content))

    def get_notes(self):
        self.cur.execute(self.SELECT_NOTES_QUERY)
        return self.cur.fetchall()


def main():
    try:
        with pymysql.connect(**config, cursorclass=DictCursor) as connection:
            with connection.cursor() as cursor:
                notes_database = NotesAppDatabase(cursor)
                notes_database.create_database()
                notes_database.use_database()
                notes_database.create_notes_table()
                title = 'Shopping list'
                content = 'Milk, Bread, Eggs'
                notes_database.add_note(title, content)
                connection.commit()
                notes = notes_database.get_notes()
                for note in notes:
                    print(f"Note added: {note['title']}")

    except pymysql.MySQLError as e:
        print(f'Database error: {e}')


if __name__ == '__main__':
    main()