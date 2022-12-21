from robots import Robot
from dinosaur import  Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot('Robo') 
        self.dinosaur = Dinosaur('Dino', 30)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Get ready for the fight of the millennium as Dinosaur takes on Robot!')
        print('May the odds be ever in your favor!')

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.dino_health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)

    def display_winner(self):
        if (self.robot.health <= 0):
            print('Robot has no health points left. Dinosaur wins!')
        
        elif (self.dinosaur.dino_health <= 0):
            print('Dinosaur has no health points left. Robot wins!')
        