from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from tortoise.contrib.fastapi import register_tortoise

from dao.models import TodoData666

app = FastAPI()
template = Jinja2Templates("pages")

# 实现数据库的绑定
register_tortoise(app,  # 用户名root，密码root123123，本地地址端口@localhost:3306/，数据库名称fastapi01
                  db_url="mysql://root:root123123@localhost:3306/fastapi01",
                  modules={"models": ["dao.models"]},
                  generate_schemas=True,
                  add_exception_handlers=True
                  )

todos = ["写日记", "看电影", "玩游戏"]


@app.get("/")
async def index(req: Request):
    # 从数据库获取 todos 的代码
    # ORM，获取所有的todos
    todos = await TodoData666.all()
    print("todos=", todos)
    return template.TemplateResponse("index07.html", context={"request": req, "todos": todos})


@app.post("/todo")
def todo(todo=Form(None)):
    """处理用户发送过来的 todolist 数据"""
    todos.insert(0, todo)
    # 把新事项存储到数据库中
    return RedirectResponse("/", status_code=302)
