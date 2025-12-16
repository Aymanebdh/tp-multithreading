import multiprocessing as mp
from task import Task
from minion import worker

if __name__ == '__main__':
    task_queue = mp.Queue()
    result_queue = mp.Queue()
    
    num_workers = 4
    workers = []
    for i in range(num_workers):
        p = mp.Process(target=worker, args=(task_queue, result_queue))
        p.start()
        workers.append(p)
    
    num_tasks = 8
    for i in range(num_tasks):
        t = Task(identifier=i, size=600)
        task_queue.put(t)
    
    for _ in range(num_workers):
        task_queue.put(None)
    
    for p in workers:
        p.join()
    
    print("Résultats :")
    while not result_queue.empty():
        task_id, exec_time = result_queue.get()
        print(f"Tâche {task_id}: {exec_time:.4f} sec")
