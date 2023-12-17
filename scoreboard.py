from turtle import Turtle

FONT = ("Courier", 24, "bold")
SCOREBOARD_POSITION = (-280, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update current level on scoreboard on interface"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increase the level of player by 1 and update automatically the score on the screen"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """If detects collision with a car, show "Game Over!" in the middle of the screen for user info."""
        self.home()
        self.write("Game Over!", align="center", font=FONT)
