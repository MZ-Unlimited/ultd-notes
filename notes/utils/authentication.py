from typing import Annotated, Optional

from fastapi import Header, HTTPException

from notes.config import settings


async def needs_api_key(x_api_key: Annotated[Optional[str], Header()]) -> None:
    if not x_api_key or x_api_key != settings.API_KEY_VALUE:
        raise HTTPException(status_code=400, detail="Invalid X-Api-Key header.")
