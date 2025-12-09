"""
Noah's Ark Animation – Corrected Version
All constructors fixed, animation logic repaired
"""

from cs1graphics import *
import time
import math

# Canvas setup
canvas = Canvas(800, 600, 'lightblue', "Noah's Ark - A Story of Hope")


# ==================== MESSAGE FUNCTION ====================
def show_message(text, duration=1.5, color="darkblue", size=20, y=50):
    msg = Text(text, size, Point(400, y))
    msg.setFontColor(color)
    msg.setDepth(0)
    canvas.add(msg)
    time.sleep(duration)
    canvas.remove(msg)


# ==================== BASE ANIMAL CLASS ====================
class Animal:
    def __init__(self, x, y):
        self.layer = Layer()
        self.x = x
        self.y = y
        self.layer.moveTo(x, y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.layer.move(dx, dy)

    def moveTo(self, x, y):
        self.layer.moveTo(x, y)
        self.x = x
        self.y = y


# ==================== GIRAFFE CLASS ====================
class Giraffe(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.leg_angle = 0

        # Body
        self.body = Ellipse(40, 60, Point(0, 20))
        self.body.setFillColor("gold")
        self.layer.add(self.body)

        # Neck + head
        self.neck = Rectangle(15, 80, Point(0, -30))
        self.neck.setFillColor("gold")
        self.layer.add(self.neck)

        self.head = Circle(12, Point(0, -65))
        self.head.setFillColor("gold")
        self.layer.add(self.head)

        # Ears
        for dx in (-8, 8):
            ear = Ellipse(6, 10, Point(dx, -72))
            ear.setFillColor("goldenrod")
            self.layer.add(ear)

        # Legs
        self.legs = []
        for dx in (-15, -5, 5, 15):
            leg = Rectangle(6, 35, Point(dx, 50))
            leg.setFillColor("goldenrod")
            self.layer.add(leg)
            self.legs.append(leg)

        # Spots
        for dx, dy in [(0, 10), (-10, 20), (10, 15), (-5, 30), (8, 25)]:
            spot = Circle(4, Point(dx, dy))
            spot.setFillColor("sienna")
            self.layer.add(spot)

        # Tail
        tail = Path(Point(20, 30), Point(28, 45))
        tail.setBorderColor("goldenrod")
        tail.setBorderWidth(3)
        self.layer.add(tail)

    def walk(self):
        self.leg_angle += 15
        offset = math.sin(math.radians(self.leg_angle)) * 3

        # Move alternating legs
        for i, leg in enumerate(self.legs):
            leg.move(0, offset if i % 2 == 0 else -offset)

    def swayNeck(self):
        offset = math.sin(math.radians(self.leg_angle)) * 2
        self.neck.move(offset, 0)
        self.head.move(offset, 0)


# ==================== BIRD CLASS ====================
class Bird(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.wing_angle = 0

        # Body
        body = Ellipse(15, 20, Point(0, 0))
        body.setFillColor("white")
        self.layer.add(body)

        # Head
        head = Circle(8, Point(0, -12))
        head.setFillColor("white")
        self.layer.add(head)

        # Beak
        beak = Polygon(Point(0, -12), Point(6, -11), Point(0, -10))
        beak.setFillColor("orange")
        self.layer.add(beak)

        # Wings
        self.left_wing = Polygon(Point(-8, 0), Point(-25, -8), Point(-20, 5))
        self.left_wing.setFillColor("white")
        self.layer.add(self.left_wing)

        self.right_wing = Polygon(Point(8, 0), Point(25, -8), Point(20, 5))
        self.right_wing.setFillColor("white")
        self.layer.add(self.right_wing)

        # Tail
        tail = Polygon(Point(0, 10), Point(-8, 18), Point(8, 18))
        tail.setFillColor("white")
        self.layer.add(tail)

    def flapWings(self):
        self.wing_angle += 30
        flap = math.sin(math.radians(self.wing_angle)) * 10
        self.left_wing.move(0, flap)
        self.right_wing.move(0, flap)


# ==================== ELEPHANT ====================
class Elephant(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.leg_angle = 0
        self.trunk_angle = 0

        # Body
        body = Ellipse(60, 50, Point(0, 20))
        body.setFillColor("gray")
        self.layer.add(body)

        # Head
        self.head = Circle(20, Point(-15, 0))
        self.head.setFillColor("gray")
        self.layer.add(self.head)

        # Ears
        for dx in (-25, -5):
            ear = Ellipse(18, 25, Point(dx, -5))
            ear.setFillColor("darkgray")
            self.layer.add(ear)

        # Trunk
        self.trunk = Path(Point(-15, 10), Point(-18, 25), Point(-15, 40))
        self.trunk.setBorderWidth(8)
        self.trunk.setBorderColor("gray")
        self.layer.add(self.trunk)

        # Legs
        self.legs = []
        for dx in (-20, -10, 10, 20):
            leg = Rectangle(8, 25, Point(dx, 45))
            leg.setFillColor("darkgray")
            self.layer.add(leg)
            self.legs.append(leg)

    def walk(self):
        self.leg_angle += 15
        offset = math.sin(math.radians(self.leg_angle)) * 2

        for i, leg in enumerate(self.legs):
            leg.move(0, offset if i % 2 == 0 else -offset)

    def swingTrunk(self):
        self.trunk_angle += 10
        swing = math.sin(math.radians(self.trunk_angle)) * 3
        self.trunk.move(swing, 0)


# ==================== RABBIT ====================
class Rabbit(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.hop_phase = 0

        body = Ellipse(20, 25, Point(0, 0))
        body.setFillColor("white")
        self.layer.add(body)

        head = Circle(10, Point(0, -15))
        head.setFillColor("white")
        self.layer.add(head)

        # Ears
        for dx in (-6, 6):
            ear = Ellipse(4, 15, Point(dx, -25))
            ear.setFillColor("pink")
            self.layer.add(ear)

        # Back legs
        self.back_legs = []
        for dx in (-8, 8):
            leg = Ellipse(6, 10, Point(dx, 12))
            leg.setFillColor("white")
            self.layer.add(leg)
            self.back_legs.append(leg)

        tail = Circle(4, Point(0, 12))
        tail.setFillColor("white")
        self.layer.add(tail)

    def hop(self):
        self.hop_phase += 40
        hop_height = abs(math.sin(math.radians(self.hop_phase))) * 8
        self.layer.move(0, -hop_height)


# ==================== ARK ====================
class Ark:
    def __init__(self, x, y):
        self.layer = Layer()

        hull = Rectangle(200, 80)
        hull.setFillColor("sienna")
        hull.setBorderColor("saddlebrown")
        hull.setBorderWidth(3)
        self.layer.add(hull)

        roof = Polygon(Point(-100, -40), Point(0, -70), Point(100, -40), Point(100, 0), Point(-100, 0))
        roof.setFillColor("saddlebrown")
        self.layer.add(roof)

        # Door
        self.door = Rectangle(40, 60, Point(-60, 20))
        self.door.setFillColor("peru")
        self.layer.add(self.door)

        self.layer.moveTo(x, y)
        self.rock_angle = 0

    def rock(self):
        self.rock_angle += 5
        offset = math.sin(math.radians(self.rock_angle)) * 2
        self.layer.move(0, offset)


# ==================== WATER ====================
class Water:
    def __init__(self):
        self.layer = Layer()

        base = Rectangle(800, 300, Point(400, 500))
        base.setFillColor("steelblue")
        base.setBorderWidth(0)
        self.layer.add(base)

        self.waves = []
        for i in range(5):
            wave = Ellipse(100, 20, Point(i * 180 + 50, 350))
            wave.setFillColor("lightskyblue")
            wave.setBorderWidth(0)
            self.layer.add(wave)
            self.waves.append(wave)

        self.phase = 0

    def animate(self):
        self.phase += 5
        for i, wave in enumerate(self.waves):
            offset = math.sin(math.radians(self.phase + i * 40)) * 5
            wave.move(0, offset)


# ==================== RAINBOW ====================
class Rainbow:
    def __init__(self, x, y):
        self.layer = Layer()
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]

        for i, c in enumerate(colors):
            arc = Circle(200 - i * 20)
            arc.setFillColor("lightblue")
            arc.setBorderColor(c)
            arc.setBorderWidth(12)
            self.layer.add(arc)

        self.layer.moveTo(x, y)


# ==================== SUN ====================
class Sun:
    def __init__(self, x, y):
        self.layer = Layer()

        sun = Circle(40)
        sun.setFillColor("yellow")
        self.layer.add(sun)

        # Rays
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            x1 = math.cos(rad) * 50
            y1 = math.sin(rad) * 50
            x2 = math.cos(rad) * 70
            y2 = math.sin(rad) * 70
            ray = Path(Point(x1, y1), Point(x2, y2))
            ray.setBorderColor("gold")
            ray.setBorderWidth(4)
            self.layer.add(ray)

        self.layer.moveTo(x, y)


# ==================== SETUP SCENE ====================
sun = Sun(650, 100);       canvas.add(sun.layer)
water = Water();           canvas.add(water.layer)
ark = Ark(500, 320);       canvas.add(ark.layer)
rainbow = Rainbow(400, 150)
rainbow.layer.setDepth(100)

# Animals
giraffe1 = Giraffe(50, 450)
giraffe2 = Giraffe(20, 480)
elephant1 = Elephant(150, 500)
elephant2 = Elephant(120, 530)
rabbit1 = Rabbit(250, 520)
rabbit2 = Rabbit(280, 525)
bird1 = Bird(100, 200)
bird2 = Bird(130, 220)

for a in [giraffe1, giraffe2, elephant1, elephant2, rabbit1, rabbit2]:
    canvas.add(a.layer)
canvas.add(bird1.layer)
canvas.add(bird2.layer)


# ==================== ANIMATION LOOP ====================
frames = 0
max_frames = 500
shown = {
    'giraffes': False,
    'birds': False,
    'elephants': False,
    'rabbits': False,
    'boarding': False,
    'rainbow': False,
    'safe': False,
    'covenant': False
}

# Opening
show_message("Noah's Ark", 1.4, "navy", 36)
show_message('"Two by two they came to Noah" - Genesis 7:9', 2, "darkblue", 16)

while frames < max_frames:

    if frames < 250:

        if frames == 30 and not shown['giraffes']:
            show_message("The animals arrive two by two...", 1.4, "goldenrod")
            shown['giraffes'] = True

        if frames == 70 and not shown['birds']:
            show_message("Birds glide above in peace", 1.3, "steelblue")
            shown['birds'] = True

        if frames == 110 and not shown['elephants']:
            show_message("More animals follow, steady and calm", 1.4, "gray")
            shown['elephants'] = True

        if frames == 150 and not shown['rabbits']:
            show_message("Small creatures hop with joy", 1.3, "green")
            shown['rabbits'] = True

        if frames == 200 and not shown['boarding']:
            show_message('"Come into the ark," says the Lord', 1.8, "purple")
            shown['boarding'] = True

        # Animal movement
        if giraffe1.x < 350:
            giraffe1.move(1.5, 0); giraffe1.walk(); giraffe1.swayNeck()
        if giraffe2.x < 320:
            giraffe2.move(1.5, 0); giraffe2.walk(); giraffe2.swayNeck()

        if elephant1.x < 380:
            elephant1.move(1, 0); elephant1.walk(); elephant1.swingTrunk()
        if elephant2.x < 350:
            elephant2.move(1, 0); elephant2.walk(); elephant2.swingTrunk()

        if rabbit1.x < 400:
            rabbit1.move(2, 0); 
            if frames % 20 < 10: rabbit1.hop()

        if rabbit2.x < 370:
            rabbit2.move(2, 0)
            if frames % 20 < 10: rabbit2.hop()

        # Birds fly in circle
        angle = frames * 3
        bird1.moveTo(400 + math.cos(math.radians(angle)) * 150,
                     200 + math.sin(math.radians(angle)) * 80)
        bird1.flapWings()

        bird2.moveTo(400 + math.cos(math.radians(angle + 180)) * 150,
                     200 + math.sin(math.radians(angle + 180)) * 80)
        bird2.flapWings()


    # Rainbow phase
    if frames == 250:
        canvas.add(rainbow.layer)
        show_message("God's rainbow of promise appears!", 2, "purple", 22)
        shown['rainbow'] = True

    if frames == 300 and not shown['safe']:
        show_message("All creatures are safe in God's care", 2, "white")
        shown['safe'] = True

    if frames == 350 and not shown['covenant']:
        show_message('"I have set my rainbow in the clouds,"', 2, "white", 16, 520)
        show_message('"It is the sign of My covenant." - Genesis 9:13', 3, "white", 16, 545)
        shown['covenant'] = True

    if frames >= 250:
        ark.rock()
        water.animate()

    time.sleep(0.03)
    frames += 1


# Closing
show_message("A Story of Faith, Hope, and New Beginnings", 3, "navy", 22, 260)
show_message('"The Lord then said to Noah, "Go into the ark"', 2, "darkblue", 16, 300)
show_message('"I have found you righteous in this generation" - Gen 7:1', 3, "darkblue", 16, 330)

print("Animation complete!")
