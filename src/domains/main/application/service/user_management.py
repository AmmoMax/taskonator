from domains.main.application.port.input.user_manager import UserManagerInterface
from domains.main.application.port.output.user_repository import UserRepositoryPort
from domains.main.application.port.output.task_repository import TaskRepositoryPort
from domains.main.domain.user import User


class UserManager(UserManagerInterface):
    def __init__(self, task_repository: TaskRepositoryPort, user_repository: UserRepositoryPort):
        self.task_repository = task_repository
        self.user_repository = user_repository

    async def create_user(self, username: str, user_id: str):
        user = User(username=username, user_id=user_id)
        self.user_repository.create_user(user)

    async def assign_task(self, user_id: str, task_id: str) -> bool:
        result = await self.user_repository.assign_task(user_id, task_id)
        return result

    async def get_user(self, tg_user_id: int) -> User:
        pass
