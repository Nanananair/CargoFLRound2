from os import stat
import os
from tkinter import E
from urllib import response
from itsdangerous import json
from sqlalchemy.sql.expression import null
from db.db import SessionHelper
from flask import Response
from flask import request, jsonify
from db.models import Shipment
from werkzeug.utils import secure_filename
import main
import pandas as pd

ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upsert_excel(): 
    try : 
        session_helper = SessionHelper()
        session = session_helper.get_session()

        file = request.files['file']

        if file.filename  == '': 
            resp = jsonify({'message' : 'No file part in the request'})
            resp.status_code = 400
            return resp
        if file and allowed_file (file.filename):
            df = pd.read_excel(file)
            