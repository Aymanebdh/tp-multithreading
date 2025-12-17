def worker(task_queue, result_queue):
    """
    Worker pour traiter les tâches depuis la file.

    Args:
        task_queue: File d'attente des tâches à traiter
        result_queue: File d'attente pour les résultats
    """
    while True:
        task = task_queue.get()

        # Signal de fin
        if task is None:
            break

        # Traitement de la tâche
        task.work()
        result_queue.put((task.identifier, task.time))


if __name__ == "__main__":
    print("Module minion - worker pour le manager TP-2")
