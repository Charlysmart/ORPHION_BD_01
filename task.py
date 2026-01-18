from fastapi import APIRouter, HTTPException, status
from schemas.taskSchema import TaskIn
from util.taskvar import tasks

task_router = APIRouter(prefix="/page")

@task_router.post("/add_post")
def add_post(task: TaskIn):
    for t in tasks:
        if task.task_name.lower() == t.task_name.lower():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{task.task_name} already exists in your Todo List!")
    tasks.append(task)

    return {
        "message" : f"{task.task_name} added to your todo list!"
    }

@task_router.get("/get_task")
def get_task():
    if len(tasks) > 0:
        return {
            "tasks" : tasks
        }
    return {
        "detail" : "No task yet!"
    }

@task_router.patch("/update_task")
def update_task(task: str, task_status: bool):
    if task:
        exists = next((t for t in tasks if t.task_name.lower() == task.lower()), None)
        if exists:
            exists.status = task_status
            return f"{task} updated!"
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{task} does not exist in your todo list!")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST , detail=f"{task} not included!")
    
@task_router.delete("/delete_task")
def delete_task(task: str):
    if task:
        index = next((i for i, t in enumerate(tasks) if t.task_name.lower() == task.lower()), None)        
        if index != None:
            if index < 0 or index > len(tasks):
                raise ValueError
            del tasks[index]
            return f"{task} deleted!"
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{task} does not exist in your todo list!")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST , detail=f"{task} not included!")