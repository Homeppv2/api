from sqlalchemy import BIGINT
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        BIGINT(), primary_key=True, unique=True, index=True
    )
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    hashed_password = Column(String, nullable=False)
    controller_id = Column(Integer, ForeignKey("controllers.id"))
    controller = relationship("Controller", back_populates="users")