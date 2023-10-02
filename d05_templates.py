from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
template = Jinja2Templates("pages")


@app.get("/")
def user(username, req: Request):
    return template.TemplateResponse("index05.html", context={"request": req, "name": username})
