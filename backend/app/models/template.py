from sqlalchemy import String, Boolean
from user import User
from group import Group
from base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Template(BaseModel):
    __tablename__ = "templates"

    name: Mapped[str] = mapped_column(String)
    subject: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)
    is_tracked: Mapped[bool] = mapped_column(Boolean, default=False)
    files: Mapped[str] = mapped_column(String)

    user: Mapped["User"] = relationship("User", back_populates="templates")
    group: Mapped["Group"] = relationship("Group", back_populates="templates")

