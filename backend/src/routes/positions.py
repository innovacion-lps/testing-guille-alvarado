from fastapi import APIRouter, Depends, HTTPException
from auth import get_current_user
from database import supabase
from models.position import PositionCreate

router = APIRouter()


@router.get("/positions")
def get_positions(user=Depends(get_current_user)):
    response = supabase.table("positions").select("*").eq("user_id", user.id).execute()
    return response.data


@router.post("/positions")
def create_position(position: PositionCreate, user=Depends(get_current_user)):
    payload = position.model_dump()
    payload["user_id"] = user.id
    try:
        response = supabase.table("positions").insert(payload).execute()
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"No se pudo guardar la posición: {error}")
    if not response.data:
        raise HTTPException(
            status_code=500,
            detail="Supabase no devolvió la posición creada (posible RLS o tabla positions sin policy para este usuario)",
        )
    return response.data[0]
