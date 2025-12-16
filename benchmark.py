import time
import multiprocessing as mp
from task import Task
from minion import worker

def sequential(tasks):
    start = time.time()
    for task in tasks:
        task.work()
    return time.time() - start

def parallel(tasks, num_workers):
    task_queue = mp.Queue()
    result_queue = mp.Queue()
    
    workers = []
    for _ in range(num_workers):
        p = mp.Process(target=worker, args=(task_queue, result_queue))
        p.start()
        workers.append(p)
    
    for task in tasks:
        task_queue.put(task)
    
    for _ in range(num_workers):
        task_queue.put(None)
    
    for p in workers:
        p.join()
    
    return

if __name__ == '__main__':
    tasks = [Task(identifier=i, size=800) for i in range(10)]
    
    print("=== Benchmark ===")
    
    seq_time = sequential(tasks.copy())
    print(f"Séquentiel: {seq_time:.4f} sec")
    
    start = time.time()
    parallel(tasks.copy(), 2)
    par2_time = time.time() - start
    print(f"2 workers: {par2_time:.4f} sec (speedup: {seq_time/par2_time:.2f}x)")
    
    start = time.time()
    parallel(tasks.copy(), 4)
    par4_time = time.time() - start
    print(f"4 workers: {par4_time:.4f} sec (speedup: {seq_time/par4_time:.2f}x)")
