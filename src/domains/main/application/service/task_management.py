from domains.main.application.port.input.task_manager import TaskManagerInterface
from domains.main.application.port.output.family_repository import FamilyRepositoryPort
from domains.main.application.port.output.task_repository import TaskRepositoryPort
from domains.main.application.port.output.user_repository import UserRepositoryPort
from domains.main.domain.task import Task


class TaskManager(TaskManagerInterface):
    def __init__(self, task_repository: TaskRepositoryPort, user_repository: UserRepositoryPort):
        self._task_repository = task_repository
        self._user_repository = user_repository

    async def get_available_tasks(self, user_id: str) -> list[Task]:
        """
        Get all tasks that are available for the user.
        :param user_id:
        :return:
        """
        user = await self._user_repository.get_user(user_id)
        family_id = user.family_id

        available_family_tasks = await self._task_repository.get_available_tasks(family_id)
        return available_family_tasks


    async def change_task_status(self, task_id: str, status: str):
        pass
