from sqlalchemy_utils import EmailType
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, func
from sqlalchemy.orm import relationship
from db.base import Base

class Produtos(Base):
    __tablename__ = "tb_productos"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    item = Column('item', String, nullable=False)
    peso = Column('peso', Float)
    numero_caixas = Column('numero_caixas', Integer)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())
    sector_id = Column('sector_id', Integer, ForeignKey('tb_sectors.id'), nullable=False)

class User(Base):
    __tablename__ = 'tb_users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
    user_email = Column('user_emial', EmailType, nullable= False, unique= True)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())

class Sectors(Base):
    __tablename__ = 'tb_sectors'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    sector_name = Column('sector_name', String, nullable=False)                         
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())