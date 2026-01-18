from pydantic import BaseModel
from typing import Optional

class TaskIn(BaseModel):
    task_name: str
    status: Optional[bool] = False