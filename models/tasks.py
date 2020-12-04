def create_task(task_description: str, task_id: int) -> list:
    return [task_id, "Por completar", task_description]


def get_id(task: list) -> int:
    return task[0]


def mark_task(task: list) -> None:
    task[1] = "Completa"
