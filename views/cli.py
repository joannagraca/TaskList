from typing import List
import controllers.task_list_controller as tlc

def cli() -> None:
    tlc.task_controller.init_task_list()
    
    while True:
        line: str = input()
        commands: List[str] = line.split(" ")
        command: str = commands[0].upper()
        task_id: int
        task: list
    
        if command == "RT":
            task_description: str = " ".join(commands[1:len(commands)])
            task_id = tlc.task_controller.task_register(task_description)
            print(f"Tarefa registada com identificador {task_id}")
    
    
        elif command == "LT":
            tasks: list = tlc.task_controller.get_tasks_list()
            if len(tasks) == 0:
                print("Sem tarefas registadas.")
            else:
                print("Id", "Descrição", "Concluida")
                for task in tasks:
                    print(task.id, task.descricao, "Sim" if task.concluida else "Não")

    
        elif command == "MT":
            task_id = int(commands[1])
            if tlc.task_controller.mark_task(task_id):
                print("Tarefa cumprida.")
            else:
                print("Tarefa inexistente.")
                
    
        elif command == "DT":
            task_id = int(commands[1])
            if not tlc.task_controller.delete_task(task_id):
                print("Tarefa inexistente.")
            else:
                print("Tarefa eliminada com sucesso.")


        elif command == "Q":
            break
        
        else:
            print("Instrução inválida.")

        