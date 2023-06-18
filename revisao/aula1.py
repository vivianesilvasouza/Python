n = 5
execution_time = [3, 4, 1, 7, 6]
x = 4
y = 2


def can_execute_all_tasks(n, l, x, y):
    execution_time = l.copy()
    num_operations = 0

    while len(execution_time) > 0:
        # escolha a tarefa principal (a que tem maior tempo de execução)
        main_task_index = execution_time.index(max(execution_time))
        execution_time[main_task_index] -= x

        # reduz o tempo de execução das outras tarefas
        for i in range(len(execution_time)):
            if i != main_task_index and execution_time[i] > 0:
                execution_time[i] -= y

        # remove as tarefas concluídas
        execution_time = [t for t in execution_time if t > 0]
        num_operations += 1

    return num_operations

    
    num_operations = can_execute_all_tasks(n, execution_time, x, y)

print(num_operations)