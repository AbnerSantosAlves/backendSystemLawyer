from fastapi import FastAPI

from database.session import Base, engine
from routers.webhook_router import router as webhook_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.router('/')
def home():
    return "Estou ativo"
app.include_router(webhook_router)