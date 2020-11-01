import unittest
from task.habit_task import HabitTask


class TestHabitTask(unittest.TestCase):

    def setUp(self):
        self.task_1 = HabitTask("Clean garden", 1)

    def tearDown(self):
        pass

    def test_repeat(self):
        self.assertEqual(self.task_1.repeat, 1)

        self.task_1.repeat = 5
        self.assertEqual(self.task_1.repeat, 5)

        with self.assertRaises(ValueError):
            self.task_1.repeat = 9

        with self.assertRaises(TypeError):
            self.task_1.repeat = "3"


if __name__ == '__main__':
    unittest.main()
