from flask import render_template,request
from flask import redirect, url_for
import os
from PIL import Image
from app.utils import pipeline_extract_face

UPLOAD_FOLDER='static/uploads/'

def getwidth(path):
    img=Image.open(path)
    size=img.size
    aspect = size[0]/size[1]
    w = 350*aspect
    return int(w)


def base():
    if request.method == 'POST':
        f=request.files['image']
        filename=f.filename
        path=os.path.join(UPLOAD_FOLDER,filename)
        f.save(path)
        w=getwidth(path)
        pipeline_extract_face(path,filename)
        return render_template('base.html',fileupload=True,fname= filename,w=w)
    return render_template("base.html",fileupload=False,fname= 'facedetect.png',w="350")