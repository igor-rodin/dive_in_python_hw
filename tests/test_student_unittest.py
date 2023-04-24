import sys

sys.path.append("../homeworks")

import unittest
from student import Student


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.st = Student("Иван", "Иванович", "Иванов")

    def test_first_name(self):
        self.assertEqual(self.st.first_name, "Иван")

    def test_middle_name(self):
        self.assertEqual(self.st.middle_name, "Иванович")

    def test_last_name(self):
        self.assertEqual(self.st.last_name, "Иванов")

    def test_name_is_title(self):
        with self.assertRaises(ValueError):
            self.st2 = Student("иван", "Иванович", "Иванов")

    def test_name_is_only_letters(self):
        with self.assertRaises(ValueError):
            self.st2 = Student("Иван", "Иванович", "Иванов123")

    def test_subjects(self):
        self.assertEqual(self.st.subjects, (("математика", "физика", "алгоритмы")))

    def test_validate_mark_raise(self):
        with self.assertRaises(ValueError):
            self.st.validate_mark(20, min_mark=0, max_mark=5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
