"""
Noah's Ark Animation - Step by Step Build
A joyful biblical story brought to life with cs1graphics
"""

from cs1graphics import *
import time
import math

# Canvas setup
canvas = Canvas(800, 600, 'lightblue', 'Noah\'s Ark - A Story of Hope')

# ==================== STEP 1: BASE ANIMAL CLASS ====================
class Animal:
    """Base class for all animals"""
    def __init__(self, x, y):
        self.layer = Layer()
        self.x = x
        self.y = y
        self.layer.moveTo(x, y)
    
    def move(self, dx, dy):
        """Move the animal"""
        self.x += dx
        self.y += dy
        self.layer.move(dx, dy)
    
    def moveTo(self, x, y):
        """Move animal to specific position"""
        self.x = x
        self.y = y
        self.layer.moveTo(x, y)

# ==================== STEP 2: BIRD CLASS (YOUR VERSION) ====================
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
        
        # Calculate the difference from previous position
        if not hasattr(self, 'prev_left_flap'):
            self.prev_left_flap = 0
            self.prev_right_flap = 0
        
        left_diff = flap - self.prev_left_flap
        right_diff = -flap - self.prev_right_flap
        
        # Move wings by the difference
        self.left_wing.move(0, left_diff)
        self.right_wing.move(0, right_diff)
        
        # Store current positions
        self.prev_left_flap = flap
        self.prev_right_flap = -flap

# ==================== STEP 3: GIRAFFE CLASS ====================
class Giraffe(Animal):
    """Giraffe with walking animation"""
    def __init__(self, x, y):
        super().__init__(x, y)
        
        # Body
        body = Ellipse(40, 60, Point(0, 20))
        body.setFillColor('gold')
        body.setBorderColor('goldenrod')
        body.setBorderWidth(2)
        self.layer.add(body)
        
        # Neck
        neck = Rectangle(15, 80, Point(0, -30))
        neck.setFillColor('gold')
        neck.setBorderColor('goldenrod')
        neck.setBorderWidth(2)
        self.layer.add(neck)
        
        # Head
        head = Circle(12, Point(0, -65))
        head.setFillColor('gold')
        head.setBorderColor('goldenrod')
        head.setBorderWidth(2)
        self.layer.add(head)
        
        # Ears
        left_ear = Ellipse(6, 10, Point(-8, -72))
        left_ear.setFillColor('goldenrod')
        self.layer.add(left_ear)
        right_ear = Ellipse(6, 10, Point(8, -72))
        right_ear.setFillColor('goldenrod')
        self.layer.add(right_ear)
        
        # Legs
        self.legs = []
        leg_positions = [(-15, 50), (-5, 50), (5, 50), (15, 50)]
        for pos in leg_positions:
            leg = Rectangle(6, 35, Point(pos[0], pos[1]))
            leg.setFillColor('goldenrod')
            leg.setBorderColor('peru')
            self.layer.add(leg)
            self.legs.append(leg)
        
        # Spots
        spot_positions = [(0, 10), (-10, 20), (10, 15), (-5, 30), (8, 25)]
        for pos in spot_positions:
            spot = Circle(4, Point(pos[0], pos[1]))
            spot.setFillColor('sienna')
            self.layer.add(spot)
        
        # Tail
        tail = Path(Point(20, 30), Point(28, 45))
        tail.setBorderColor('goldenrod')
        tail.setBorderWidth(3)
        self.layer.add(tail)
        
        self.leg_angle = 0
    
    def walk(self):
        """Animate walking"""
        self.leg_angle += 20
        offset = math.sin(math.radians(self.leg_angle)) * 3
        
        self.legs[0].move(0, offset)
        self.legs[2].move(0, offset)
        self.legs[1].move(0, -offset)
        self.legs[3].move(0, -offset)

