import multiprocessing as mp
from multiprocessing.managers import BaseManager
from task import Task

class QueueManager(BaseManager):
    pass

def worker(task_queue, result_queue):
    while True:
        task = task_queue.get()
        if task is None:
            break
        task.work()
        result_queue.put((task.identifier, task.time))

if __name__ == '__main__':
    task_queue = mp.Queue()
    result_queue = mp.Queue()
    
    QueueManager.register('get_task_queue', callable=lambda: task_queue)
    QueueManager.register('get_result_queue', callable=lambda: result_queue)
    
    manager = QueueManager(address=('localhost', 50000), authkey=b'secret')
    server = manager.get_server()
    print("Serveur Manager démarré sur localhost:50000")
    server.serve_forever()
