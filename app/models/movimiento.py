from unicodedata import numeric
from sqlalchemy import Column, Float, ForeignKey, Integer, Numeric, String, Date, UniqueConstraint
from sqlalchemy.orm import relationship

from app.conexion.database import Base


class Movimiento(Base):
    __tablename__ = "movimiento"

    __table_args__ = (UniqueConstraint('fecha', 'retail', 'cod_local', 'cod_item', 'ean', name='move_role_uc'),)
    fecha = Column(Date, primary_key=True, index=True)
    retail = Column(String, primary_key=True, index=True)
    cod_local = Column(String, primary_key=True, index=True)
    cod_item = Column(String, primary_key=True, index=True)
    venta_unidades = Column(Numeric(8, 2), nullable=False, default=0)
    venta_volumen = Column(Numeric(10, 5), nullable=False, default=0)
    ean = Column(String(100), ForeignKey("item_master.i_ean"), primary_key=True, index=True)
    item = relationship("ItemMaster")
    # item = relationship("ItemMaster", back_populates="movimientos")

    def __init__(self, ean: str, venta_unidades, venta_volumen: numeric):
        self.ean = ean
        self.venta_unidades = venta_unidades
        self.venta_volumen = venta_volumen

    def __repr__(self) -> str:
        return f"<Movimiento {self.ean}, {self.venta_volumen}, {self.venta_volumen}>"
