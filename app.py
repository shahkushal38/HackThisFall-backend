from flask import Flask, Response, request
from flask_restful import Resource, Api
from dotenv import load_dotenv, find_dotenv
import os
import pprint
import json
from pymongo import MongoClient
load_dotenv(find_dotenv())
from flask_cors import CORS 
from models.test import *


app = Flask(__name__)
api=Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})

database = os.environ.get("database")
client = MongoClient(database)
try:
    if(client):
        print("Connection Established")
    else:
        raise Exception("Database Connection Error")
except Exception as err:
    print(err)


db=client.Hackathon


@app.route('/test', methods=['GET', 'POST'])
def route():
    try:
        res = function1(request)
        return res
    except Exception as ex:
        print("Exception --- ", ex)

if __name__ == '__main__':
    app.run(debug=True)
