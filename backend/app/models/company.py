from sqlalchemy import String
from base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column


class Company(BaseModel):
    __tablename__ = "companies"

    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    description: Mapped[str] = mapped_column(String)
