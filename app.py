import itertools
import psycopg2

from flask import Flask
from flask_restx import Resource, Api

from config import DB_CONFIG


app = Flask(__name__)
api = Api(app)

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


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
