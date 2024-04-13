from importlib.metadata import version

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from {{cookiecutter.project_slug}}.common.main import hello_world

app = FastAPI(
    title="{{cookiecutter.project_slug}} API",
    version=version("{{cookiecutter.project_slug}}"),
)


@app.get("/")
async def root():
    return RedirectResponse("/docs")


@app.post(
    "/hello",
)
async def hello():
    return hello_world()
