from sqlalchemy import ForeignKey, Column, DateTime, func, String

from app.database.base import Base


class Note(Base):
    id = Column(String(64), primary_key=True)
    user_id = Column(String(64), ForeignKey("user.id", ondelete="CASCADE"))
    title = Column(String(64), nullable=False)
    content = Column(String(1024), nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(
        DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp()
    )
