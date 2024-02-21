from typing import Protocol


class PUserManager(Protocol):
    async def create_user(self, username: str, user_id: str):
        pass

    async def assign_task(self, user_id: str, task_id: str) -> bool:
        pass


class UserManager:
    def __init__(self, task_manager, user_store):
        self._task_manager = task_manager
        self._user_store = user_store

    async def create_user(self, username: str, user_id: str):
        user = self._user_store.create_user(username, user_id)
        return user

    async def assign_task(self, user_id: str, task_id: str) -> bool:
        result = await self._user_store.assign_task(user_id, task_id)
        return result