# ==================== STEP 4: ELEPHANT CLASS ====================
class Elephant(Animal):
    """Elephant with walking animation"""
    def __init__(self, x, y):
        super().__init__(x, y)
        
        # Body
        body = Ellipse(60, 50, Point(0, 20))
        body.setFillColor('gray')
        body.setBorderColor('darkgray')
        body.setBorderWidth(2)
        self.layer.add(body)
        
        # Head
        head = Circle(20, Point(-15, 0))
        head.setFillColor('gray')
        head.setBorderColor('darkgray')
        head.setBorderWidth(2)
        self.layer.add(head)
        
        # Ears
        left_ear = Ellipse(18, 25, Point(-25, -5))
        left_ear.setFillColor('darkgray')
        self.layer.add(left_ear)
        
        right_ear = Ellipse(18, 25, Point(-5, -5))
        right_ear.setFillColor('darkgray')
        self.layer.add(right_ear)
        
        # Trunk
        trunk = Path(Point(-15, 10), Point(-18, 25), Point(-15, 40))
        trunk.setBorderColor('gray')
        trunk.setBorderWidth(8)
        self.layer.add(trunk)
        
        # Legs
        self.legs = []
        leg_positions = [(-20, 45), (-10, 45), (10, 45), (20, 45)]
        for pos in leg_positions:
            leg = Rectangle(8, 25, Point(pos[0], pos[1]))
            leg.setFillColor('darkgray')
            self.layer.add(leg)
            self.legs.append(leg)
        
        # Tail
        tail = Path(Point(30, 20), Point(40, 30))
        tail.setBorderColor('darkgray')
        tail.setBorderWidth(3)
        self.layer.add(tail)
        
        self.leg_angle = 0
    
    def walk(self):
        """Animate walking"""
        self.leg_angle += 15
        offset = math.sin(math.radians(self.leg_angle)) * 2
        
        self.legs[0].move(0, offset)
        self.legs[2].move(0, offset)
        self.legs[1].move(0, -offset)
        self.legs[3].move(0, -offset)

# ==================== STEP 5: RABBIT CLASS ====================
class Rabbit(Animal):
    """Hopping rabbit"""
    def __init__(self, x, y):
        super().__init__(x, y)
        
        # Body
        body = Ellipse(20, 25, Point(0, 0))
        body.setFillColor('white')
        body.setBorderColor('lightgray')
        body.setBorderWidth(2)
        self.layer.add(body)
        
        # Head
        head = Circle(10, Point(0, -15))
        head.setFillColor('white')
        head.setBorderColor('lightgray')
        head.setBorderWidth(2)
        self.layer.add(head)
        
        # Ears
        left_ear = Ellipse(4, 15, Point(-6, -25))
        left_ear.setFillColor('pink')
        self.layer.add(left_ear)
        right_ear = Ellipse(4, 15, Point(6, -25))
        right_ear.setFillColor('pink')
        self.layer.add(right_ear)
        
        # Tail
        tail = Circle(4, Point(0, 12))
        tail.setFillColor('white')
        self.layer.add(tail)
        
        self.hop_phase = 0
        self.original_y = y
    
    def hop(self):
        """Hopping animation"""
        self.hop_phase += 40
        hop_height = abs(math.sin(math.radians(self.hop_phase))) * 8
        # Reset to original position then apply hop
        current_y = self.original_y - hop_height
        self.layer.moveTo(self.x, current_y)

# ==================== STEP 6: NOAH CLASS ====================
class Noah:
    """Noah welcoming animals"""
    def __init__(self, x, y):
        self.layer = Layer()
        self.x = x
        self.y = y
        
        # Body (robe)
        body = Rectangle(30, 50, Point(0, 20))
        body.setFillColor('brown')
        body.setBorderColor('saddlebrown')
        body.setBorderWidth(2)
        self.layer.add(body)
        
        # Head
        head = Circle(10, Point(0, -10))
        head.setFillColor('peachpuff')
        head.setBorderColor('tan')
        head.setBorderWidth(2)
        self.layer.add(head)
        
        # Beard
        beard = Ellipse(12, 8, Point(0, 0))
        beard.setFillColor('white')
        self.layer.add(beard)
        
        # Arms
        self.left_arm = Rectangle(6, 25, Point(-18, 10))
        self.left_arm.setFillColor('brown')
        self.layer.add(self.left_arm)
        
        self.right_arm = Rectangle(6, 25, Point(18, 10))
        self.right_arm.setFillColor('brown')
        self.layer.add(self.right_arm)
        
        # Staff
        staff = Rectangle(4, 60, Point(-22, 20))
        staff.setFillColor('saddlebrown')
        self.layer.add(staff)
        
        self.layer.moveTo(x, y)
        self.wave_angle = 0
        self.right_arm_base_y = 10
    
    def wave(self):
        """Wave right arm"""
        self.wave_angle += 15
        wave = math.sin(math.radians(self.wave_angle)) * 8
        self.right_arm.moveTo(18, self.right_arm_base_y + wave)

