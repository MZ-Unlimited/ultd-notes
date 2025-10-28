from fastapi import APIRouter
from fastapi.responses import JSONResponse

from notes.config import settings

router = APIRouter(responses={404: {"description": "Not found"}})


@router.get("/_meta", response_class=JSONResponse)
async def meta() -> JSONResponse:
    return JSONResponse(
        {
            "name": settings.APP_NAME,
            "description": settings.APP_DESCRIPTION,
            "version": settings.APP_VERSION,
            "time": settings.DEPLOYED_AT,
        }
    )


@router.get("/healthcheck")
async def health_check():
    return {"status": "healthy"}


@router.get("/")
async def root():
    return {
        "Name": "Fabio Marzullo",
        "Email": "fabio@ultd.ai",
        "Description": "This is a demo environment for Golden City Project",
    }
