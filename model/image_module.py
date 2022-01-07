from flask import Flask, request, session
import json
from collections import OrderedDict
import os



def save_image(image):
    url=[]
    for f in image:
        filename = len(os.listdir('./image/'))+1
        f.save('./image/'+str(filename)+'.jpg')
        url.append(filename)

    return url

#[1,2,3,4] -> "1,2,3,4"
def url_to_db(image_url):
    if len(image_url)==1:
        return str(image_url[0])
    return ','.join(image_url)
# "1,2,3,4"->[1,2,3,4]
def db_ro_url(db_url):
    return db_url.split(',')