# ==================== STEP 7: ARK CLASS ====================
class Ark:
    """Noah's Ark with opening door"""
    def __init__(self, x, y):
        self.layer = Layer()
        self.x = x
        self.y = y
        
        # Hull
        hull = Rectangle(200, 80, Point(0, 0))
        hull.setFillColor('sienna')
        hull.setBorderColor('saddlebrown')
        hull.setBorderWidth(3)
        self.layer.add(hull)
        
        # Roof
        roof = Polygon(Point(-100, -40), Point(0, -70), Point(100, -40), Point(100, 0), Point(-100, 0))
        roof.setFillColor('saddlebrown')
        roof.setBorderColor('black')
        roof.setBorderWidth(2)
        self.layer.add(roof)
        
        # Door
        self.door = Rectangle(40, 60, Point(-60, 20))
        self.door.setFillColor('peru')
        self.door.setBorderColor('black')
        self.door.setBorderWidth(2)
        self.layer.add(self.door)
        self.door_open = False
        self.door_original_x = -60
        
        # Windows
        for i in range(3):
            window = Square(15, Point(-20 + i*30, -30))
            window.setFillColor('lightblue')
            window.setBorderColor('black')
            self.layer.add(window)
        
        # Ramp
        ramp = Polygon(Point(-80, 40), Point(-150, 100), Point(-140, 100), Point(-80, 45))
        ramp.setFillColor('peru')
        ramp.setBorderColor('saddlebrown')
        self.layer.add(ramp)
        
        self.layer.moveTo(x, y)
        self.rock_angle = 0
    
    def openDoor(self):
        """Open door"""
        if not self.door_open:
            self.door.moveTo(-95, 20)
            self.door_open = True
    
    def closeDoor(self):
        """Close door"""
        if self.door_open:
            self.door.moveTo(self.door_original_x, 20)
            self.door_open = False
    
    def rock(self):
        """Rocking motion"""
        self.rock_angle += 5
        rock = math.sin(math.radians(self.rock_angle)) * 2
        self.layer.move(0, rock)

# ==================== STEP 8: WATER & RAINBOW ====================
class Water:
    """Animated water"""
    def __init__(self):
        self.layer = Layer()
        
        # Water surface
        water_rect = Rectangle(800, 300, Point(400, 500))
        water_rect.setFillColor('steelblue')
        water_rect.setBorderWidth(0)
        self.layer.add(water_rect)
        
        # Waves
        self.waves = []
        for i in range(5):
            wave = Ellipse(100, 20, Point(i * 180 + 50, 350))
            wave.setFillColor('lightskyblue')
            wave.setBorderWidth(0)
            self.layer.add(wave)
            self.waves.append(wave)
        
        self.wave_offset = 0
    
    def animate(self):
        """Animate waves"""
        self.wave_offset += 5
        for i, wave in enumerate(self.waves):
            offset = math.sin(math.radians(self.wave_offset + i * 40)) * 5
            wave.move(0, offset)

class Rainbow:
    """Rainbow"""
    def __init__(self, x, y):
        self.layer = Layer()
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
        
        for i, color in enumerate(colors):
            arc = Circle(200 - i*15, Point(0, 0))
            arc.setFillColor('lightblue')
            arc.setBorderColor(color)
            arc.setBorderWidth(10)
            self.layer.add(arc)
        
        self.layer.moveTo(x, y)

class Sun:
    """Sun"""
    def __init__(self, x, y):
        self.layer = Layer()
        
        sun = Circle(40, Point(0, 0))
        sun.setFillColor('yellow')
        sun.setBorderColor('gold')
        sun.setBorderWidth(2)
        self.layer.add(sun)
        
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            x1 = math.cos(rad) * 45
            y1 = math.sin(rad) * 45
            x2 = math.cos(rad) * 65
            y2 = math.sin(rad) * 65
            ray = Path(Point(x1, y1), Point(x2, y2))
            ray.setBorderColor('gold')
            ray.setBorderWidth(4)
            self.layer.add(ray)
        
        self.layer.moveTo(x, y)

# ==================== STEP 9: SETUP SCENE ====================
print("Setting up Noah's Ark scene...")

# Background
sun = Sun(650, 100)
canvas.add(sun.layer)

water = Water()
canvas.add(water.layer)

ark = Ark(500, 320)
canvas.add(ark.layer)

# Noah will appear at the end, not at the beginning
noah = Noah(50, 340)  # Start off screen

rainbow = Rainbow(400, 150)

# Create animals - they will be added to canvas when it's their turn
giraffe1 = Giraffe(50, 450)
giraffe2 = Giraffe(20, 480)
bird1 = Bird(100, 200)
bird2 = Bird(130, 220)
elephant1 = Elephant(150, 500)
elephant2 = Elephant(120, 530)
rabbit1 = Rabbit(250, 520)
rabbit2 = Rabbit(280, 525)

# DON'T add animals to canvas yet - they'll appear when it's their turn

print("Scene ready! Starting animation...")

