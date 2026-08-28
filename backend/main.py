from fastapi import FastAPI

import database_models
from database import engine
from routes.foods import router as foods_router


app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)
app.include_router(foods_router)


@app.get("/")
def greet():
    return "welcome to app"
