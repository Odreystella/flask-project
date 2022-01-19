import itertools
import psycopg2

from my_settings import DB_CONFIG


param_dic = {
    "port":5432,
    "host": DB_CONFIG['HOST'],
    "user": DB_CONFIG['USERNAME'],
    "password": DB_CONFIG['PASSWORD'],
    "dbname": DB_CONFIG['DB_NAME'],
}

class Database():
    def __init__(self):
        self.db = psycopg2.connect(
            host=DB_CONFIG['HOST'], 
            port=5432, 
            user=DB_CONFIG['USERNAME'], 
            password=DB_CONFIG['PASSWORD'], 
            dbname=DB_CONFIG['DB_NAME'])
        self.cursor = self.db.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchall()

        return list(itertools.chain(*row))
