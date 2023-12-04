from sqlalchemy import String, Boolean
from user import User
from template import Template
from victim import Victim
from base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Group(BaseModel):
    __tablename__ = "groups"

    name: Mapped[str] = mapped_column(String)

    victims: Mapped["Victim"] = relationship("Victim", back_populates="group")
    user: Mapped["User"] = relationship("User", back_populates="groups")
    templates: Mapped["Template"] = relationship("Template", back_populates="group")

