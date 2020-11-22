import controllers.task_list_controller as tlc


def cli():
    task_list = tlc.create_task_list()
    while True:
        line = input()
        commands = line.split(" ")
        command = commands[0].upper()
        if command == "RT":
            task_description = " ".join(commands[1:len(commands)])
            task_id = tlc.register_task(task_list, task_description)
            print(f"Tarefa registada com identificador {task_id}")
        elif command == "LT":
            tasks = tlc.get_tasks(task_list)
            if len(tasks) == 0:
                print("Sem tarefas registadas.")
            else:
                for task in tasks:
                    print(f"{task[0]} [{task[1]}] {task[2]}")
        elif command == "MT":
            task_id = int(commands[1])
            if not tlc.has_task(task_list, task_id):
                print("Tarefa inexistente.")
            else:
                tlc.mark_task(task_list, task_id)
                print("Tarefa cumprida.")
        elif command == "DT":
            task_id = int(commands[1])
            if not tlc.has_task(task_list, task_id):
                print("Tarefa inexistente.")
            else:
                tlc.delete_task(task_list, task_id)
                print("Tarefa eliminada.")
        elif command == "Q":
            break
        else:
            print("Instrução inválida.")
