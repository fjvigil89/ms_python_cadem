from sqlalchemy.orm import Session
from app.models import item_master as itemMaster


# item_master
def get_items(db: Session):
    items = db.query(itemMaster.ItemMaster).limit(100).all()
    return items

def get_item(db: Session, ean: str):
    item = db.query(itemMaster.ItemMaster).filter(itemMaster.ItemMaster.i_ean == ean).first() 
    return item

