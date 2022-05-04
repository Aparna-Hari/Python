from classes.character import Character

class Pirate(Character):

    def __init__( self , name ):
        super().__init__(name, strength = 15, speed = 3 , health = 100 )

