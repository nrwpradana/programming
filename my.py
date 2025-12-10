from cs1graphics import *
import math
import time


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


# ==================== GIRAFFE ====================
class Giraffe(Animal):
    """Giraffe with a longer, more realistic neck."""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.step = 0

        # --------------------------------------------------
        # BODY
        # --------------------------------------------------
        body = Ellipse(90, 130, Point(0, 70))  
        body.setFillColor("goldenrod")
        body.setBorderColor("black")
        body.setBorderWidth(3)
        self.layer.add(body)

        # --------------------------------------------------
        # LONG NECK (EXTENDED MUCH HIGHER)
        # --------------------------------------------------
        self.neck = Polygon(
            Point(-15, -90),   # top-left of neck
            Point(15, -90),    # top-right
            Point(30, 30),     # bottom-right of neck
            Point(-30, 30)     # bottom-left
        )
        self.neck.setFillColor("goldenrod")
        self.neck.setBorderColor("black")
        self.neck.setBorderWidth(3)
        self.layer.add(self.neck)

        # --------------------------------------------------
        # HEAD (raised high to match long neck)
        # --------------------------------------------------
        # --------------------------------------------------
# HEAD GROUP (Everything in one layer)
# --------------------------------------------------
        self.head_layer = Layer()

        # Head shape
        head = Polygon(
            Point(-12, -100),
            Point(12, -100),
            Point(25, -85),
            Point(10, -70),
            Point(-15, -70)
        )
        head.setFillColor("goldenrod")
        head.setBorderColor("black")
        head.setBorderWidth(3)
        self.head_layer.add(head)

        # Ears
        ear_left = Ellipse(10, 18, Point(-18, -108))
        ear_left.setFillColor("goldenrod")
        ear_left.setBorderColor("black")
        self.head_layer.add(ear_left)

        ear_right = Ellipse(10, 18, Point(18, -108))
        ear_right.setFillColor("goldenrod")
        ear_right.setBorderColor("black")
        self.head_layer.add(ear_right)

        # Horns (ossicones)
        horn1 = Rectangle(5, 15, Point(-6, -118))
        horn2 = Rectangle(5, 15, Point(6, -118))
        horn1.setFillColor("black")
        horn2.setFillColor("black")
        self.head_layer.add(horn1)
        self.head_layer.add(horn2)

        # Eye
        eye = Circle(4, Point(10, -92))
        eye.setFillColor("black")
        self.head_layer.add(eye)

        # Add head layer last (on top)
        self.layer.add(self.head_layer)


        # --------------------------------------------------
        # LEGS (position corrected for taller neck)
        # --------------------------------------------------
        self.legs = []
        leg_x = [-25, -8, 8, 25]
        base_y = 150

        for dx in leg_x:
            leg = Rectangle(12, 80, Point(dx, base_y))
            leg.setFillColor("goldenrod")
            leg.setBorderColor("black")
            leg.setBorderWidth(3)
            self.layer.add(leg)
            self.legs.append(leg)

        # Hooves
        for dx in leg_x:
            hoof = Rectangle(14, 10, Point(dx, base_y + 48))
            hoof.setFillColor("black")
            self.layer.add(hoof)

        # --------------------------------------------------
        # TAIL
        # --------------------------------------------------
        tail = Path(Point(-45, 80), Point(-55, 120))
        tail.setBorderColor("black")
        tail.setBorderWidth(4)
        self.layer.add(tail)

        tuft = Circle(7, Point(-55, 128))
        tuft.setFillColor("black")
        self.layer.add(tuft)

        # --------------------------------------------------
        # SPOTS
        # --------------------------------------------------
        spots = [
            (0, 40), (-15, 55), (15, 60),
            (-10, 85), (10, 95),
            (-5, 110), (15, 115)
        ]

        for sx, sy in spots:
            spot = Polygon(
                Point(sx - 10, sy - 5),
                Point(sx + 10, sy - 5),
                Point(sx + 14, sy + 5),
                Point(sx, sy + 14),
                Point(sx - 14, sy + 5)
            )
            spot.setFillColor("saddlebrown")
            spot.setBorderColor("black")
            self.layer.add(spot)

    # ------------------------------------------------------
    # ANIMATION
    # ------------------------------------------------------
    def walk(self):
        self.step += 8
        move = math.sin(math.radians(self.step)) * 4

        self.legs[0].move(0, move)
        self.legs[2].move(0, move)
        self.legs[1].move(0, -move)
        self.legs[3].move(0, -move)

    def swayNeck(self):
        # Move neck and whole head together (ears, eyes, horns fixed)."""
        sway = math.sin(math.radians(self.step)) * 2
        self.neck.move(sway, 0)
        self.head_layer.move(sway, 0)




