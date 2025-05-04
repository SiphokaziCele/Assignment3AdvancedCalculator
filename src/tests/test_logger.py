import unittest
from src.creational_patterns.Singletons.logger import Logger

class TestLogger(unittest.TestCase):
    def test_singleton_behavior(self):
        logger1 = Logger()
        logger2 = Logger()
        self.assertIs(logger1, logger2)

    def test_log_capture(self):
        logger = Logger()
        logger.log("Test entry")
        self.assertIn("Test entry", logger.get_logs())
