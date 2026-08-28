from fastapi import FastAPI

import database_models
from database import engine
from routes.centers import router as centers_router
from routes.distributions import router as distributions_router
from routes.foods import router as foods_router


app = FastAPI()
app.include_router(foods_router)
app.include_router(centers_router)
app.include_router(distributions_router)


@app.get("/")
def greet():
    return "welcome to app"
