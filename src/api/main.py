from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from boilerplate.main import hello_world

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse("/docs")


@app.post(
    "/hello",
)
async def hello():
    return hello_world()
