from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes.feedback import feedbackRouter
from app.core.config import settings
from app.core.db import Base, engine

app = FastAPI()
app.include_router(feedbackRouter, prefix="/api/feedback", tags=["feedback"])

Base.metadata.create_all(bind=engine)

@feedbackRouter.get("/")
async def root():
    return {"message": "Hello World"}

@feedbackRouter.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