# ==================== SIMPLE CARTOON ELEPHANT (ORANGE) ====================
class Elephant(Animal):
    """Elephant facing RIGHT, longer body, and tail added."""

    def __init__(self, x, y):
        super().__init__(x, y)
        self.leg_angle = 0
        self.trunk_angle = 0

        # ============================================
        # LONGER BODY (stretched horizontally)
        # ============================================
        body = Ellipse(200, 110, Point(-10, 20))   # widened from 160 → 200
        body.setFillColor("orange")
        body.setBorderColor("black")
        body.setBorderWidth(4)
        self.layer.add(body)

        # ============================================
        # TAIL (attached to back of body)
        # ============================================
        self.tail = Path(
            Point(-105, 15),
            Point(-125, 25),
            Point(-115, 35)
        )
        self.tail.setBorderColor("black")
        self.tail.setBorderWidth(6)
        self.layer.add(self.tail)

        # ============================================
        # HEAD + TUSK FUSED AS ONE SHAPE (never detaches)
        # ============================================
        head_tusk = Polygon(
            Point(40, -40),     
            Point(75, -20),      
            Point(85, -5),       
            Point(110, 15),      
            Point(95, 25),       
            Point(80, 10),       
            Point(70, 25),       
            Point(50, 40),       
            Point(20, 20),       
            Point(25, -10)       
        )
        head_tusk.setFillColor("orange")
        head_tusk.setBorderColor("black")
        head_tusk.setBorderWidth(4)
        self.layer.add(head_tusk)

        # EYE
        eye = Circle(5, Point(70, -10))
        eye.setFillColor("black")
        self.layer.add(eye)

        # EAR (attached)
        ear = Ellipse(70, 85, Point(5, -5))
        ear.setFillColor("orange")
        ear.setBorderColor("black")
        ear.setBorderWidth(4)
        self.layer.add(ear)

        # TRUNK
        self.trunk = Path(
            Point(80, 10),
            Point(110, 40),
            Point(90, 75)
        )
        self.trunk.setBorderColor("black")
        self.trunk.setBorderWidth(10)
        self.layer.add(self.trunk)

        # LEGS (stretched slightly to match longer body)
        self.legs = []
        for dx in [-70, -30, 20, 60]:
            leg = Ellipse(45, 55, Point(dx, 70))
            leg.setFillColor("orange")
            leg.setBorderColor("black")
            leg.setBorderWidth(4)
            self.layer.add(leg)
            self.legs.append(leg)

    # ============================================
    # Walking animation
    # ============================================
    def walk(self):
        self.leg_angle += 15
        shift = math.sin(math.radians(self.leg_angle)) * 3
        for i, leg in enumerate(self.legs):
            leg.move(0, shift if i % 2 == 0 else -shift)

        # Tail wag (optional)
        self.tail.move(math.sin(math.radians(self.leg_angle)) * 0.8, 0)

    # ============================================
    # Trunk sway
    # ============================================
    def swingTrunk(self):
        self.trunk_angle += 10
        sway = math.sin(math.radians(self.trunk_angle)) * 3
        self.trunk.move(sway, 0)





