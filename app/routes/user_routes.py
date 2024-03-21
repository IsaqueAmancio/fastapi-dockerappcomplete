from typing import List
from fastapi import APIRouter, Response, Depends, status, Query, HTTPException
from sqlalchemy.orm import Session
from db.database import engine,SessionLocal
from db.models import User as UsersModel
from schemas.user import User as UsersOutput
from sqlalchemy.orm import Session

from db.base import Base

Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/users")   

def get_db():
    try:
        db = SessionLocal()
        #TODO 
        yield db
    finally:
        db.close()

@router.post("/addComSchema", status_code=status.HTTP_201_CREATED, description='Add user')
def add_user(request:UsersOutput, db: Session = Depends(get_db)):
        user_on_db = UsersModel(id=request.id, username=request.username, password=request.password, user_email=request.user_email)
        user_on_db = UsersModel(**request.dict())
        db.add(user_on_db)
        db.commit()
        return Response(status_code=status.HTTP_201_CREATED)

'''@router.get("/{user_usernames}", description="List users by username")
def get_produtos(user_usernames,db: Session = Depends(get_db)):
    user_on_db= db.query(UsersModel).filter(UsersModel.item == user_usernames).first()
    return user_on_db


@router.get("/users/list")
async def get_users(db: Session = Depends(get_db)):
    users= db.query(UsersModel).all()
    return users

#validação no código
@router.delete("/{id}", description="Delete an user by ID")
def delete_user(id: int, db: Session = Depends(get_db)):

    user_on_db = db.query(UsersModel).filter(UsersModel.id == id).first()
    if user_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There\'s no users with the given ID')
    db.delete(user_on_db)
    db.commit()
    return f"The user with the ID: {id}, was deleted.", Response(status_code=status.HTTP_200_OK)

@router.put('/update/{id}', description='Update user data')
def update_user(
    id: int,
    user: UsersOutput,
    db: Session = Depends(get_db)
    
    ):
    user_on_db = db.query(UsersModel).filter_by(id=id).first()
    if user_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No user was found with the given ID')
        
    user_on_db.username = user.username
    user_on_db.password = user.password
    user_on_db.user_email = user.user_email
    
    db.add(user_on_db)
    db.commit()
    return "ok"

# @router.put("/{id}", )
# async def update_todo(id: int, produtos = Produtos, body: dict) -> dict:
#     produtos_on_db = db.query(Produtos).filter(Produtos.id == id).first()
#     for todo in produtos:
#         if int(todo["id"]) == id:
#             todo["item"] = body["item"]
#             return {
#                 "data": f"Todo with id {id} has been updated."
#             }

#     return {
#         "data": f"Todo with id {id} not found."
#     }

# @app.put("/produto/{id}",response_model=Produtos)
# async def update_produto(request:ProdutosSchema, id: int, db: Session = Depends(get_db)):
#     user_on_db = db.query(Produtos).filter(Produtos.id == id).first()
#     print(user_on_db)
#     if user_on_db is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem produto com este id')
#     user_on_db = Produtos(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
#     db.up
#     db.(user_on_db)
#     db.commit()
#     db.refresh(user_on_db)
#     return user_on_db, Response(status_code=status.HTTP_204_NO_CONTENT)


# router = APIRouter()'''