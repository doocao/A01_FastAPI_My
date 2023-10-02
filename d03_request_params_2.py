from fastapi import FastAPI, Header, Body

app = FastAPI()


@app.get("/user")
def user(id, token=Header(None)):  # Python的默认参数机制，token是关键字，把它赋值成一个叫Header()的对象
    return {"id": id, "token": token}


"""
@app.get("/user") 
上面这种用法呢是使用了我们Python当中一种非常灵活的机制叫做【默认参数】。
def user(id, token=Header(None)):这里是一个关键字 token 我们把它赋值成一个叫做Header()的对象
然后当我们在浏览器（或者postman）的URL中，当我们在请求(GET)当中，即在头部信息Header()里面传递了这个token值
那么呢我们就可以在这个函数当中找到同名的字段token，如果在我们这里啊传递的不是一个叫做token而是叫做tok
那么呢这个数据它就接收不到，我们接受的token呢就拿不到这个数据了，
所以一定要保持你传递的字段的名称和我们这个函数当中的这个关键字的名称是一样的。
"""


@app.post("/login")
def login(data=Body(None)):
    return {"data": data}
