from fastapi import FastAPI
from routers import user, equipment, reservations, client
from auth import authentication
from db import models
from db.database import engine

app = FastAPI()
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(client.router)
app.include_router(reservations.router)
app.include_router(equipment.router)

@app.get('/')
def root():
    return 'Hello'



models.Base.metadata.create_all(engine)