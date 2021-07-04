from utils.util import display_score


class Scoreboard:
    def __init__(self, screen, font, speed_increment):
        self.screen = screen
        self.font = font
        self.score = 0
        self.speed = 15
        self.speed_increment = speed_increment

    def increment_score(self):
        self.score += 1
        if self.score % self.speed_increment == 0:
            if self.speed < 47:
                self.speed += 1

    def display_score(self):
        display_score(self.screen, self.font, str(self.score))
