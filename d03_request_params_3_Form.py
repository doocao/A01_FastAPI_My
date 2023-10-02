from fastapi import FastAPI, Header, Body, Form

app = FastAPI()


@app.post("/login")
def login(username=Form(None), password=Form(None)):
    return {"data": {"username": username, "password": password}}
