from weapon import Weapon

class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('light bolt', 10)
    
    def attack(self, dinosaur):
        # self.location = 'battlefield'
        dinosaur.dino_health -= self.active_weapon.attack_power
        # print('dinosaur health,' self.dino_health)
        
    