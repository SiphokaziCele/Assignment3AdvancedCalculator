
import unittest
from creational_patterns.Factories.results_formatter import PlainTextFormatter

class TestFormatter(unittest.TestCase):
    def test_format_plain_text(self):
        formatter = PlainTextFormatter()
        self.assertEqual(formatter.format(10), "10")
