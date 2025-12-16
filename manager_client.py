import multiprocessing as mp
from multiprocessing.managers import BaseManager
from task import Task
from minion import worker

class QueueManager(BaseManager):
    pass

if __name__ == '__main__':
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')
    
    manager = QueueManager(address=('localhost', 50000), authkey=b'secret')
    manager.connect()
    
    task_queue = manager.get_task_queue()
    result_queue = manager.get_result_queue()
    
    num_workers = 4
    workers = []
    for _ in range(num_workers):
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
    
    print("Résultats manager:")
    while not result_queue.empty():
        task_id, exec_time = result_queue.get()
        print(f"Tâche {task_id}: {exec_time:.4f} sec")
