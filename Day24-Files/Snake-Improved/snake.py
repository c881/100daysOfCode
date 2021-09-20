from turtle import Turtle

# CONSTANTS
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.moved = False

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.tail.position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.moved = True

    def up(self):
        if self.moved and self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.moved = False

    def down(self):
        if self.moved and self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.moved = False

    def right(self):
        if self.moved and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.moved = False

    def left(self):
        if self.moved and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.moved = False
