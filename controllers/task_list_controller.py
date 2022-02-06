from typing import Optional
import models.tasks as tks

class task_controller:

    # Inicializa a lista de tarefas
    def init_task_list():
        tks.task_list = tks.task_list()

    # Regista uma nova tarefa com a Descrição indicada
    def task_register(descricao):
        new_task = tks.task_list.add_task(descricao)
        return new_task.id

    # Obtém a lista de tarefas
    def get_tasks_list():
        return tks.task_list.get_task_list()

    # Marca uma tarefa como completada
    def mark_task(id) -> None:
        if task_controller.has_task(id):
            tks.task_list.mark_task(id)
            return True
        else:
            return False
            
    # Elimina a tarefa indicada
    def delete_task(id):
        if task_controller.has_task(id):
            tks.task_list.remove_task(id)
            return True
        else:
            return False

    # Verifica se existe a tarefa com o id indicado
    def has_task(task_id_to_check: int) -> bool:
        for task in tks.task_list.get_task_list():
            if task.id == task_id_to_check:
                return True
        return False


