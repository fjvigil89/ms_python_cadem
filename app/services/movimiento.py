from sqlalchemy.orm import Session
from app.models import movimiento


# movimiento
def get_moves(db: Session):
    moves = db.query(movimiento.Movimiento).limit(100).all()
    return moves


def get_item(db: Session, ean: str):
    move = db.query(movimiento.Movimiento).filter(movimiento.Movimiento.ean == ean).first() 
    return move
