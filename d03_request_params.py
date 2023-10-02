from fastapi import FastAPI

app = FastAPI()


# @app.get("/user/{id}")  #在postman中地址栏输入http://127.0.0.1:8000/user/7
# def user(id):
#     return {"id": id}\

@app.get("/user")  # 在postman中地址栏输入http://127.0.0.1:8000/user?id=7
def user(id):
    return {"id": id}
