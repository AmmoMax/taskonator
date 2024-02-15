import datetime
from typing import Protocol
from uuid import uuid4


class PTaskStore(Protocol):

    async def create_task(self, description: str,
                          cost: str,
                          expiration_date: datetime.date,
                          status: str) -> None:
        pass

    async def get_task(self, task_id: str):
        pass

    async def update_task_status(self, task_id: str, status: str):
        pass

    async def delete_task(self, task_id: str) -> None:
        pass

    async def get_tasks_by_status(self, status: str) -> list:
        pass


class TaskStore:
    def __init__(self):
        self.store = {}

    async def create_task(self, description: str,
                          cost: str,
                          expiration_date: datetime.date,
                          status: str) -> None:
        task_id = str(uuid4())
        task = {task_id: {'description': description,
                          'status': status,
                          'expiration_date': expiration_date,
                          'cost': cost}}
        self.store.update(task)
        return self.store[task_id]

    async def get_task(self, task_id: str):
        return self.store.get(task_id)

    async def update_task_status(self, task_id: str, status: str):
        task = self.store[task_id]
        task['status'] = status
        return self.store.get(task_id)

    async def delete_task(self, task_id: str) -> None:
        task = self.store[task_id]
        task['status'] = 'deleted'

    async def get_tasks_by_status(self, status: str) -> list:
        tasks_list = []
        for task_id, task_info in self.store.items():
            if task_info['status'] == status:
                tasks_list.append({task_id: task_info})
        return tasks_list
