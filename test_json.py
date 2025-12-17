import unittest
from task import Task


class TestTaskJSON(unittest.TestCase):
    def test_json_roundtrip(self):
        a = Task()
        a.solve()

        txt = a.to_json()
        b = Task.from_json(txt)

        self.assertEqual(a, b)

    def test_json_no_solve(self):
        a = Task(5)

        txt = a.to_json()
        b = Task.from_json(txt)

        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
