from weapon import Weapon
from battlefield import Battlefield

class Robot:
    def __init__(self, name) -> None:
        self.name = 'robo'
        self.health = 100
        self.active_weapon = Weapon, 10
    
    def attack(self, dinosaur):
        self.location = 'battlefield'
        self.active_weapon -= self.dino_health
        print('dinosaur health,' self.dino_health)
        