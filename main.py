from fastapi import FastAPI
from config.database import Session, engine, Base
from middlewares.error_handler import Errorhandler
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.title = "App with fastAPI and react"

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)
Base.metadata.create_all(bind=engine)


@app.get('/', tags=['home'])
def message(): 
    return "Hello World"
