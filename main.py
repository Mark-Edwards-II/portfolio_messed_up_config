# Import the FastAPI class from the fastapi and neccessary imports.
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
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

@app.get("/this_will_json_response", response_class=JSONResponse)
async def return_json(request: Request):
    return {"data":25342452}

def get_content():
    return [1,2,3,4,5]

@app.get("/route_name_html_response", response_class=HTMLResponse)
async def return_json(request: Request):
    this_string="this is the title"
    """
    this is a route that returns
    """
    html_content = f"""
        <html>
            <head>
                <title>{this_string}</title>
            </head>
            <body>
                <h1  style="background-color: blue;" >{this_string}</h1>
            </body>
        </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