# ==================== STEP 10: FULL SEQUENTIAL ANIMATION ====================
# Opening message
title = Text("Noah's Ark", 36, Point(400, 100))
title.setFontColor('navy')
canvas.add(title)

verse = Text('"Two by two they came to Noah" - Genesis 7:9', 16, Point(400, 150))
verse.setFontColor('darkslateblue')
canvas.add(verse)

time.sleep(3)
canvas.remove(title)
canvas.remove(verse)

print("Animation starting...")

# ==================== PHASE 1: GIRAFFES ====================
print("Phase 1: Giraffes approaching...")

# ADD giraffes to canvas now (they appear)
canvas.add(giraffe1.layer)
canvas.add(giraffe2.layer)

# Show message
msg = Text("The giraffes arrive with graceful steps...", 20, Point(400, 50))
msg.setFontColor('goldenrod')
msg.setDepth(0)
canvas.add(msg)
time.sleep(2)
canvas.remove(msg)

# Giraffes walk to ark
while giraffe1.x < 380 or giraffe2.x < 350:
    if giraffe1.x < 380:
        giraffe1.move(1.5, 0)
        giraffe1.walk()
    
    if giraffe2.x < 350:
        giraffe2.move(1.5, 0)
        giraffe2.walk()
    
    time.sleep(0.03)

# Giraffes enter ark
print("Giraffes entering ark...")
msg = Text('"Come in, blessed creatures!" - Noah', 20, Point(400, 50))
msg.setFontColor('darkgreen')
canvas.add(msg)
time.sleep(1.5)
canvas.remove(msg)

ark.openDoor()
time.sleep(0.5)

# Move giraffes inside
for i in range(30):
    giraffe1.move(3, 0)
    giraffe2.move(3, 0)
    time.sleep(0.03)

# Remove giraffes (they're inside now)
canvas.remove(giraffe1.layer)
canvas.remove(giraffe2.layer)
ark.closeDoor()
time.sleep(1)

print("Giraffes safely inside!")

# ==================== PHASE 2: ELEPHANTS ====================
print("Phase 2: Elephants approaching...")

# ADD elephants to canvas now (they appear)
canvas.add(elephant1.layer)
canvas.add(elephant2.layer)

msg = Text("The elephants march forward with wisdom...", 20, Point(400, 50))
msg.setFontColor('gray')
canvas.add(msg)
time.sleep(2)
canvas.remove(msg)

# Elephants walk to ark
while elephant1.x < 400 or elephant2.x < 370:
    if elephant1.x < 400:
        elephant1.move(1.2, 0)
        elephant1.walk()
    
    if elephant2.x < 370:
        elephant2.move(1.2, 0)
        elephant2.walk()
    
    time.sleep(0.03)

# Elephants enter ark
print("Elephants entering ark...")
msg = Text('"Enter and find safety!" - Noah', 20, Point(400, 50))
msg.setFontColor('navy')
canvas.add(msg)
time.sleep(1.5)
canvas.remove(msg)

ark.openDoor()
time.sleep(0.5)

# Move elephants inside
for i in range(30):
    elephant1.move(3, 0)
    elephant2.move(3, 0)
    time.sleep(0.03)

# Remove elephants
canvas.remove(elephant1.layer)
canvas.remove(elephant2.layer)
ark.closeDoor()
time.sleep(1)

print("Elephants safely inside!")

# ==================== PHASE 3: RABBITS ====================
print("Phase 3: Rabbits approaching...")

# ADD rabbits to canvas now (they appear)
canvas.add(rabbit1.layer)
canvas.add(rabbit2.layer)

msg = Text("Joyful rabbits hop with excitement!", 20, Point(400, 50))
msg.setFontColor('darkgreen')
canvas.add(msg)
time.sleep(2)
canvas.remove(msg)

# Rabbits hop to ark
hop_counter = 0
while rabbit1.x < 410 or rabbit2.x < 380:
    if rabbit1.x < 410:
        rabbit1.move(2, 0)
        if hop_counter % 15 < 8:
            rabbit1.hop()
    
    if rabbit2.x < 380:
        rabbit2.move(2, 0)
        if hop_counter % 15 < 8:
            rabbit2.hop()
    
    hop_counter += 1
    time.sleep(0.03)

# Rabbits enter ark
print("Rabbits entering ark...")
msg = Text('"Quick little ones, hop inside!" - Noah', 20, Point(400, 50))
msg.setFontColor('purple')
canvas.add(msg)
time.sleep(1.5)
canvas.remove(msg)

ark.openDoor()
time.sleep(0.5)

# Move rabbits inside
for i in range(30):
    rabbit1.move(3, 0)
    rabbit2.move(3, 0)
    time.sleep(0.03)

