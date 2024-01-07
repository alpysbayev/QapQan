from typing import List
from sqlalchemy import Integer, DateTime, Column, String, Boolean, Enum, JSON, Date, ForeignKey
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
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    users: Mapped[List["User"]] = relationship(back_populates="company", foreign_keys='Company.user_id')


class User(CoreModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    is_active: Mapped[str] = mapped_column(Boolean, default=True)

    # ORM feature
    company: Mapped["Company"] = relationship(back_populates="users")
    templates: Mapped[List["Template"]] = relationship(back_populates="user")
    smtp_servers: Mapped[List["SMTPServer"]] = relationship(back_populates="user")
    groups: Mapped[List["Group"]] = relationship(back_populates="user")
    campaigns: Mapped[List["Campaign"]] = relationship(back_populates="user")

class Group(CoreModel):
    __tablename__ = "groups"

    name: Mapped[str] = mapped_column(String)
    user_id: Mapped["User"] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="groups", foreign_keys=user_id)
    victims: Mapped[List["Victim"]] = relationship(back_populates="group")
    campaign: Mapped[List["Campaign"]] = relationship(back_populates="group")

class Victim(CoreModel):
    __tablename__ = "victims"

    email: Mapped[str] = mapped_column(String)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    position: Mapped[str] = mapped_column(String)
    group_id: Mapped["Group"] = mapped_column(ForeignKey("groups.id"))

    group: Mapped["Group"] = relationship(back_populates="victims", foreign_keys=group_id)
    log: Mapped["Log"] = relationship(back_populates="victim")

class Template(CoreModel):
    __tablename__ = "templates"

    name: Mapped[str] = mapped_column(String)
    subject: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)
    is_tracked: Mapped[bool] = mapped_column(Boolean, default=False)
    files: Mapped[str] = mapped_column(String)
    user_id: Mapped["User"] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="templates", foreign_keys=user_id)
    campaign: Mapped[List["Campaign"]] = relationship(back_populates="template")


class SMTPServer(CoreModel):
    __tablename__ = "smtp_servers"

    name: Mapped[str] = mapped_column(String)
    from_email: Mapped[str] = mapped_column(String)
    host: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(String)
    hashed_password: Mapped[str] = mapped_column(String)
    user_id: Mapped["User"] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="smtp_servers", foreign_keys=user_id)
    campaign: Mapped[List["Campaign"]] = relationship(back_populates="smtp_server")


class Campaign(CoreModel):
    __tablename__ = "campaigns"

    name: Mapped[str] = mapped_column(String)
    start_date: Mapped[str] = mapped_column(Date)
    end_date: Mapped[str] = mapped_column(Date)
    user_id: Mapped["User"] = mapped_column(ForeignKey("users.id"))
    group_id: Mapped["Group"] = mapped_column(ForeignKey("groups.id"))
    template_id: Mapped["Template"] = mapped_column(ForeignKey("templates.id"))
    smtp_server_id: Mapped["SMTPServer"] = mapped_column(ForeignKey("smtp_servers.id"))


    user: Mapped["User"] = relationship(back_populates="campaigns", foreign_keys=user_id)
    group: Mapped["Group"] = relationship(back_populates="campaign", foreign_keys=group_id)
    template: Mapped["Template"] = relationship(back_populates="campaign", foreign_keys=template_id)
    smtp_server: Mapped["SMTPServer"] = relationship(back_populates="campaign", foreign_keys=smtp_server_id)
    log: Mapped["Log"] = relationship(back_populates="campaign")

class Log(CoreModel):
    __tablename__ = "logs"

    STATES = Enum("SENDING_ERROR", "EMAIL_SENT", "EMAIL_OPENED", "CLICKED_LINK", "SUBMITTED_DATA", name='enum_states')

    hashed_id: Mapped[str] = mapped_column(String, primary_key=True)
    state: Mapped[str] = mapped_column(STATES)
    submitted_data: Mapped[dict] = mapped_column(JSON)
    victim_id: Mapped["Victim"] = mapped_column(ForeignKey("victims.id"))
    campaign_id: Mapped["Campaign"] = mapped_column(ForeignKey("campaigns.id"))

    victim: Mapped["Victim"] = relationship(back_populates="log", foreign_keys=victim_id)
    campaign: Mapped["Campaign"] = relationship(back_populates="log", foreign_keys=campaign_id)

