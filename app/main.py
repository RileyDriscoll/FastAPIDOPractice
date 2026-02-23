from fastapi import FastAPI, HTTPException, status
from contextlib import asynccontextmanager
from pydantic import BaseModel
import os
import shutil
import uvicorn


class Notice(BaseModel):
    name: str
    text: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not os.path.exists("text"):
        os.mkdir("text")
    yield
    if os.path.isdir("text"):
        shutil.rmtree("text")


app = FastAPI(lifespan=lifespan)


@app.get("/file/{name:str}")
def fetch_file(name: str) -> str:
    with open("text/" + name + ".txt", "r") as file:
        contents = file.read()
        return contents


@app.post("/file")
def create_file(notice: Notice) -> Notice:
    f = open("text/" + notice.name + ".txt", "x")
    f.write(notice.text)
    return notice


@app.put("/file")
def replace_file(notice: Notice) -> Notice:
    with open("text/" + notice.name + ".txt", "w") as file:
        file.write(notice.text)
        return notice


if __name__ == "__main__":
    uvicorn.run("main.app", port=8000, reload=True)
