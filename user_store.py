from collections import defaultdict
from typing import Protocol


class PUserStore(Protocol):
    async def create_user(self, username: str, user_id: str):
        pass

    async def assign_task(self, user_id: str, task_id: str) -> bool:
        pass


class UserStore:
    def __init__(self):
        """
        {
        user_id: [task_id1, task_id2]
        }
        """
        self._users = defaultdict(list)

    async def assign_task(self, user_id: str, task_id: str) -> bool:
        self._users[user_id].append(task_id)
        return True
