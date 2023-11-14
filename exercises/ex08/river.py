"""File to define River class"""

__author__ = "730705343"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]


    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())


    def check_ages(self):
        fish_population: list[Bear] = []
        bear_population: list[Fish] = []
        # Removing fishes with age > 3
        for fishes in self.fish:
            if fishes.age <= 3:
                fish_population.append(fishes)
        # Removing bears with age > 5
        for bear in self.bears:
            if bear.age <= 5:
                bear_population.append(bear)
        self.fish = fish_population
        self.bears = bear_population

    def remove_fish(self, amount: int):
        for i in range(0,amount):
            self.fish.pop(i)
        return None


    def bears_eating(self):
        """Function demonstrating the bears eating the fish."""
        for bear in self.bears:
            if len(self.fish) >=5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    

    def check_hunger(self):
        """Removes bears that are too hungry."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        return None
        
    
    def repopulate_fish(self):
        """Fish repopulating the river with offspring."""
        born_fish: int (len(self.fish) // 2) * 4
        if len((self.fish) / 2) >= 1:
            self.fish.append(Fish() for index in range(born_fish))

        return None
    

    def repopulate_bears(self):
        """Bears repopulating."""
        born_bear: int(len(self.bears) // 2)
        self.bears.append(Bear() for index in range(born_bear))
        return None
    

    def view_river(self):
        print(f"~~~ Day {self.day} ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Fish population: {len(self.bears)}")
        return None

    
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    

    def one_river_week(self):
        """Simulate a whole week of life in the river."""
        for i in range(0, 8):
            self.one_river_day
