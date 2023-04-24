from rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    def test_create_rect(self):
        self.rect = Rectangle(12, 10)
        self.assertEqual((12, 10), (self.rect.width, self.rect.height))

    def test_set_height(self):
        self.rect = Rectangle(12, 10)
        self.rect.height = 20
        self.assertEqual(20, self.rect.height)

    def test_set_width(self):
        self.rect = Rectangle(12, 10)
        self.rect.width = 20
        self.assertEqual(20, self.rect.width)

    def test_perimeter(self):
        self.rect = Rectangle(12, 10)
        self.assertEqual(44, self.rect.perimetr())

    def test_area(self):
        self.rect = Rectangle(12, 10)
        self.assertEqual(120, self.rect.area())

    def test_width_is_not_negative(self):
        with self.assertRaises(ValueError):
            self.rect = Rectangle(-10, 10)

    def test_height_is_not_negative(self):
        with self.assertRaises(ValueError):
            self.rect = Rectangle(10, -10)


if __name__ == "__main__":
    unittest.main(verbosity=2)
