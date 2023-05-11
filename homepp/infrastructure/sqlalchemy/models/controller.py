from sqlalchemy import BIGINT
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class Controller(Base):
    __tablename__ = "controllers"

    id: Mapped[int] = mapped_column(
        BIGINT(), primary_key=True, unique=True, index=True
    )
    name = Column(String(50), nullable=False)
    hardware_key = Column(String, nullable=False)
    users = relationship("User", back_populates="controllers")