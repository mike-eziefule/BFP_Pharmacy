"""Main FastAPI App."""

from fastapi import FastAPI
from sql.database import engine
from router import auth, shop, user, info
from sql.model import Base
from config.config import get_settings
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
# from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Pharmacy API",
    description="A FastAPI-based pharmacy and cosmetic store.",
    version="0.1.0",
    openapi_tags= get_settings().tags
)

# HTML Dependencies
templates = Jinja2Templates(directory="templates")

# CSS/JS Dependencies
app.mount("/static", StaticFiles(directory="static"), name="static")

Base.metadata.create_all(bind=engine)

#CORS middleware restrictions
# origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = origins,
#     allow_credentials = True,
#     allow_methods = ["*"],
#     allow_headers = ["*"]
# )

# Include the router
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(shop.router)
app.include_router(info.router)