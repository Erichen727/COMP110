"""File to define Bear class"""

class Bear:
    age: int
    hunger_score: int
    
    def __init__(self, update_age: int = 0, update_hunger: int = 0):
        self.age = update_age
        self.hunger_score = update_hunger
        return None
    
    def one_day(self):
        self.hunger_score -= 1
        if self.hunger_score < 0:
            self.hunger_score = 0
        self.age += 1
        return None
    
    def eat(self, num_fish: int):
        self.hunger_score += num_fish


