from cs1graphics import *
import time, math

canvas = Canvas(900, 600)
canvas.setBackgroundColor("lightblue")
canvas.setTitle("Bird")

class Bird:
    def __init__(self, x, y):
        self.layer = Layer()

        body = Ellipse(25,15)
        body.setFillColor("white")
        self.layer.add(body)

        head = Circle(8, Point(10,-8))
        head.setFillColor("white")
        self.layer.add(head)

        wing = Ellipse(20,10,Point(-5,0))
        wing.setFillColor("white")
        self.layer.add(wing)

        beak = Polygon(Point(15,-8), Point(22,-6), Point(15,-4))
        beak.setFillColor("orange")
        self.layer.add(beak)

        self.layer.moveTo(x,y)
        canvas.add(self.layer)

        self.angle = 0

    def fly(self):
        self.angle += 4
        dx = 3
        dy = math.sin(math.radians(self.angle)) * 0.8  # small wave (stay in sky)
        self.layer.move(dx, dy)

# Birds (upper sky)
bird1 = Bird(-150, 40)
bird2 = Bird(-200, 60)
