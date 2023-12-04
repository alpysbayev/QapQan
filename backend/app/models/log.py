from sqlalchemy import String, Boolean, Enum, JSON
from victim import Victim
from campaign import Campaign
from base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship


STATES = Enum("SENDING_ERROR", "EMAIL_SENT", "EMAIL_OPENED", "CLICKED_LINK", "SUBMITTED_DATA")


class Log(BaseModel):
    __tablename__ = "logs"

    state: Mapped[str] = mapped_column(STATES)
    submitted_data: Mapped[dict] = mapped_column(JSON)

    victim: Mapped["Victim"] = relationship("Victim", back_populates="logs")
    campaign: Mapped["Campaign"] = relationship("Campaign", back_populates="logs")
