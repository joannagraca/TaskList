def create_task(task_description, task_id):
    return [task_id, "Por completar", task_description]


def get_id(task):
    return task[0]


def mark_task(task):
    task[1] = "Completa"