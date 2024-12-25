import sys
from typing import Any


def json_logger_config_factory(level: str) -> dict[str, Any]:
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "json": {
                # "()": ilogging.Formatter,
                "timestamp": True,
                "static_fields": {"format": "app-python"},
                "reserved_attrs": {
                    "levelno",
                    "name",
                    "args",
                    "filename",
                    "module",
                    "funcName",
                    "created",
                    "msecs",
                    "relativeCreated",
                    "exc_info",
                    "exc_text",
                    "process",
                    "msg",
                    "stack_info",
                    "thread",
                },
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "json",
                "stream": sys.stdout,
            },
        },
        "root": {
            "handlers": ["console"],
            "level": level,
        },
    }
