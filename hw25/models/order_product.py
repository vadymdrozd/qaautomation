from __future__ import annotations
from typing import List

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
)

from hw25.core import session
from hw25.models.product import Product
from hw25.models.base import Base


class OrderProduct(Base):
    __tablename__ = "orders_products"

    id = Column(String(5), primary_key=True)
    quantity = Column(Integer)
    order_id = Column(String(5), ForeignKey("orders.id"))
    product_id = Column(String(5), ForeignKey("products.id"))

    @classmethod
    def get_all_by_order_id(cls, order_id: str) -> List[OrderProduct]:
        products_by_order_id = session.query(OrderProduct).filter(OrderProduct.order_id == order_id).all()

        return products_by_order_id

    def insert(self, product: Product, reserving_amount: int) -> None:
        product.increment_reserve(reserving_amount=reserving_amount)
        session.add(self)
        session.commit()