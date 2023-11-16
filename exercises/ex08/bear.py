"""File to define Bear class."""
__author__ = "730705343"


class Bear:
    """Bear Class."""
    age: int
    hunger_score: int
    
    def __init__(self, update_age: int = 0, update_hunger: int = 0):
        """Initializes the hunger_score and the age of the age of the bear."""
        self.age = update_age
        self.hunger_score = update_hunger
        return None
    
    def one_day(self):
        """How the bear will get hungry and age in one day."""
        self.hunger_score -= 1
        self.age += 1
        return None
    
    def eat(self, num_fish: int):
        """How the bear will be able to eat and replenish hunger."""
        self.hunger_score += num_fish