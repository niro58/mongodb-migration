from enum import Enum
from typing import Tuple

from modules.repository import Repository


class ActionsEnum(Enum):
    MOVE_TO = 1
    COPY_TO = 2


def _get_action() -> ActionsEnum:
    print("""
          1. Move to
          2. Copy to
          """)
    try:
        action = int(input("Enter action: "))
    except ValueError:
        print("Invalid action")
        _get_action()

    return ActionsEnum(action)


def _get_repository() -> Repository:
    db = input("Enter database name: ")
    collection = input("Enter collection name: ")
    return Repository(db, collection)


def get_actions() -> Tuple[Repository, Repository, ActionsEnum]:
    return _get_repository(), _get_repository(), _get_action()
