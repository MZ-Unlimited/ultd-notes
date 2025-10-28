from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Integer, select, String, Text

from notes.utils.base import log_error
from .base import BaseModel


class Note(BaseModel):
    __tablename__ = "note"
    __table_args__ = {"extend_existing": True}

    id = Column("note_cd_id", Integer, primary_key=True)

    title = Column("note_tx_title", String(150), nullable=False)
    description = Column("note_tx_description", Text, nullable=False)
    created_at = Column(
        "note_dt_created_at", DateTime, default=datetime.now, nullable=True
    )

    @classmethod
    async def get_by_title(cls, title: str) -> Optional["Note"]:
        try:
            db_manager = await cls.get_db_manager()
            async with db_manager.transaction() as session:
                return await session.scalar(select(cls).where(cls.title == title))
        except Exception as e:
            log_error(e)
        return None
