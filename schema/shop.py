"""Setup the model schemas."""

from pydantic import BaseModel
from typing import List
from datetime import date
from schema import user



class ItemBase(BaseModel):
    """ Define URLBase class. """
    

    class Config:
        """Set config for this class."""
        orm_mode = True

# class URL(ItemBase):
#     """Define URL class."""
    

# class URLListItem(URLBase):
#     """A single URL item, with extra 'url' field."""
#     date_created: date
#     url: str
#     owner: user.ShowUser


# class URLList(BaseModel):
#     """List of URLs."""
#     urls: List[URLListItem]


# class URLInfo(URL):
#     """Define URLInfo class."""
#     url: str
#     private_key: str