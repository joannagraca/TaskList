class task:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao
        self.concluida = False




class task_list():

    # Construtor: inicializa a lista de tarefas e o gerador de id's de tarefa
    def __init__(self):
        self.tasks = []
        self.next_task_id : int = 1

    # Adiciona uma tarefa à lista
    def add_task(self, descricao):
        new_task = task(self.next_task_id, descricao)
        self.tasks.append(new_task)
        self.next_task_id = self.next_task_id + 1
        return new_task

    # Remove uma tarefa da lista
    def remove_task(self, id):
        posicao = task_list.get_task_position(id)
        self.tasks.pop(posicao)

    # Obtém a lista de tarefas
    def get_task_list(self):
        return self.tasks

    # Obtém a posição na lista de tarefas corresponde ao id de tarefa
    def get_task_position(self, task_id) -> int:
        position = 0
        for task in self.tasks:
            if task.id == task_id:
                return position
            position = position + 1
        return None

    # Marca uma tarefa como completa
    def mark_task(self, id) -> None:
        posicao = task_list.get_task_position(id)
        self.tasks[posicao].concluida = True
