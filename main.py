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

class SomekRequest(BaseModel):
	status: str




# ----------------------------------------
# define structure for requests (Pydantic & more)
# ----------------------------------------
import numpy as np
import cv2





# ==============================================================================================
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
    byte_img = file.file.read()
    print('name:', file.filename)
    print('recv:', type(byte_img))
    decoded = cv2.imdecode(np.frombuffer(byte_img, np.uint8), -1)
    print('decoded:', decoded.shape, type(decoded))
    

    return {
		"status": 'success'
	}