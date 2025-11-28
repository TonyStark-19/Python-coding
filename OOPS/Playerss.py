# This program demonstrates use of instance variables and counter.

class Player:
    # track count of players
    count = 0

    # instance method
    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.count += 1

    # class method
    @classmethod
    def get_total_players(cls):
        print(f"Total players are = {cls.count}")

p1 = Player("Aditya", 3)
p2 = Player("Aman", 2)
p3 = Player("Ajay", 4)

Player.get_total_players()