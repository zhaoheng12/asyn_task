# -*- coding: utf-8 -*-
from werkzeug.utils import secure_filename

from asyn_task import run_task
import flask
from flask import Flask, render_template, request

import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'

@app.route('/')
def upload_file():
   return render_template('upload.html')


@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
       file = request.files['file']
       try:
           file_data = file.file.read()
           print(file_data)
       except:
           file_data = file.file.getvalue()
       file.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
       def parse_data(task_id,file_data):
           import base64
           import xlrd
           file_data = base64.b64decode(file_data)

           run_task(parse_data, ['1223', file_data])
           print("-" * 30)
   return 'file uploaded successfully'















if __name__ == '__main__':
   app.run(debug=True)






