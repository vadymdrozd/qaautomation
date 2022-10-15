from __future__ import annotations

from typing import List, Tuple


class Product:
    def __init__(
            self,
            id: str,
            name: str,
            quantity: int,
            price: int,
    ):
        self.__id = id
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    @classmethod
    def from_cursor_data(cls, data: List[Tuple]) -> List[Product]:
        products = []
        for item in data:
            products.append(cls(*item))

        return products

    def __str__(self):
        return f'{self.__name} | {self.__quantity} | {self.__price}'
