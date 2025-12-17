import multiprocessing as mp
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

class QueueClient:
    def __init__(self):
        QueueManager.register("get_task_queue")
        QueueManager.register("get_result_queue")

        manager = QueueManager(address=("localhost", 50000), authkey=b"secret")
        manager.connect()

        self.task_queue = manager.get_task_queue()
        self.result_queue = manager.get_result_queue()

if __name__ == "__main__":
    print("QueueClient module pour proxy.py")
