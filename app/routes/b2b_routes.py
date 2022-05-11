from typing import List
from fastapi import APIRouter, Depends, HTTPException

from app.services import item_master as itemService
from app.services import movimiento as moveService

from app.schemas import item_master as itemSchema 
from app.schemas import movimiento as moveSchema

from app.conexion.database import SessionLocal, engine
from sqlalchemy.orm import Session

# Crear todas las tablas en la BD.
# models.Base.metadata.create_all(bind=engine)
b2b_router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        print('Error: ' + str(type(e)))
    finally:
        db.close_all

# item_master
@b2b_router.get("/items", response_model=List[itemSchema.ItemMaster])
async def get_items(db: Session = Depends(get_db)):
    items = itemService.get_items(db=db)
    return items

@b2b_router.get("/items/{ean}", response_model=itemSchema.ItemMaster)
def get_user(ean: int, db: Session = Depends(get_db)):
    the_item = itemService.get_item(db=db, ean=ean)
    if the_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return the_item


# movimientos
@b2b_router.get("/movimientos", response_model=List[moveSchema.Movimiento])
async def get_moves(db: Session = Depends(get_db)):
    moves = moveService.get_moves(db=db)
    return moves

@b2b_router.get("/movimientos/{ean}", response_model=moveSchema.Movimiento)
def get_user(ean: int, db: Session = Depends(get_db)):
    the_move = moveService.get_moves(db=db, ean=ean)
    if the_move is None:
        raise HTTPException(status_code=404, detail="Movimiento not found")
    return the_move
