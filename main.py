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
async def create_upload_file(file: UploadFile = File(...)):
    img_file = file.file
    #img = cv2.imread(img_file)
    print('recv:', type(img_file))

    return {
		"status": 'success'
	}