# ==================== RABBIT ====================
class Rabbit(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.hop_phase = 0
        self.ground_y = y  # stay on the ground!

        body = Ellipse(20, 25, Point(0, 0))
        body.setFillColor("white")
        body.setBorderColor("black")
        body.setBorderWidth(2)
        self.layer.add(body)

        head = Circle(10, Point(0, -15))
        head.setFillColor("white")
        self.layer.add(head)

        for dx in (-6, 6):
            ear = Ellipse(4, 15, Point(dx, -25))
            ear.setFillColor("pink")
            self.layer.add(ear)

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
        """Rabbits hop up and down but ALWAYS return to ground level."""
        self.hop_phase += 25
        hop_height = abs(math.sin(math.radians(self.hop_phase))) * 10

        # NEW: always keep rabbit at ground level + hop height
        self.moveTo(self.x, self.ground_y - hop_height)



# ==================== BIRD ====================
class Bird(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.phase = 0

        # Body
        self.body = Ellipse(30, 20, Point(0, 0))
        self.body.setFillColor("white")
        self.body.setBorderColor("black")
        self.body.setBorderWidth(2)
        self.layer.add(self.body)

        # Head
        head = Circle(10, Point(12, -5))
        head.setFillColor("white")
        head.setBorderColor("black")
        head.setBorderWidth(2)
        self.layer.add(head)

        # Beak
        beak = Polygon(Point(20, -5), Point(28, -2), Point(20, 1))
        beak.setFillColor("orange")
        beak.setBorderColor("black")
        self.layer.add(beak)

        # LEFT WING
        self.left_wing = Polygon(
            Point(-5, -5),
            Point(-25, -10),
            Point(-40, 0),
            Point(-25, 12),
            Point(-8, 3)
        )
        self.left_wing.setFillColor("white")
        self.left_wing.setBorderColor("black")
        self.left_wing.setBorderWidth(2)
        self.layer.add(self.left_wing)

        # RIGHT WING
        self.right_wing = Polygon(
            Point(-5, -5),
            Point(15, -10),
            Point(30, 0),
            Point(15, 12),
            Point(-8, 3)
        )
        self.right_wing.setFillColor("white")
        self.right_wing.setBorderColor("black")
        self.right_wing.setBorderWidth(2)
        self.layer.add(self.right_wing)

    def flapWings(self):
        """Stable cs1graphics-compatible wing movement."""
        self.phase += 10
        flap = math.sin(math.radians(self.phase)) * 5

        # Move wings up/down, but KEEP them attached
        self.left_wing.move(0, flap)
        self.right_wing.move(0, -flap)


# ==================== SCENE SETUP ====================
canvas = Canvas(900, 600)
canvas.setTitle("Noah's Ark - Two by Two")

# Ground
ground = Rectangle(900, 150, Point(450, 525))
ground.setFillColor("darkgreen")
ground.setBorderWidth(0)
canvas.add(ground)

# Ark (simple version)
ark = Layer()
ark_body = Rectangle(250, 120, Point(750, 380))
ark_body.setFillColor("sienna")
ark_body.setBorderColor("black")
ark_body.setBorderWidth(4)
ark.add(ark_body)

ark_door = Rectangle(60, 80, Point(680, 400))
ark_door.setFillColor("peru")
ark_door.setBorderColor("black")
ark_door.setBorderWidth(4)
ark.add(ark_door)

canvas.add(ark)


# ==================== CREATE ANIMAL PAIRS ====================
pairs = [
    (Giraffe(50, 400), Giraffe(20, 430)),
    (Elephant(50, 420), Elephant(10, 460)),
    (Rabbit(50, 480), Rabbit(80, 490)),
    (Bird(200, 250), Bird(240, 260)),
]

# Active animals on canvas (start empty)
active = []


# ==================== FUNCTION TO MOVE A PAIR INTO THE ARK ====================
def bring_pair(animalA, animalB, duration=12):
    """
    FAST arrival and immediate entry.
    Duration controls total time per pair.
    """

    canvas.add(animalA.layer)
    canvas.add(animalB.layer)

    door_x = 680  # Ark door
    entry_x = door_x + 60  # Inside ark

    frames = int(duration / 0.03)
    BOOST = 4  # Increase for even faster motion

    # Speeds: fast + smooth
    speedA = ((door_x - animalA.x) / frames) * BOOST
    speedB = ((door_x - animalB.x) / frames) * BOOST

    for frame in range(frames):

        # Move until door is reached
        if animalA.x < door_x:
            animalA.move(speedA, 0)
        else:
            # Immediately continue into ark
            animalA.move(6, 0)

        if animalB.x < door_x:
            animalB.move(speedB, 0)
        else:
            animalB.move(6, 0)

        # Animations
        if isinstance(animalA, Giraffe):
            animalA.walk(); animalA.swayNeck()
        elif isinstance(animalA, Elephant):
            animalA.walk(); animalA.swingTrunk()
        elif isinstance(animalA, Rabbit):
            animalA.hop()
        elif isinstance(animalA, Bird):
            animalA.flapWings()

        if isinstance(animalB, Giraffe):
            animalB.walk(); animalB.swayNeck()
        elif isinstance(animalB, Elephant):
            animalB.walk(); animalB.swingTrunk()
        elif isinstance(animalB, Rabbit):
            animalB.hop()
        elif isinstance(animalB, Bird):
            animalB.flapWings()

        time.sleep(0.03)

        # If BOTH are fully inside, stop early
        if animalA.x >= entry_x and animalB.x >= entry_x:
            break

    # Remove after entering ark
    canvas.remove(animalA.layer)
    canvas.remove(animalB.layer)





# ==================== TWO BY TWO ENTRY ====================
pairs = [
    (Giraffe(50, 400), Giraffe(20, 430)),
    (Elephant(50, 420), Elephant(10, 460)),
    (Rabbit(50, 480), Rabbit(80, 490)),
    (Bird(200, 250), Bird(240, 260)),
]

for A, B in pairs:
    bring_pair(A, B, duration=12)  # 4 × 12 = 48 seconds total

# Final message (4 seconds)
msg = Text("All creatures entered Noah's Ark — Two by Two!", 28, Point(450, 150))
msg.setFontColor("navy")
canvas.add(msg)

time.sleep(4)
canvas.remove(msg)