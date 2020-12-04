from typing import Optional

import models.tasks as tasks


def create_task_list() -> list:
    return [0, []]


def register_task(task_list: list, task_description: str) -> int:
    task_id: int = new_task_id(task_list)
    insert_task(task_list, task_id, task_description)
    return task_id


def insert_task(task_list: list, task_id: int, task_description: str) -> None:
    new_task: list = tasks.create_task(task_description, task_id)
    task_list[1].append(new_task)


def new_task_id(task_list: list) -> int:
    task_list[0] += 1
    return task_list[0]


def get_tasks(task_list) -> list:
    return task_list[1]


def has_task(task_list: list, task_id: int) -> bool:
    task: list
    for task in get_tasks(task_list):
        if tasks.get_id(task) == task_id:
            return True
    return False


def get_task(task_list, task_id) -> Optional[list]:
    task: list
    for task in get_tasks(task_list):
        if tasks.get_id(task) == task_id:
            return task
    return None


def mark_task(task_list, task_id) -> None:
    task: list = get_task(task_list, task_id)
    tasks.mark_task(task)


def delete_task(task_list, task_id) -> None:
    task_list_tasks: list = get_tasks(task_list)
    task_list_tasks.remove(get_task(task_list, task_id))
