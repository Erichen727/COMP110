"""File to define Fish class"""

class Fish:
    age: int
    
    def __init__(self, update_age: int = 0):
        self.age = update_age
        return None
    
    def one_day(self):
        self.age += 1
        return None