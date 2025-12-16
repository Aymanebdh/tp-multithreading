import multiprocessing as mp
from task import Task

def main():
    task_queue = mp.Queue()
    result_queue = mp.Queue()
    
    tasks = []
    for i in range(5):
        t = Task(identifier=i, size=800)
        tasks.append(t)
        task_queue.put(t)
    
    print("Boss prêt.")

if __name__ == '__main__':
    main()
