class Character:

    def __init__ (self,name,strength,speed,health):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self

    def attack( self , opponent ):
        opponent.health -= self.strength
        return self
        
    def show_Name(self):
        print(f"Name: {self.name}")
