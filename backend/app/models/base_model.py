from sqlalchemy import Integer, DateTime, Column
from ..database import Base
from datetime import datetime as dt
from sqlalchemy.orm import Mapped, mapped_column, MappedColumn


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[str] = MappedColumn(Integer, primary_key=True, index=True)
    created_at: Mapped[str] = MappedColumn(DateTime, default=dt.utcnow)
    updated_at: Mapped[str] = MappedColumn(DateTime, default=dt.utcnow, onupdate=dt.utcnow)

