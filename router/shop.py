"""Routes related to online store and info."""

from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sql import database, model
from sqlalchemy.orm import Session
from utils import service
from starlette.datastructures import URL
from config.config import get_settings

router = APIRouter(prefix="/shop", tags=["shop"])
templates = Jinja2Templates(directory="templates")


#shoppers welcome page route
@router.get("/", response_class = HTMLResponse)
async def store(
    request:Request,
):
    return templates.TemplateResponse("shop_index.html", {"request": request})

#products page route
@router.get("/products", response_class = HTMLResponse)
async def products(
    request:Request,
    db:Session=Depends(database.get_db)
):
    
    user = service.get_user_from_token(request, db)
    if not user:
        return RedirectResponse("/auth/login")
    
    """View URL."""
    catalogue = db.query(model.Cart).filter(model.Cart.owner_id == user.id).all()
        
    return templates.TemplateResponse(
        "shop_product.html",{
        "request": request,
        "cart": catalogue, 
        "user": user}
    )
