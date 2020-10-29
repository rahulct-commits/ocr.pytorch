# ----------------------------------------
# create fastapi app 
# ----------------------------------------
from fastapi import FastAPI, File ,UploadFile
app = FastAPI()


# ----------------------------------------
# setup templates folder
# ----------------------------------------
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")


# ----------------------------------------
# setup static files folder
# ----------------------------------------
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")
# can use images as it is eg. <img src='static-img.jpg'>


# ----------------------------------------
# define structure for requests (Pydantic & more)
# ----------------------------------------
from fastapi import Request # for get
from pydantic import BaseModel # for post

class SomeRequest(BaseModel):
	status: str




# ----------------------------------------
# custom
# ----------------------------------------
import numpy as np
import cv2
import os
from ocr import ocr
import time
import shutil
from PIL import Image
from glob import glob
import cv2
import matplotlib.pyplot as plt

def single_pic_proc(rgbimg):
    """ input is numpy arr """
    result, image_framed = ocr(rgbimg)
    return result, image_framed

def get_rgb_from_spooled_tempfile(spooled_tempfile):
    byte_img = spooled_tempfile.read() # type `byte` 
    bgrimg = cv2.imdecode(np.frombuffer(byte_img, np.uint8), 1) # 1 - BGR
    return cv2.cvtColor(bgrimg, cv2.COLOR_BGR2RGB)

def plot_on_img(img, res):
    for _, v in res.items():
        # (0,1) + ---------------+ (2,3)
        #       |      text      |
        # (4,5) + ---------------+ (6,7)
        # 8 - acc score


# ==============================================================================================
# Application Interface
# ==============================================================================================
@app.get("/")
def api_home(request: Request):
	"""
	home page to display all real time values
	"""
	
	context = {
		"request": request
	}
	return templates.TemplateResponse("home.html", context)


@app.post("/uploadfile/")
def create_upload_file(file: UploadFile = File(...)):
    if file.filename.endswith('jpg') or file.filename.endswith('jpeg') or file.filename.endswith('png'):
        img = get_rgb_from_spooled_tempfile(file.file)
        res, imframed = single_pic_proc(img)
        return {"status": 'success'}
    else:
        print('image format exception')
        return {"status": 'image format exception'}
