from fastapi import FastAPI, Header, Body, Form
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse

app = FastAPI()


@app.get("/user")
def user():
    return JSONResponse(content={"msg": "user"},
                        status_code=202,
                        headers={"a": "b"})


@app.get("/")
def user():
    html_content = """
    <html>
        <body><p style="color:red">Hello Word</p></body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/avatar")
def user():
    avatar = 'static/mage.jpg'
    # return FileResponse(avatar, filename="mage.jpg") #下载图片文件
    return FileResponse(avatar)  # 网页直接打开
