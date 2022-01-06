from flask import Blueprint, request, session, send_file
from model import db_module
from model import sql_module
import json
from collections import OrderedDict
import os


bp = Blueprint('image_bp',__name__,url_prefix='/image')

@bp.route("/get_image", methods = ['GET'])
def get_image():
    if request.method == 'GET':
        url = request.args.get('image_url')
        #return str(int(url))
        path = "../image/"+str(url)+".jpg"
        #return path
        return send_file(path, attachment_filename = str(url)+".jpg",as_attachment=True)



@bp.route("/post_image",methods = ['POST'])
def post_image():
    if request.method == 'POST':
        file = request.files['file']
        file_num = len(os.listdir('./image/'))
        file.save("./image/"+str(file_num)+".jpg")
        return str(file_num)
