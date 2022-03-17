from flask import Flask, render_template
from api import shipments
from dotenv import load_dotenv


load_dotenv()

UPLOAD_FOLDER = './uploads'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#shipments
app.add_url_rule("/upsert_excel", view_func= shipments.upsert_excel, methods=["POST"] )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)