from typing import List
from fastapi import APIRouter, Response, Depends, status, Query, HTTPException
from sqlalchemy.orm import Session
from db.database import engine,SessionLocal
from db.models import Sectors as SectorsModel
from schemas.sector import Sectors as SectorsOutput
from sqlalchemy.orm import Session

from db.base import Base

Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/sectors")   

def get_db():
    try:
        db = SessionLocal()
        #TODO 
        yield db
    finally:
        db.close()

@router.post("/addComSchema", status_code=status.HTTP_201_CREATED, description='Add sector')
def add_sector(request:SectorsOutput, db: Session = Depends(get_db)):
        sector_on_db = SectorsModel(id=request.id, namw=request.name)
        sector_on_db = SectorsModel(**request.dict())
        db.add(sector_on_db)
        db.commit()
        return Response(status_code=status.HTTP_201_CREATED)

'''@router.get("/{sector_names}", description="List sectors by name")
def get_sectors(sector_names,db: Session = Depends(get_db)):
    sector_on_db= db.query(SectorsModel).filter(SectorsModel.item == sector_names).first()
    return sector_on_db


@router.get("/sectors/list")
async def get_sectors(db: Session = Depends(get_db)):
    users= db.query(SectorsModel).all()
    return users

#validação no código
@router.delete("/{id}", description="Delete a sector by ID")
def delete_sector(id: int, db: Session = Depends(get_db)):


    sector_on_db = db.query(SectorsModel).filter(SectorsModel.id == id).first()
    if sector_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There\'s no sectors with the given ID')
    db.delete(sector_on_db)
    db.commit()
    return f"The user with the ID: {id}, was deleted.", Response(status_code=status.HTTP_200_OK)

@router.put('/update/{id}', description='Update sector data')
def update_sector(
    id: int,
    sector: SectorsOutput,
    db: Session = Depends(get_db)
    
    ):
    sector_on_db = db.query(SectorsModel).filter_by(id=id).first()
    if sector_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No sector was found with the given ID')
        
    sector_on_db.name = sector.username
    
    db.add(sector_on_db)
    db.commit()
    return "ok"'''

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
#     sector_on_db = db.query(Produtos).filter(Produtos.id == id).first()
#     print(sector_on_db)
#     if sector_on_db is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Sem produto com este id')
#     sector_on_db = Produtos(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
#     db.up
#     db.(sector_on_db)
#     db.commit()
#     db.refresh(sector_on_db)
#     return sector_on_db, Response(status_code=status.HTTP_204_NO_CONTENT)


# router = APIRouter()
