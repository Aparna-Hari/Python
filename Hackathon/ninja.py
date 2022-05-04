from classes.character import Character

class Ninja(Character):

    def __init__( self , name ):
        super().__init__(name, strength = 10, speed = 5 , health = 100 )


class shadow_Ninja(Ninja):
    def __init__( self , name ):
        super().__init__(name, strength = 20, speed = 20 , health = 100 )