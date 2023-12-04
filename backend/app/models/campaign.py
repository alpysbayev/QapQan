from sqlalchemy import String, Boolean, Date
from group import Group
from typing import List
from user import User
from base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Campaign(BaseModel):
    __tablename__ = "campaigns"

    name: Mapped[str] = mapped_column(String)
    start_date: Mapped[str] = mapped_column(Date)
    end_date: Mapped[str] = mapped_column(Date)

    groups: Mapped[List["Group"]] = relationship("Group", back_populates="campaign")
    user: Mapped["User"] = relationship("User", back_populates="campaigns")
