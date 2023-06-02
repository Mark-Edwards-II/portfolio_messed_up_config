# Import the FastAPI class from the fastapi and neccessary imports.
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Create an instance of the FastAPI class
app = FastAPI()

# mount the static file to app to be accessed when returning HTMLResponse.
app.mount("/static", StaticFiles(directory="static"), name="static")

# instantiate Jinja2Templates in order to return a template reponse.
templates = Jinja2Templates(directory="templates")

# Define a route for the home page using the HTTP GET method and declare the response type.
@app.get("/", response_class=HTMLResponse)
async def read_main(request: Request):

    return templates.TemplateResponse("home.html", {"request": request, "context":get_content()})

def get_content():
    return [1,2,3,4,5]