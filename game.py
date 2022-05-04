from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

class Game:
    def __init__(self, p1, p2):
        self.isrunning = False
        self.p1 = p1
        self.p2 = p2

    def battle(self):
        self.isrunning = True
        while self.isrunning:
            if self.p1.health <= 0 or self.p2.health <=0 :
                self.isrunning = False
            self.p1.attack(self.p2)
            self.p2.show_stats()
            self.p2.attack(self.p1)
            self.p1.show_stats()

game = Game(michelangelo,jack_sparrow)
game.battle()
# michelangelo.show_Name()