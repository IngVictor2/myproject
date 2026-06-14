from contextlib import contextmanager, asynccontextmanager
from fastapi import FastAPI
from config.database import Base, engine
from controller.auth_controller import router as auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    yield

app = FastAPI(
    title= "Myproject",
    version="0.1",
    lifespan=lifespan,
)

@app.get("/")                                            
async def bienvenida():
    return {"mensaje": "MyProject"}

app.include_router(auth_router)