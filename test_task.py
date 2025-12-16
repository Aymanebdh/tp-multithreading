import unittest
import numpy as np
from task import Task

class TestTask(unittest.TestCase):
    def test_solution(self):
        task = Task()
        task.work()  # Résoudre Ax = B
        Ax = task.a @ task.x
        np.testing.assert_allclose(Ax, task.b, rtol=1e-7, atol=0)

if __name__ == '__main__':
    unittest.main()
