from fastapi import FastAPI
import random
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Welcome to the API"}


@app.get("/random")
def random_number():
    return random.randint(0, 20)


if __name__ == "__main__":
    uvicorn.run("main.app", port=8000, reload=True)
