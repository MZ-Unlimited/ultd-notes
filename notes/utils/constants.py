from typing import Any, Dict

DEACTIVATED_JSON: Dict[str, Any] = {"CODE": 100, "INFO": "DEACTIVATED"}
SUCCESS_JSON: Dict[str, Any] = {"CODE": 200, "INFO": "SUCCESS"}
ERROR_JSON: Dict[str, Any] = {"CODE": 500, "INFO": "GENERAL ERROR"}
ERROR_EXISTS_JSON: Dict[str, Any] = {"CODE": 400, "INFO": "ERROR EXISTS"}
ERROR_DOES_NOT_EXIST_JSON: Dict[str, Any] = {
    "CODE": 400,
    "INFO": "ERROR DOES NOT EXIST",
}
ERROR_INVALID_ID: Dict[str, Any] = {
    "CODE": 400,
    "INFO": "ERROR INVALID ID - ID NOT FOUND",
}

DATE_FORMAT: Dict[str, Any] = {
    "full": "%Y-%m-%d %H:%M:%S",
    "date_only": "%Y-%m-%d",
    "time_only": "%H:%M:%S",
    "full_br": "%d/%m/%Y %H:%M:%S",
    "date_only_br": "%d/%m/%Y",
}
