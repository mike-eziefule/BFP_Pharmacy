from sql.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index= True)
    names = Column(String, nullable= False)
    lastname = Column(String, nullable= False)
    email = Column(String, nullable= False, unique= True)
    password = Column(String, nullable= False)
    recovery = Column(String, nullable= False)
    date_joined = Column(String, nullable= False)
    
    #relationship
    cart = relationship("Cart", back_populates = "owner")


class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index = True)
    code = Column(String, nullable= False, unique=True)
    title = Column(String, nullable=True, default="My Title")
    description = Column(String, nullable=True)
    price = Column(Float, nullable=True, default=0)
    available = Column(Boolean, default=True)
    
    #relationship
    cart2 = relationship("Cart", back_populates = "item")
    
    
class Cart(Base):
    __tablename__ = 'cart'
    
    id = Column(Integer, primary_key=True, index = True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=True, default=0)
    price = Column(Float, nullable=False, default= 0.00)
    amount = Column(Float, nullable= False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    #relationship
    owner = relationship("User", back_populates = "cart")
    item = relationship("Product", back_populates = "cart2")
