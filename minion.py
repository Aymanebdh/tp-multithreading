import multiprocessing as mp
from task import Task

def worker(task_queue, result_queue):
    while True:
        task = task_queue.get()
        
        if task is None:
            break
        
        task.work()
        result_queue.put((task.identifier, task.time))

if __name__ == '__main__':
    print("Module minion.")
