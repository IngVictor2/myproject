from datetime import datetime
from sqlalchemy import Enum, ForeignKey, String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from config.database import Base
from schemas.task_schemas import TaskPriority, TaskStatus


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[String] = mapped_column(String(255), nullable=False)
    description: Mapped[String | None] = mapped_column(String(500), nullable=True)
    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus, name="task_status"), nullable=False, default=TaskStatus.PENDING, server_default=TaskStatus.PENDING.value)
    priority: Mapped[TaskPriority] = mapped_column(Enum(TaskPriority, name="task_priority"), nullable=False, default=TaskPriority.MEDIUM, server_default=TaskPriority.MEDIUM.value)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
