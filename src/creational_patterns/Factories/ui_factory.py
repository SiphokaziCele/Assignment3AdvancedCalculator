from abc import ABC, abstractmethod

# Product Interfaces
class Button(ABC):
    @abstractmethod
    def draw(self):
        pass

class Label(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete Products
class DarkButton(Button):
    def draw(self):
        return "Drawing dark button"

class LightButton(Button):
    def draw(self):
        return "Drawing light button"

class DarkLabel(Label):
    def render(self):
        return "Rendering dark label"

class LightLabel(Label):
    def render(self):
        return "Rendering light label"

# Abstract Factory
class UIFactory(ABC):
    @abstractmethod
    def create_button(self): pass

    @abstractmethod
    def create_label(self): pass

# Concrete Factories
class DarkThemeFactory(UIFactory):
    def create_button(self):
        return DarkButton()
    def create_label(self):
        return DarkLabel()

class LightThemeFactory(UIFactory):
    def create_button(self):
        return LightButton()
    def create_label(self):
        return LightLabel()
