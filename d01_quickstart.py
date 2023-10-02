import uvicorn
from fastapi import FastAPI

app = FastAPI()


# @app是python的装饰器，当在浏览器地址栏中输入"/"这个URL地址时，那么app = FastAPI()程序就会调用下面的这个函数 def index()
# 调用完成就返回字符串 "This is Home Page" 给浏览器，渲染在前端页面

@app.get("/")  # 输入URL地址
def index():
    """这是首页"""
    return "This is Home Page"  # 得到响应信息，是返回普通字符串


@app.get("/users")  # 输入URL地址
def users():
    """获取所有的用户"""
    return {"msg": "Get all users", "code": 2002}  # 得到响应信息，是返回字典，浏览器得到JSON格式数据


@app.get("/projects")  # 输入URL地址
def projects():
    return ["项目1", "项目2", "项目3"]  # 得到响应信息，是返回列表，浏览器得到列表格式数据


# if __name__=='__main__'  #直接键入 main  就全跳出来了

if __name__ == '__main__':
    uvicorn.run(app)
