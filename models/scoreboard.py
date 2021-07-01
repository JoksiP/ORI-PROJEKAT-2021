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
            self.speed += 1

    def display_score(self):
        text = self.font.render(f'Score:  {str(self.score)}', True, (0, 0, 0))
        self.screen.blit(text, (85, 650))