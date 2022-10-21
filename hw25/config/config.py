from dataclasses import dataclass

from .db_config import DBConfig


@dataclass
class Config:
    db = DBConfig()

config = Config()