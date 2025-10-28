#
# Notes API Service
#
import logging
from typing import Any

from fastapi import APIRouter, Depends, FastAPI, Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from starlette.responses import JSONResponse

from notes.base.middleware import RequestMiddleware
from notes.config import settings
from notes.core.services import (
    note_router,
    root_router,
)
from notes.db.db_manager import get_db_manager
from notes.utils.authentication import needs_api_key

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    dependencies=[Depends(get_db_manager)],
)
app.add_middleware(RequestMiddleware)

keyed_routes = APIRouter(dependencies=[Depends(needs_api_key)])
open_routes = APIRouter()

keyed_routes.include_router(note_router)
open_routes.include_router(root_router)

app.include_router(keyed_routes)
app.include_router(open_routes)


@app.middleware("http")
async def process_after_request(request: Request, call_next: Any) -> Any:
    response = await call_next(request)

    # Access the configuration information set in the request state.
    request_config = getattr(request.state, "request_config", None)
    if request_config:
        db_session = request_config.get("db_session")
        if db_session:
            db_session.close()

    return response


@app.get("/openapi.json")
async def get_open_api_endpoint() -> JSONResponse:
    # auth: str = Depends(needs_api_key)
    if settings.DEBUG:
        return JSONResponse(
            get_openapi(
                title="FastAPI", version=settings.APP_VERSION, routes=app.routes
            )
        )
    return JSONResponse(
        content={"error": "OpenAPI documentation is not available in production."},
        status_code=404,
    )


@app.get("/docs")
@app.get("/redoc")
async def get_documentation() -> Any:
    # auth: str = Depends(needs_api_key)
    if settings.DEBUG:
        return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")
    return None
