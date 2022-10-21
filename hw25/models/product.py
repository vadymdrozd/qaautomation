from __future__ import annotations

from sqlalchemy import (
    Column,
    String,
    Integer,
)
from sqlalchemy.orm import relationship

from hw25.exceptions.insufficient_amount import InsufficientAmountException
from hw25.core import session
from hw25.models.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(String(5), primary_key=True)
    name = Column(String(128), unique=True)
    price = Column(Integer)
    quantity = Column(Integer)
    reserved_quantity = Column(Integer)
    orders_products = relationship("OrderProduct")

    @classmethod
    def get_by_id(cls, product_id: str) -> Product:
        product = session.query(Product).get(product_id)

        return product

    def __str__(self):
        return f"{self.name} | {self.price} | {self.quantity} | {self.reserved_quantity}"

    def insert(self) -> None:
        session.add(self)
        session.commit()

    def increment_reserve(self, reserving_amount: int) -> None:
        if self.quantity < reserving_amount:
            raise InsufficientAmountException('There is no such a lot products you want')
        self.quantity = self.quantity - reserving_amount
        self.reserved_quantity = self.reserved_quantity + reserving_amount
        session.commit()

    def decrement_reserve(self, reserved_amount: int) -> None:
        self.quantity = self.quantity + reserved_amount
        session.commit()
