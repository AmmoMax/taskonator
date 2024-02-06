from dataclasses import dataclass


@dataclass
class User:
    telegram_id: int
    first_name: str
    username: str
    status: str = 'user'
