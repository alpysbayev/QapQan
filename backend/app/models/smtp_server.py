from sqlalchemy import String, Boolean
from user import User
from base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship


class SMTPServer(BaseModel):
    __tablename__ = "smtp_servers"

    name: Mapped[str] = mapped_column(String)
    from_email: Mapped[str] = mapped_column(String)
    host: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(String)
    hashed_password: Mapped[str] = mapped_column(String)

    user: Mapped["User"] = relationship("User", back_populates="smtp_servers")