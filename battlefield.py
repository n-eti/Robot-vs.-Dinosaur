from robots import Robot
from dinosaur import  Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot 
        self.diniosaur = Dinosaur

    def run_game(self):
        pass

    def display_welcome(self):
        print ('Get ready for the fight of the millennium as Dinosaur fights Robot!')
        print('May the odds be ever in your favor!')

    def battle_phase(self):
        pass

    def display_winner(self):
        if (self.health <= 0)
            print('Robot has no health points left. Dinosaur wins!')
        
        elif (self.dino_health <= 0):
            print('Dinosaur has no health points left. Robot wins!')
        