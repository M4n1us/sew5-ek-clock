from abc import ABC


class Uhr(ABC):
    """
    Interface for the strategy
    """
    def render(self, params=None):
        pass