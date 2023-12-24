from typing import List
from sqlalchemy import Integer, DateTime, Column, String, Boolean, Enum, JSON, Date
from database import Base
from datetime import datetime as dt
from sqlalchemy.orm import Mapped, mapped_column, MappedColumn, relationship


class CoreModel(Base):
    __abstract__ = True
    __tablename__: str = None

    id: Mapped[str] = MappedColumn(Integer, primary_key=True, index=True)
    created_at: Mapped[str] = MappedColumn(DateTime, default=dt.utcnow)
    updated_at: Mapped[str] = MappedColumn(DateTime, default=dt.utcnow, onupdate=dt.utcnow)


class Company(CoreModel):
    __tablename__ = "companies"

    name: Mapped[str] = mapped_column(String, unique=True, index=True)
    description: Mapped[str] = mapped_column(String)


class User(CoreModel):
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


class Group(CoreModel):
    __tablename__ = "groups"

    name: Mapped[str] = mapped_column(String)

    victims: Mapped["Victim"] = relationship("Victim", back_populates="group")
    user: Mapped["User"] = relationship("User", back_populates="groups")
    templates: Mapped["Template"] = relationship("Template", back_populates="group")


class Victim(CoreModel):
    __tablename__ = "victims"

    email: Mapped[str] = mapped_column(String)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    position: Mapped[str] = mapped_column(String)

    group: Mapped["Group"] = relationship("Group", back_populates="victims")


class Template(CoreModel):
    __tablename__ = "templates"

    name: Mapped[str] = mapped_column(String)
    subject: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)
    is_tracked: Mapped[bool] = mapped_column(Boolean, default=False)
    files: Mapped[str] = mapped_column(String)

    user: Mapped["User"] = relationship("User", back_populates="templates")
    group: Mapped["Group"] = relationship("Group", back_populates="templates")


class SMTPServer(CoreModel):
    __tablename__ = "smtp_servers"

    name: Mapped[str] = mapped_column(String)
    from_email: Mapped[str] = mapped_column(String)
    host: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(String)
    hashed_password: Mapped[str] = mapped_column(String)

    user: Mapped["User"] = relationship("User", back_populates="smtp_servers")



class Log(CoreModel):
    __tablename__ = "logs"

    STATES = Enum("SENDING_ERROR", "EMAIL_SENT", "EMAIL_OPENED", "CLICKED_LINK", "SUBMITTED_DATA")

    state: Mapped[str] = mapped_column(STATES)
    submitted_data: Mapped[dict] = mapped_column(JSON)

    victim: Mapped["Victim"] = relationship("Victim", back_populates="logs")
    campaign: Mapped["Campaign"] = relationship("Campaign", back_populates="logs")


class Campaign(CoreModel):
    __tablename__ = "campaigns"

    name: Mapped[str] = mapped_column(String)
    start_date: Mapped[str] = mapped_column(Date)
    end_date: Mapped[str] = mapped_column(Date)

    groups: Mapped[List["Group"]] = relationship("Group", back_populates="campaign")
    user: Mapped["User"] = relationship("User", back_populates="campaigns")
