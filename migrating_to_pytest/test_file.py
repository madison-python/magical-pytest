import unittest


def calculate_offset(page, per_page=10):
    return (page - 1) * per_page


class TestCalculateOffset(unittest.TestCase):

    def test_first_page(self):
        self.assertEqual(calculate_offset(1), 0)

    def test_second_page(self):
        self.assertEqual(calculate_offset(2), 10)
