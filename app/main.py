from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import os
import uvicorn


class Notice(BaseModel):
    name: str
    text: str


app = FastAPI()


@app.get("/file/{name:str}")
def fetch_file(name: str) -> str:
    with open("text/" + name + ".txt", "r") as file:
        contents = file.read()
        return contents


@app.post("/file")
def create_file(notice: Notice) -> Notice:
    if not os.path.exists("text"):
        os.mkdir("text")
    f = open("text/" + notice.name + ".txt", "x")
    f.write(notice.text)
    return notice


@app.put("/file")
def replace_file(notice: Notice) -> Notice:
    if not os.path.exists("text"):
        os.mkdir("text")
    with open("text/" + notice.name + ".txt", "w") as file:
        file.write(notice.text)
        return notice


if __name__ == "__main__":
    uvicorn.run("main.app", port=8000, reload=True)
