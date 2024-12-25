import uuid
from datetime import datetime
from typing import List

import sqlalchemy
from sqlalchemy import Index, String, Text, UniqueConstraint, types
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from src.domains.command.configuration import DBConfig

db_config = DBConfig()
metadata_obj = sqlalchemy.MetaData(schema=db_config.POSTGRES_SCHEMA_NAME)


class Base(DeclarativeBase):
    metadata = metadata_obj


class DBFamily(Base):
    __tablename__ = "family"

    id: Mapped[uuid.UUID] = mapped_column(types.Uuid, primary_key=True)
    name: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(types.DateTime(), default=func.now())
    updated_at: Mapped[datetime] = mapped_column(types.DateTime(), default=func.now(), onupdate=func.now())

    users: Mapped[List["DBUser"]] = relationship(back_populates="family", cascade="all, delete-orphan")


class DBUser(Base):
    __tablename__ = "user"

    id: Mapped[uuid.UUID] = mapped_column(types.Uuid, primary_key=True)
    family_id: Mapped[uuid.UUID] = mapped_column(types.Uuid, sqlalchemy.ForeignKey("family.id"), nullable=True)
    name: Mapped[str]
    balance: Mapped[int]
    is_admin: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(types.DateTime(), default=func.now())
    updated_at: Mapped[datetime] = mapped_column(types.DateTime(), default=func.now(), onupdate=func.now())

    family: Mapped["DBFamily"] = relationship(back_populates="users", cascade="all, delete-orphan")
    tasks: Mapped[List["DBTask"]] = relationship(back_populates="user")


class DBTask(Base):
    __tablename__ = "task"

    id: Mapped[uuid.UUID] = mapped_column(types.Uuid, primary_key=True)
    description: Mapped[str]
    user_id: Mapped[uuid.UUID] = mapped_column(types.Uuid, sqlalchemy.ForeignKey("user.id"))
    cost: Mapped[int]
    status: Mapped[str]
    expiration_date: Mapped[datetime]
    created_at: Mapped[datetime] = mapped_column(types.DateTime(), default=func.now())
    updated_at: Mapped[datetime] = mapped_column(types.DateTime(), default=func.now(), onupdate=func.now())

    user: Mapped["DBUser"] = relationship(back_populates="tasks")
