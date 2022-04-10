#Name: Tosin Owoseni
#Title: Rpsls
#File: Player.py
#Date: April 10th 2022

class Player:
    def __init__(self):
        self.name = ''
        self.wins = 0
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.choice = ''

    # Leave blank and override at Human, Computer
    def choose_gesture(self):
        pass