from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from model.task_model import Task
from repositories.task_repository import TaskRepository
from model.user_model import User
from schemas.task_schemas import TaskCreate, TaskUpdate

class TaskService:
    def __init__(self, db: Session):
        self.task_repository = TaskRepository(db)

    def create_task(self, task_data: TaskCreate, current_user: User) -> Task:
        task = Task(
            title=task_data.title,
            description=task_data.description,
            priority=task_data.priority,
            owner_id=current_user.id
        )
        return self.task_repository.create_task(task)
    
    def get_task_by_id(self, task_id: int, current_user: User) -> Task:
        task = self.task_repository.get_by_id(task_id)
        
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Task not found"
                )
            
        if task.owner_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail="You do not have permission to perform this action."
                )
            
        return task
    
    def get_my_tasks(self, current_user: User) -> list[Task]:
        return self.task_repository.get_by_owner_id(current_user.id)
    
    def update_task(self, task_id: int, task_data: TaskUpdate, current_user: User) -> Task:
        
        task = self.get_task_by_id(task_id, current_user)
        
        if task.status == "pending" and task_data.status == "done":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Task must first be in progress before being completed"
            )
            
        task.title = task_data.title
        task.description = task_data.description
        task.priority = task_data.priority
        task.status = task_data.status
        
        return self.task_repository.update_task(task)
    
    def delete_task(self, task_id: int, current_user: User) -> None:
        task = self.get_task_by_id(task_id, current_user)
        self.task_repository.delete_task(task)