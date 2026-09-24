from fastapi import APIRouter, Depends
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
    response = supabase.table("positions").insert(payload).execute()
    return response.data[0]
