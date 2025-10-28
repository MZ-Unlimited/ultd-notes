from typing import Optional

from pydantic import BaseModel


class NoteSchema(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
