from typing import List
from sqlalchemy import String, Boolean

from backend.app.database import Base
from base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from template import Template
from smtp_server import SMTPServer
from group import Group


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)

    is_active: Mapped[str] = mapped_column(Boolean, default=True)

    templates: Mapped[List["Template"]] = relationship("Template", back_populates="user")
    smtp_servers: Mapped[List["SMTPServer"]] = relationship("SMTPServer", back_populates="user")
    groups: Mapped[List["Group"]] = relationship("Group", back_populates="user")
