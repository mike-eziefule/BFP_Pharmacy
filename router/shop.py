"""Routes related to online store and info."""

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter(prefix="/shop", tags=["shop"])
templates = Jinja2Templates(directory="templates")


#shoppers welcome page route
@router.get("/", response_class = HTMLResponse)
async def store(
    request:Request,
):
    return templates.TemplateResponse("shop.html", {"request": request})
