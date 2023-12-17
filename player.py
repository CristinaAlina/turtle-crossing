from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.reset_position()

    def reset_position(self):
        """Resets turtle position to starting position"""
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        """Moves the turtle forward 10 paces"""
        self.forward(MOVE_DISTANCE)

    def achieved_finish_line(self):
        """Returns True if player y-coordinate is higher than finish line y-coordinate, or False otherwise"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False
