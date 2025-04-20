
import unittest
from creational_patterns.Factories.ui_factory import DarkThemeFactory


class TestUIFactory(unittest.TestCase):
    def test_dark_theme_elements(self):
        factory = DarkThemeFactory()
        button = factory.create_button()
        label = factory.create_label()
        self.assertIn("dark", button.draw().lower())
        self.assertIn("dark", label.render().lower())
