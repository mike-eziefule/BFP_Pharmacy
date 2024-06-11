"""Routes related to User web pages and info."""

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter(tags=["info"])

templates = Jinja2Templates(directory="templates")

#Home page route
@router.get("/", response_class = HTMLResponse)
async def index(
    request:Request,
):
    return templates.TemplateResponse("index.html", {"request": request})

#Contact page route
@router.get("/contact", response_class = HTMLResponse)
async def contact(
    request:Request,
):
    return templates.TemplateResponse("contact.html", {"request": request})

#Contact page route
@router.get("/shop", response_class = HTMLResponse)
async def shop(
    request:Request,
):
    return templates.TemplateResponse("shop.html", {"request": request})
