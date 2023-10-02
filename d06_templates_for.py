from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()
template = Jinja2Templates("pages")

todos = ["写日记", "看电影", "玩游戏"]


@app.get("/")
def index(req: Request):
    return template.TemplateResponse("index06.html", context={"request": req, "todos": todos})


@app.post("/todo")
def todo(todo=Form(None)):
    """处理用户发送过来的 todolist 数据"""
    todos.insert(0, todo)
    return RedirectResponse("/", status_code=302)
