from fastapi import APIRouter, HTTPException
from database import supabase
from models.task import TaskCreate, TaskUpdate

router = APIRouter()


@router.get("/tasks")
def get_tasks():
    response = supabase.table("tasks").select("*").execute()
    return response.data


@router.post("/tasks")
def create_task(task: TaskCreate):
    response = supabase.table("tasks").insert({
        "title": task.title,
        "completed": False
    }).execute()

    return response.data[0]


@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    response = (
        supabase
        .table("tasks")
        .select("*")
        .eq("id", task_id)
        .execute()
    )

    if not response.data:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    return response.data[0]


@router.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    response = (
        supabase
        .table("tasks")
        .update({
            "title": task_update.title,
            "completed": task_update.completed
        })
        .eq("id", task_id)
        .execute()
    )

    if not response.data:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    return response.data[0]


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    response = (
        supabase
        .table("tasks")
        .delete()
        .eq("id", task_id)
        .execute()
    )

    if not response.data:
        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    return {"message": "Tarea eliminada correctamente"}