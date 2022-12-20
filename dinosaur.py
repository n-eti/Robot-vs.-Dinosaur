from robots import Robot

class Dinosaur:
    def __init__(self, name, attack_power) -> None:
        self.name = 'dino'
        self.attack_power = 20
        self.dino_health = 500

        # Method: 
    def attack (self, robot):
        self.location = 'battlefield'
        self.attack_power -= self.health
        print (self.health)