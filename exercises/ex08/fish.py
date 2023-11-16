"""File to define Fish class."""
__author__ = "730705343"


class Fish:
    """Fish Class."""
    age: int
    
    def __init__(self, update_age: int = 0):
        """Initializing the age of the Fish."""
        self.age = update_age
        return None
    
    def one_day(self):
        """How the fish will age every day."""
        self.age += 1
        return None