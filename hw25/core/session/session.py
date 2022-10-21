from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from hw25.config import config

engine = create_engine(
                       f"postgresql://"
                       f"{config.db.user}:"
                       f"{config.db.password}@"
                       f"{config.db.host}/"
                       f"{config.db.database}",
)

session: Session = sessionmaker(engine)()