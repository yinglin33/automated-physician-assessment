import os
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
# from flask_cors import CORS, cross_origin
import logging

logging.basicConfig(level=logging.INFO)

UPLOAD_FOLDER = './file_uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def fileUpload():  # fails for some reason but file is still saved
    target=os.path.join(UPLOAD_FOLDER)
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    file.save(destination)
    session['uploadFilePath']=destination
    print(request.json)
    return ""



if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host="0.0.0.0",use_reloader=False)