# Remove rabbits
canvas.remove(rabbit1.layer)
canvas.remove(rabbit2.layer)
ark.closeDoor()
time.sleep(1)

print("Rabbits safely inside!")

# ==================== PHASE 4: BIRDS ====================
print("Phase 4: Birds flying...")

# ADD birds to canvas now (they appear)
canvas.add(bird1.layer)
canvas.add(bird2.layer)

msg = Text("Doves circle above, singing songs of hope!", 20, Point(400, 50))
msg.setFontColor('steelblue')
canvas.add(msg)
time.sleep(2)
canvas.remove(msg)

# Birds fly in circles
for frame in range(100):
    angle = frame * 5
    bird1.moveTo(400 + math.cos(math.radians(angle)) * 120, 
                 250 + math.sin(math.radians(angle)) * 60)
    bird1.flapWings()
    
    bird2.moveTo(400 + math.cos(math.radians(angle + 180)) * 120,
                 250 + math.sin(math.radians(angle + 180)) * 60)
    bird2.flapWings()
    
    time.sleep(0.03)

# Birds enter through window
print("Birds entering through window...")
msg = Text('"The doves find their rest" - Birds enter', 20, Point(400, 50))
msg.setFontColor('skyblue')
canvas.add(msg)
time.sleep(1.5)
canvas.remove(msg)

# Move birds toward ark window
for i in range(40):
    bird1.move(3, 1.5)
    bird2.move(3, 1.5)
    bird1.flapWings()
    bird2.flapWings()
    time.sleep(0.03)

# Remove birds
canvas.remove(bird1.layer)
canvas.remove(bird2.layer)
time.sleep(1)

print("Birds safely inside!")

# ==================== PHASE 5: NOAH AND FAMILY ENTER LAST ====================
print("Phase 5: Noah and his family board the ark...")

# ADD Noah to canvas now (he appears)
canvas.add(noah.layer)

msg = Text('"Noah and his family enter last" - Genesis 7:7', 22, Point(400, 50))
msg.setFontColor('darkblue')
canvas.add(msg)
time.sleep(2)
canvas.remove(msg)

# Noah walks to the ark door
while noah.x < 420:
    noah.layer.move(2, 0)
    noah.x += 2
    noah.wave()
    time.sleep(0.03)

time.sleep(1)

# Door opens for Noah
ark.openDoor()
time.sleep(0.5)

msg = Text('"Go into the ark, you and your whole family" - Genesis 7:1', 20, Point(400, 50))
msg.setFontColor('purple')
canvas.add(msg)
time.sleep(2)
canvas.remove(msg)

# Noah enters ark
for i in range(25):
    noah.layer.move(3, 0)
    time.sleep(0.03)

canvas.remove(noah.layer)
time.sleep(0.5)
ark.closeDoor()

# Close door final time
#ark.closeDoor()
time.sleep(1)

print("Noah and family safely inside!")

# ==================== PHASE 6: ALL ABOARD - JOURNEY BEGINS ====================
print("All animals aboard! Journey begins...")

msg = Text('"The Lord will keep all safe" - Genesis 7:23', 22, Point(400, 300))
msg.setFontColor('darkblue')
canvas.add(msg)
time.sleep(3)
canvas.remove(msg)

# Noah was already removed earlier, so do NOT remove again

ark.closeDoor()
time.sleep(1)

# Rainbow appears
print("Rainbow appears!")
canvas.add(rainbow.layer)

msg = Text("🌈 God's Rainbow of Promise! 🌈", 28, Point(400, 100))
msg.setFontColor('darkviolet')
canvas.add(msg)
time.sleep(3)
canvas.remove(msg)

# Ark rocks on water
for i in range(80):
    ark.rock()
    water.animate()
    time.sleep(0.03)

# Final covenant message
msg1 = Text('"I have set my rainbow in the clouds,"', 18, Point(400, 520))
msg1.setFontColor('white')
canvas.add(msg1)

msg2 = Text('"and it will be the sign of the covenant" - Genesis 9:13', 18, Point(400, 545))
msg2.setFontColor('white')
canvas.add(msg2)

time.sleep(4)
canvas.remove(msg1)
canvas.remove(msg2)

# Closing
closing = Text("✨ A Story of Faith, Hope, and New Beginnings ✨", 24, Point(400, 300))
closing.setFontColor('navy')
canvas.add(closing)

time.sleep(3)

print("\n" + "="*60)
print("Animation Complete!")
print("All creatures are safe in Noah's Ark!")
print("The rainbow represents God's promise of hope!")
print("="*60)