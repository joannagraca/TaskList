import models.tasks as tasks


def create_task_list():
    return [0, []]


def register_task(task_list, task_description):
    task_id = new_task_id(task_list)
    insert_task(task_list, task_id, task_description)
    return task_id


def insert_task(task_list, task_id, task_description):
    new_task = tasks.create_task(task_description, task_id)
    task_list[1].append(new_task)


def new_task_id(task_list):
    task_list[0] += 1
    return task_list[0]


def get_tasks(task_list):
    return task_list[1]


def has_task(task_list, task_id):
    for task in get_tasks(task_list):
        if tasks.get_id(task) == task_id:
            return True
    return False


def get_task(task_list, task_id):
    for task in get_tasks(task_list):
        if tasks.get_id(task) == task_id:
            return task
    return None


def mark_task(task_list, task_id):
    task = get_task(task_list, task_id)
    tasks.mark_task(task)


def delete_task(task_list, task_id):
    tasks:list = get_tasks(task_list)
    tasks.remove(get_task(task_list, task_id))