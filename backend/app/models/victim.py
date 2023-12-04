from sqlalchemy import String, Boolean
from group import Group
from base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Victim(BaseModel):
    __tablename__ = "victims"

    email: Mapped[str] = mapped_column(String)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    position: Mapped[str] = mapped_column(String)

    group: Mapped["Group"] = relationship("Group", back_populates="victims")
