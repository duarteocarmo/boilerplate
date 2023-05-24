import pkg_resources
from boilerplate.common.main import hello_world
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="Boilerplate API",
    version=pkg_resources.get_distribution("boilerplate").version,
)


@app.get("/")
async def root():
    return RedirectResponse("/docs")


@app.post(
    "/hello",
)
async def hello():
    return hello_world()
