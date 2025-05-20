from fastapi import APIRouter, HTTPException
from app.services.regon_api import nip_search

router = APIRouter()


@router.get("/{nip}")
def get_data_by_nip(nip: int):
    result = nip_search(nip)
    if "ErrorCode" in result[0]:
        raise HTTPException(status_code=404, detail=result)
    return result
