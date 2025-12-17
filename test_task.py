import unittest
import numpy as np
from task import Task


class TestTask(unittest.TestCase):
    def test_solution(self):
        task = Task()
        A, B, x = task.solve()
        np.testing.assert_allclose(A @ x, B, rtol=1e-7, atol=0)


if __name__ == "__main__":
    unittest.main()
