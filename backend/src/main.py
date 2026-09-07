
from database import supabase
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str
    completed: bool    

@app.get("/")
def read_root():
    return {"message": "¡Hola! Mi API keep it cool man"}

tasks = [
    {"id": 1, "title": "Aprender FastAPI", "completed": False},
    {"id": 2, "title": "Conectar Vue", "completed": False},
    {"id": 3, "title": "Conectar Supabase", "completed": False},
]

@app.get("/tasks")
def get_tasks():
    response = supabase.table("tasks").select("*").execute()
    return response.data

@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = {"id": len(tasks) + 1, "title": task.title, "completed": False}
    tasks.append(new_task)
    return new_task

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_update.title
            task["completed"] = task_update.completed
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Tarea eliminada correctamente"}

    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Tarea eliminada correctamente"}

    raise HTTPException(status_code=404, detail="Tarea no encontrada")