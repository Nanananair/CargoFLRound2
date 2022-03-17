from flask import Flask, render_template
from api import shipments
from dotenv import load_dotenv


load_dotenv()

UPLOAD_FOLDER = './uploads'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

