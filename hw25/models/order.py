from __future__ import annotations

from typing import List, Tuple

from hw25.core import session
from hw25.models.product import Product
from hw25.models.order_product import OrderProduct
from hw25.models.base import Base

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from random import choice
from string import ascii_letters


class Order(Base):
    __tablename__ = "orders"

    id = Column(String(5), primary_key=True)
    destination_address = Column(String(128))
    customer_first_name = Column(String(32))
    customer_last_name = Column(String(32))
    status = Column(String(32))
    orders_products = relationship("OrderProduct")

    @classmethod
    def get_order_by_id(cls, order_id: str) -> Order:
        order = session.query(Order).get(order_id)

        return order

    @classmethod
    def change_order_status(cls, order_id, order_status: str) -> None:
        products_by_order_id = OrderProduct.get_all_by_order_id(order_id)
        if order_status == "Canceled":
            for ordered_product in products_by_order_id:
                product = Product.get_product_by_id(ordered_product.product_id)
                product.reserved_quantity -= ordered_product.quantity
                product.decrement_reserve(ordered_product.quantity)
        elif order_status == "Processed":
            for ordered_product in products_by_order_id:
                product = Product.get_product_by_id(ordered_product.product_id)
                product.reserved_quantity -= ordered_product.quantity
        order = Order.get_order_by_id(order_id=order_id)
        order.status = order_status
        session.commit()

    def create_order(self, products_order: List[Tuple]) -> None:
        session.add(self)
        for item in products_order:
            product, quantity = item
            random_order_id = ''.join(choice(ascii_letters) for i in range(5))
            OrderProduct.create_order_product(
                OrderProduct(id=random_order_id, quantity=quantity, order_id=self.id, product_id=product.id),
                product=product,
                reserving_amount=quantity
            )
        session.commit()
