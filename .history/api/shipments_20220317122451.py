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
import pandas as pd

ALLOWED_EXTENSIONS = set(['xls', 'xlsx', 'xlsm', 'xlsb', 'odf', 'ods', 'odt'])

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
            if df.empty: 
                resp = jsonify({'message' : 'The file cannot be empty!'})
                resp.status_code = 400
                return resp
            else:
                for row in df.itertuples():
                    #TODO: Reappearing data? 
                    shipment_item = Shipment(docket= row.docket, lsp_lr= row.lsp_lr, invoice= row.invoice, pickup_date=row.pickup_date, edd= row.edd, actual_delivery_date=row.actual_delivery_date, consigner=row.consigner, consignee=row.consignee, from_city=row.from_city, to_city=row.to_city)
                    session.add(shipment_item)
                    session.commit()
                    session.refresh(shipment_item)
                return Response(status=201, response= "Shipment Items created succesfully")
        else: 
            resp = jsonify({'message' : 'Allowed file types are xls, xlsx, xlsm, xlsb, odf, ods, odt'})
            resp.status_code = 400
            return resp

    except Exception as e:
        return Response(status= 400, response=  "An error occured "+str(e))
    session_helper.close_session()