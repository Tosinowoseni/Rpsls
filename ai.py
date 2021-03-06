from player import player
import random
from time import sleep
class AI(player):

    def __init__(self, name):
        super().__init__()
        self.score = 0
        self.name = name

    def choose_gesture(self):
        self.chosen_gesture = str(random.randit(0,4))
        gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
        sleep(1)
        print(f"{self.name} has picked {gesture_list[int(self.chosen_gesture)]}")