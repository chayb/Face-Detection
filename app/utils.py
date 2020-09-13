from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
import cv2
from glob import glob
import numpy as np

haar = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')

def pipeline_extract_face(path,filename):
    img = cv2.imread(path)
    img=np.array(img)
    if img.shape[1]>1000:
        r = 1000.0 / img.shape[1]
        dim = (1000, int(img.shape[0] * r))
        img = cv2.resize(img,dim,cv2.INTER_AREA)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = haar.detectMultiScale(gray,1.1,3)
    print(faces)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imwrite('./static/detect/{}'.format(filename),img)