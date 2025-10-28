from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

import notes.utils.constants as const
from notes.core.models.db import Note
from notes.core.models.schema import NoteSchema
from notes.utils import make_response
from notes.utils.base import log_error, run_to_dict_async

router = APIRouter(
    responses={404: {"description": "Not found"}},
    prefix="/notes",
)


@router.get("/", response_class=JSONResponse)
async def list_notes(
    page: int = 1,
) -> JSONResponse:
    try:
        _list, total_count, items_per_page = await Note.list_paged(page)
        return make_response(
            await run_to_dict_async(_list),
            pagination_data={
                "page": page,
                "total_count": total_count,
                "items_per_page": items_per_page,
            },
        )
    except Exception as e:
        log_error(e)
    return make_response(const.ERROR_JSON)


@router.get("/{note_id}", response_class=JSONResponse)
async def get_by_id(note_id: int) -> JSONResponse:
    try:
        note = await Note.get_by_id(note_id)
        note_dict = await note.to_dict() if note else {}
        return make_response(
            note_dict,
            pagination_data={
                "page": 1,
                "total_count": 1,
                "items_per_page": 1,
            },
        )
    except Exception as e:
        log_error(e)
    return make_response(const.ERROR_JSON)


@router.post("/", response_class=JSONResponse)
async def create_post(request: Request, note_schema: NoteSchema) -> JSONResponse:
    try:
        db_manager = request.state.request_config["db_manager"]
        async with db_manager.transaction() as db_session:
            note = await Note.get_by_title(note_schema.title)
            if note:
                return make_response(const.ERROR_EXISTS_JSON)

            note = Note()
            note.title = note_schema.title
            note.description = note_schema.description
            db_session.add(note)
            await db_session.flush()
            note_dict = await note.to_dict()
            return make_response(note_dict)
    except Exception as e:
        log_error(e)
    return make_response(const.ERROR_JSON)


@router.put("/", response_class=JSONResponse)
async def update_note(request: Request, note_schema: NoteSchema) -> JSONResponse:
    try:
        db_manager = request.state.request_config["db_manager"]
        async with db_manager.transaction() as db_session:
            note = await Note.get_by_id(note_schema.id)
            if not note:
                return make_response(const.ERROR_DOES_NOT_EXIST_JSON)

            note.title = note_schema.title
            note.description = note_schema.description
            await db_session.flush()
            note_dict = await note.to_dict()
            return make_response(note_dict)
    except Exception as e:
        log_error(e)
    return make_response(const.ERROR_JSON)


@router.delete("/{note_id}", response_class=JSONResponse)
async def delete_note(request: Request, note_id: int) -> JSONResponse:
    response_json = const.SUCCESS_JSON
    try:
        if not note_id:
            return make_response(const.ERROR_INVALID_ID)

        db_manager = request.state.request_config["db_manager"]
        async with db_manager.transaction() as db_session:
            note = await Note.obj_delete(note_id)
            await db_session.flush()

            response_json = (
                "The note was deleted successfully"
                if note
                else "Unable to deleted the note"
            )

    except Exception as e:
        log_error(e)
        response_json = const.ERROR_JSON

    return make_response(response_json)
