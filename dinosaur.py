
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.dino_health = 100

        # Method: 
    def attack (self, robot):
        robot.health -= self.attack_power
        # print ('robot health,', self.health)