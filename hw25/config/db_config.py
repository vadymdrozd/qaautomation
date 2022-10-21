from dataclasses import dataclass


@dataclass
class DBConfig:
    database = "store"
    port = "5432"
    host = "localhost"
    user = "vadimdrozd"
    password = "postgres"
