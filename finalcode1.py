from cs1graphics import *
import math
import time

class OpeningAnimation:
    def __init__(self, canvas):
        """Initialize the opening animation with canvas."""
        self.canvas = canvas
        self.width = self.canvas.getWidth()
        self.height = self.canvas.getHeight()
        self.canvas.setBackgroundColor('black')

    def film_flicker(self):
        """Creates a black-white-black flicker effect like old film projectors."""
        # Create white rectangle for flicker
        flicker = Rectangle(self.width, self.height, Point(self.width // 2, self.height // 2))
        flicker.setFillColor('white')
        flicker.setBorderWidth(0)

        # Quick flickers
        for _ in range(3):
            self.canvas.add(flicker)
            time.sleep(0.05)
            self.canvas.remove(flicker)
            time.sleep(0.05)

    def scene1(self):
        """Scene 1: Noah's Ark Story with Description (0-20 seconds)."""
        # Change background to dark slate gray
        self.canvas.setBackgroundColor('darkslategray')

        # Create main title
        title = Text("The Noah's Ark Story", 18)
        title.setFontColor('white')
        title.setFontSize(58)
        title.moveTo(self.width // 2, 100)
        self.canvas.add(title)

        # Create Bible reference
        bible_ref = Text("Based on the Bible - Genesis 6-9", 18)
        bible_ref.setFontColor('gold')
        bible_ref.setFontSize(24)
        bible_ref.moveTo(self.width // 2, 160)

        # Create description with line breaks
        desc_lines = [
            "God, seeing humanity's wickedness, chose the righteous Noah",
            "to build a huge ark to survive a global flood,",
            "saving his family and pairs of every animal",
            "to repopulate the Earth."
        ]

        description_texts = []
        y_start = 240
        for i, line in enumerate(desc_lines):
            desc = Text(line, 18)
            desc.setFontColor('lightblue')
            desc.setFontSize(26)
            desc.moveTo(self.width // 2, y_start + (i * 50))
            description_texts.append(desc)

        # Fade in title by adjusting depth
        time.sleep(0.5)

        # Add Bible reference with delay
        time.sleep(0.5)
        self.canvas.add(bible_ref)
        time.sleep(0.5)

        # Add description line by line
        for desc in description_texts:
            self.canvas.add(desc)
            time.sleep(0.5)

        # Hold the complete scene
        time.sleep(3)

        # Remove all elements
        self.canvas.remove(title)
        self.canvas.remove(bible_ref)
        for desc in description_texts:
            self.canvas.remove(desc)

        # Keep dark slate gray background for scene 2
        time.sleep(0.3)

    def scene2(self):
        """Scene 2: Created by Team (20-35 seconds)."""
        # Background is already dark slate gray from scene 1

        # Create "A Produced by" text
        created = Text("Produced by", 18)
        created.setFontColor('lightgray')
        created.setFontSize(32)
        created.moveTo(self.width // 2, 80)
        self.canvas.add(created)

        # Add decorative lines
        line1 = Path(Point(250, 120), Point(450, 120))
        line1.setBorderColor('gold')
        line1.setBorderWidth(3)
        self.canvas.add(line1)

        line2 = Path(Point(550, 120), Point(750, 120))
        line2.setBorderColor('gold')
        line2.setBorderWidth(3)
        self.canvas.add(line2)

        time.sleep(0.8)

        # Create team members information
        team_members = [
            "22457001 - Nadhiar Ridho Wahyu Pradana",
            "22457002 - Devy Puspitasari",
            "22547008 - Jerome Mwandoki Mwamunzoyo"
        ]

        member_objects = []
        y_positions = [200, 300, 400]

        # Add each member with animation
        for i, (member, y_pos) in enumerate(zip(team_members, y_positions)):
            # Create background rectangle
            bg_rect = Rectangle(700, 70, Point(self.width // 2, y_pos))
            bg_rect.setFillColor('darkblue')
            bg_rect.setBorderColor('cyan')
            bg_rect.setBorderWidth(2)
            self.canvas.add(bg_rect)

            # Create member text
            member_text = Text(member, 18)
            member_text.setFontColor('white')
            member_text.setFontSize(28)
            member_text.moveTo(self.width // 2, y_pos)
            self.canvas.add(member_text)

            member_objects.append((bg_rect, member_text))
            time.sleep(0.7)

        # Hold the scene
        time.sleep(3.5)

        # Remove all elements
        self.canvas.remove(created)
        self.canvas.remove(line1)
        self.canvas.remove(line2)
        for bg_rect, member_text in member_objects:
            self.canvas.remove(bg_rect)
            self.canvas.remove(member_text)

        # Change background back to black for scene 3
        self.canvas.setBackgroundColor('black')
        time.sleep(0.3)

    def scene3_enjoy(self):
        """Scene 3: Enjoy the video (35-55 seconds)."""
        # Create main message (no circle behind)
        enjoy = Text("Enjoy the Video", 18)
        enjoy.setFontColor('white')
        enjoy.setFontSize(64)
        enjoy.moveTo(self.width // 2, self.height // 2)
        self.canvas.add(enjoy)

        time.sleep(0.8)

        # Add sparkle stars in corners - far from the text
        stars = []
        star_positions = [
            (150, 120), (850, 120),  # Top corners
            (150, 480), (850, 480),  # Bottom corners
            (100, 300), (900, 300),  # Far left and right
            (250, 180), (750, 180),  # Upper sides
            (250, 420), (750, 420)  # Lower sides
        ]

        for pos in star_positions:
            star = Text("✨", 18)
            star.setFontColor('yellow')
            star.setFontSize(40)
            star.moveTo(pos[0], pos[1])
            self.canvas.add(star)
            stars.append(star)
            time.sleep(0.15)

        # Pulse effect with color changes
        for _ in range(6):
            enjoy.setFontSize(70)
            for star in stars:
                star.setFontColor('gold')
            time.sleep(0.35)

            enjoy.setFontSize(64)
            for star in stars:
                star.setFontColor('yellow')
            time.sleep(0.35)

        # Hold final screen
        time.sleep(3)

        # Remove all elements
        self.canvas.remove(enjoy)
        for star in stars:
            self.canvas.remove(star)
        time.sleep(0.3)

    def scene4_countdown(self):
        """Scene 4: Film Countdown (55-60 seconds)."""
        # Countdown numbers
        for count in [3, 2, 1]:
            # Create outer circle (film reel)
            outer_circle = Circle(200, Point(self.width // 2, self.height // 2))
            outer_circle.setFillColor('white')
            outer_circle.setBorderColor('black')
            outer_circle.setBorderWidth(8)
            self.canvas.add(outer_circle)

            # Create inner circle
            inner_circle = Circle(150, Point(self.width // 2, self.height // 2))
            inner_circle.setFillColor('black')
            inner_circle.setBorderWidth(0)
            self.canvas.add(inner_circle)

            # Create countdown number
            number = Text(str(count), 18)
            number.setFontColor('white')
            number.setFontSize(120)
            number.moveTo(self.width // 2, self.height // 2)
            self.canvas.add(number)

            # Create corner markers (film frame corners)
            corner_size = 30
            corners = []
            corner_positions = [
                (350, 150), (650, 150),  # Top corners
                (350, 450), (650, 450)  # Bottom corners
            ]

            for x, y in corner_positions:
                corner = Rectangle(corner_size, corner_size, Point(x, y))
                corner.setFillColor('white')
                corner.setBorderWidth(0)
                self.canvas.add(corner)
                corners.append(corner)

            # Add film scratches (vertical lines)
            scratch1 = Path(Point(200, 100), Point(200, 500))
            scratch1.setBorderColor('gray')
            scratch1.setBorderWidth(2)
            self.canvas.add(scratch1)

            scratch2 = Path(Point(800, 100), Point(800, 500))
            scratch2.setBorderColor('gray')
            scratch2.setBorderWidth(2)
            self.canvas.add(scratch2)

            # Hold for 1 second
            time.sleep(1)

            # Remove all countdown elements
            self.canvas.remove(outer_circle)
            self.canvas.remove(inner_circle)
            self.canvas.remove(number)
            for corner in corners:
                self.canvas.remove(corner)
            self.canvas.remove(scratch1)
            self.canvas.remove(scratch2)

            # Brief black screen
            time.sleep(0.2)

        # Final flicker before video starts
        self.film_flicker()

    def run(self):
        """Main animation sequence."""
        print("=" * 60)
        print("NOAH'S ARK STORY - OPENING ANIMATION")
        print("=" * 60)
        print("Duration: ~60 seconds")
        print("Scenes:")
        print("  1. The Noah's Ark Story (0-20s)")
        print("  2. Created by Team (20-35s)")
        print("  3. Enjoy the Video (35-55s)")
        print("  4. Film Countdown 3-2-1 (55-60s)")
        print("=" * 60)
        print("\nStarting animation...\n")

        # Run all scenes with film flicker transitions
        self.scene1()  # Noah's Ark Story with description
        self.film_flicker()  # Transition effect

        self.scene2()  # Created by team members
        self.film_flicker()  # Transition effect

        self.scene3_enjoy()  # Enjoy the video (no circle, stars in corners)

        self.scene4_countdown()  # Film countdown 3-2-1

        print("\n" + "=" * 60)
        print("Animation complete! The video is starting now...")
        print("=" * 60)


class ClosingAnimation:
    def __init__(self, canvas):
        """Initialize the closing animation with canvas."""
        self.canvas = canvas
        self.width = self.canvas.getWidth()
        self.height = self.canvas.getHeight()
        self.canvas.setBackgroundColor('black')

    def film_flicker(self):
        """Creates a black-white-black flicker effect like old film projectors."""
        # Create white rectangle for flicker
        flicker = Rectangle(self.width, self.height, Point(self.width // 2, self.height // 2))
        flicker.setFillColor('white')
        flicker.setBorderWidth(0)

        # Quick flickers
        for _ in range(3):
            self.canvas.add(flicker)
            time.sleep(0.05)
            self.canvas.remove(flicker)
            time.sleep(0.05)

    def scene1_fade_in(self):
        """Gradual fade in from video."""
        # Just a pause to simulate video ending
        time.sleep(1)
        self.film_flicker()
        time.sleep(0.5)

    def scene2_film_end(self):
        """Classic film ending with THE END."""
        # Create "THE END" text
        the_end = Text("THE END", 18)
        the_end.setFontColor('white')
        the_end.setFontSize(80)
        the_end.moveTo(self.width // 2, self.height // 2)
        self.canvas.add(the_end)

        # Add film frame corners
        corner_size = 40
        corners = []
        corner_positions = [
            (150, 100), (850, 100),  # Top corners
            (150, 500), (850, 500)  # Bottom corners
        ]

        for x, y in corner_positions:
            corner = Rectangle(corner_size, corner_size, Point(x, y))
            corner.setFillColor('white')
            corner.setBorderWidth(0)
            self.canvas.add(corner)
            corners.append(corner)

        # Hold "THE END"
        time.sleep(3)

        # Final film flicker
        self.film_flicker()

        # Remove all
        self.canvas.remove(the_end)
        for corner in corners:
            self.canvas.remove(corner)

        time.sleep(0.5)

    def scene3_thank_you(self):
        """Thank you message with elegant animation - no borders, no circles."""
        # Main thank you message
        thank_you = Text("Thank You", 18)
        thank_you.setFontColor('white')
        thank_you.setFontSize(68)
        thank_you.moveTo(self.width // 2, 260)
        self.canvas.add(thank_you)

        time.sleep(0.8)

        # "for Watching" text
        for_watching = Text("for Watching", 18)
        for_watching.setFontColor('gold')
        for_watching.setFontSize(52)
        for_watching.moveTo(self.width // 2, 340)
        self.canvas.add(for_watching)

        time.sleep(1)

        # Add floating sparkles around the text
        stars = []
        star_positions = [
            (250, 200), (750, 200),  # Top sides
            (250, 400), (750, 400),  # Bottom sides
            (180, 300), (820, 300),  # Far sides
            (350, 180), (650, 180),  # Upper corners
            (350, 420), (650, 420)  # Lower corners
        ]

        for pos in star_positions:
            star = Text("✨", 18)
            star.setFontColor('yellow')
            star.setFontSize(32)
            star.moveTo(pos[0], pos[1])
            self.canvas.add(star)
            stars.append(star)
            time.sleep(0.12)

        # Animated pulse effect
        for _ in range(6):
            # Pulse up
            thank_you.setFontSize(72)
            for_watching.setFontSize(56)

            for star in stars[::2]:  # Alternate stars
                star.setFontColor('gold')

            time.sleep(0.4)

            # Pulse down
            thank_you.setFontSize(68)
            for_watching.setFontSize(52)

            for star in stars[::2]:
                star.setFontColor('yellow')

            time.sleep(0.4)

        # Hold the message
        time.sleep(2)

        # Fade out - remove all elements
        for star in stars:
            self.canvas.remove(star)
        self.canvas.remove(thank_you)
        self.canvas.remove(for_watching)

        time.sleep(0.5)

    def run(self):
        """Main closing animation sequence."""
        self.canvas.clear()
        self.canvas.setBackgroundColor('black')

        # Run all closing scenes
        self.scene1_fade_in()  # Transition from video
        self.scene2_film_end()  # The End
        self.film_flicker()  # Transition
        self.scene3_thank_you()  # Thank you for watching


class Tree(Layer):
    def __init__(self, position=(170, 600), trunk_width=30, trunk_height=250, leaves_size=(150, 100)):
        super().__init__()
        trunk = Rectangle(trunk_width, trunk_height, Point(position[0], position[1]))
        trunk.setFillColor('brown')
        trunk.setBorderWidth(0)
        trunk.setDepth(40)
        self.add(trunk)
        branch1 = Polygon(Point(position[0] + 10, position[1] - 10),
                          Point(position[0] + 10, position[1] - 50),
                          Point(position[0] + 110, position[1] - 120))
        branch1.setFillColor('brown')
        branch1.setBorderWidth(0)
        branch1.setDepth(44)
        self.add(branch1)
        branch2 = Polygon(Point(position[0] - 10, position[1] + 20),
                          Point(position[0] - 10, position[1] - 20),
                          Point(position[0] - 110, position[1] - 90))
        branch2.setFillColor('brown')
        branch2.setBorderWidth(0)
        branch2.setDepth(44)
        self.add(branch2)
        leaves = Ellipse(leaves_size[0], leaves_size[1], Point(position[0], position[1] - 230))
        leaves.setFillColor('darkGreen')
        leaves.setBorderWidth(0)
        leaves.setDepth(44)
        self.add(leaves)
        leaves1 = Circle(80, Point(position[0], position[1] - 175))
        leaves1.setFillColor('darkGreen')
        leaves1.setBorderWidth(0)
        leaves1.setDepth(44)
        self.add(leaves1)
        self.setDepth(40)


def add_sun_rays(center_x, center_y, radius, num_rays=8, ray_length=30, color="orange"):
    rays = []
    for i in range(num_rays):
        angle_deg = i * 360 / num_rays
        angle_rad = math.radians(angle_deg)
        x_start = center_x + radius * math.cos(angle_rad)
        y_start = center_y - radius * math.sin(angle_rad)
        x_end = center_x + (radius + ray_length) * math.cos(angle_rad)
        y_end = center_y - (radius + ray_length) * math.sin(angle_rad)
        ray = Path([Point(x_start, y_start), Point(x_end, y_end)])
        ray.setBorderColor(color)
        ray.setBorderWidth(3)
        ray.setDepth(38)
        rays.append(ray)
    return rays


class Mountain(Polygon):
    def __init__(self, base_width, height, position, color="brown"):
        points = [
            Point(position[0] - base_width // 2, position[1] + height),
            Point(position[0], position[1]),
            Point(position[0] + base_width // 2, position[1] + height)
        ]
        super().__init__(*points)
        self.setFillColor(color)
        self.setBorderColor("black")
        self.setDepth(45)


class Goat(Layer):
    def __init__(self, color="white", x=0, y=0):
        super().__init__()
        body = Ellipse(60, 30, Point(0, 0))
        body.setFillColor(color)
        body.setBorderColor("black")
        body.setDepth(42)
        self.add(body)
        head = Circle(15, Point(-30, -10))
        head.setFillColor(color)
        head.setBorderColor("black")
        head.setDepth(41)
        self.add(head)
        horn1 = Polygon(Point(-35, -20), Point(-40, -30),
                        Point(-30, -30))
        horn1.setFillColor("gray")
        horn1.setBorderColor("black")
        horn1.setDepth(40)
        horn2 = Polygon(Point(-25, -20), Point(-30, -30),
                        Point(-20, -30))
        horn2.setFillColor("gray")
        horn2.setBorderColor("black")
        horn2.setDepth(40)
        self.add(horn1)
        self.add(horn2)
        ear1 = Ellipse(8, 15, Point(-35, -20))
        ear1.setFillColor(color)
        ear1.setBorderColor("black")
        ear1.setDepth(40)
        ear2 = Ellipse(8, 15, Point(-25, -20))
        ear2.setFillColor(color)
        ear2.setBorderColor("black")
        ear2.setDepth(40)
        self.add(ear1)
        self.add(ear2)
        eye = Circle(3, Point(-33, -12))
        eye.setFillColor("black")
        eye.setDepth(39)
        self.add(eye)
        leg1 = Rectangle(5, 20, Point(15, 20))
        leg1.setFillColor(color)
        leg1.setBorderColor("black")
        leg1.setDepth(43)
        leg2 = Rectangle(5, 20, Point(-15, 20))
        leg2.setFillColor(color)
        leg2.setBorderColor("black")
        leg2.setDepth(43)
        leg3 = Rectangle(5, 20, Point(5, 20))
        leg3.setFillColor(color)
        leg3.setBorderColor("black")
        leg3.setDepth(43)
        leg4 = Rectangle(5, 20, Point(-25, 20))
        leg4.setFillColor(color)
        leg4.setBorderColor("black")
        leg4.setDepth(43)
        self.add(leg1)
        self.add(leg2)
        self.add(leg3)
        self.add(leg4)
        tail = Path([Point(30, 0), Point(40, -10)])
        tail.setBorderColor("black")
        tail.setBorderWidth(2)
        tail.setDepth(43)
        self.add(tail)
        self.moveTo(x, y)


class Chicken(Layer):
    def __init__(self, color="yellow", x=0, y=0):
        super().__init__()
        body = Ellipse(40, 25, Point(0, 0))
        body.setFillColor(color)
        body.setBorderColor("black")
        body.setDepth(42)
        self.add(body)
        head = Circle(10, Point(-20, -8))
        head.setFillColor(color)
        head.setBorderColor("black")
        head.setDepth(41)
        self.add(head)
        beak = Polygon(Point(-28, -8), Point(-35, -5),
                       Point(-28, -2))
        beak.setFillColor("orange")
        beak.setBorderColor("orange")
        beak.setDepth(40)
        self.add(beak)
        eye = Circle(2, Point(-23, -10))
        eye.setFillColor("white")
        eye.setDepth(39)
        pupil = Circle(1, Point(-23, -10))
        pupil.setFillColor("black")
        pupil.setDepth(38)
        self.add(eye)
        self.add(pupil)
        leg1 = Rectangle(3, 15, Point(10, 15))
        leg1.setFillColor("orange")
        leg1.setBorderColor("orange")
        leg1.setDepth(43)
        leg2 = Rectangle(3, 15, Point(-10, 15))
        leg2.setFillColor("orange")
        leg2.setBorderColor("orange")
        leg2.setDepth(43)
        self.add(leg1)
        self.add(leg2)
        tail = Ellipse(20, 15, Point(20, 0))
        tail.setFillColor(color)
        tail.setBorderColor("black")
        tail.setDepth(43)
        self.add(tail)
        self.moveTo(x, y)


class Bird(Layer):
    def __init__(self, color="blue", x=0, y=0):
        super().__init__()
        body = Ellipse(30, 15, Point(0, 0))
        body.setFillColor(color)
        body.setBorderColor("black")
        self.add(body)
        head = Circle(8, Point(-15, -5))
        head.setFillColor(color)
        head.setBorderColor("black")
        self.add(head)
        beak = Polygon(Point(-20, -5), Point(-25, -3),
                       Point(-20, -1))
        beak.setFillColor("yellow")
        beak.setBorderColor("yellow")
        self.add(beak)
        eye = Circle(2, Point(-17, -6))
        eye.setFillColor("black")
        self.add(eye)
        wing1 = Polygon(Point(0, 0), Point(-10, -15),
                        Point(10, -15))
        wing1.setFillColor(color)
        wing1.setBorderColor("black")
        self.add(wing1)
        self.moveTo(x, y)


class Giraffe:
    def __init__(self, x, y):
        self.layer = Layer()
        self.x = x
        self.y = y
        self.layer.moveTo(x, y)
        self.step = 0
        self.legs = []
        self.head_layer = Layer()
        self.neck = None
        # Body
        body = Ellipse(90, 130, Point(0, 70))
        body.setFillColor("goldenrod")
        body.setBorderColor("black")
        body.setBorderWidth(3)
        self.layer.add(body)
        # Long Neck
        neck = Polygon(
            Point(-15, -90),  # top-left of neck
            Point(15, -90),  # top-right
            Point(30, 30),  # bottom-right of neck
            Point(-30, 30)  # bottom-left
        )
        neck.setFillColor("goldenrod")
        neck.setBorderColor("black")
        neck.setBorderWidth(3)
        self.layer.add(neck)
        self.neck = neck
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
        self.layer.add(self.head_layer)
        # Legs
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
        # Tail
        tail = Path(Point(-45, 80), Point(-55, 120))
        tail.setBorderColor("black")
        tail.setBorderWidth(4)
        self.layer.add(tail)
        tuft = Circle(7, Point(-55, 128))
        tuft.setFillColor("black")
        self.layer.add(tuft)
        # Spots
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

    def walk(self):
        self.step += 8
        move = math.sin(math.radians(self.step)) * 4
        self.legs[0].move(0, move)
        self.legs[2].move(0, move)
        self.legs[1].move(0, -move)
        self.legs[3].move(0, -move)

    def sway_neck(self):
        sway = math.sin(math.radians(self.step)) * 2
        self.neck.move(sway, 0)
        self.head_layer.move(sway, 0)


class Elephant:
    def __init__(self, x, y):
        self.layer = Layer()
        self.x = x
        self.y = y
        self.layer.moveTo(x, y)
        self.leg_angle = 0
        self.trunk_angle = 0
        self.tail = None
        self.trunk = None
        self.legs = []
        # Longer Body (flipped horizontally)
        body = Ellipse(200, 110, Point(10, 20))
        body.setFillColor("azure4")
        body.setBorderColor("black")
        body.setBorderWidth(4)
        self.layer.add(body)
        # Tail (flipped position)
        tail = Path(Point(105, 15), Point(125, 25), Point(115, 35))
        tail.setBorderColor("black")
        tail.setBorderWidth(6)
        self.layer.add(tail)
        self.tail = tail
        # Head + Tusk Fused Shape (flipped horizontally)
        head_tusk = Polygon(
            Point(-40, -40),
            Point(-75, -20),
            Point(-85, -5),
            Point(-110, 15),
            Point(-95, 25),
            Point(-80, 10),
            Point(-70, 25),
            Point(-50, 40),
            Point(-20, 20),
            Point(-25, -10)
        )
        head_tusk.setFillColor("azure4")
        head_tusk.setBorderColor("black")
        head_tusk.setBorderWidth(4)
        self.layer.add(head_tusk)
        # Eye (flipped position)
        eye = Circle(5, Point(-70, -10))
        eye.setFillColor("black")
        self.layer.add(eye)
        # Ear (flipped position)
        ear = Ellipse(70, 85, Point(-5, -5))
        ear.setFillColor("azure4")
        ear.setBorderColor("black")
        ear.setBorderWidth(4)
        self.layer.add(ear)
        # Trunk (flipped path)
        trunk = Path(Point(-80, 10), Point(-110, 40), Point(-90, 75))
        trunk.setBorderColor("black")
        trunk.setBorderWidth(10)
        self.layer.add(trunk)
        self.trunk = trunk
        # Legs (flipped positions)
        for dx in [60, 20, -30, -70]:
            leg = Ellipse(45, 55, Point(dx, 70))
            leg.setFillColor("azure4")
            leg.setBorderColor("black")
            leg.setBorderWidth(4)
            self.layer.add(leg)
            self.legs.append(leg)

    def walk(self):
        self.leg_angle += 15
        shift = math.sin(math.radians(self.leg_angle)) * 3
        for i, leg in enumerate(self.legs):
            leg.move(0, shift if i % 2 == 0 else -shift)
        self.tail.move(math.sin(math.radians(self.leg_angle)) * 0.8, 0)

    def swing_trunk(self):
        self.trunk_angle += 10
        sway = math.sin(math.radians(self.trunk_angle)) * 3
        self.trunk.move(sway, 0)


class Rabbit:
    def __init__(self, x, y):
        self.layer = Layer()
        self.x = x
        self.y = y
        self.layer.moveTo(x, y)
        self.hop_phase = 0
        self.ground_y = y
        self.back_legs = []
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
        for dx in (-8, 8):
            leg = Ellipse(6, 10, Point(dx, 12))
            leg.setFillColor("white")
            self.layer.add(leg)
            self.back_legs.append(leg)
        tail = Circle(4, Point(0, 12))
        tail.setFillColor("white")
        self.layer.add(tail)

    def move_to(self, x, y):
        dx = x - self.x
        dy = y - self.y
        self.layer.move(dx, dy)
        self.x = x
        self.y = y

    def hop(self):
        self.hop_phase += 25
        hop_height = abs(math.sin(math.radians(self.hop_phase))) * 10
        self.move_to(self.x, self.ground_y - hop_height)


class Noah(Layer):
    def __init__(self):
        super().__init__()
        skin = Color("peachpuff")
        robe = Color("firebrick")
        head_color = Color("peru")
        beard_color = Color("lightgrey")
        outline = Color("saddlebrown")
        staff_color = Color("chocolate")
        head = Circle(70)
        head.setFillColor(head_color)
        head.setBorderColor(outline)
        head.moveTo(0, -200)
        self.add(head)
        hair1 = Circle(17)
        hair1.setFillColor("lightgrey")
        hair1.setBorderWidth(0)
        hair1.moveTo(-40, -265)
        self.add(hair1)
        hair2 = Circle(17)
        hair2.setFillColor("lightgrey")
        hair2.setBorderWidth(0)
        hair2.moveTo(-15, -280)
        self.add(hair2)
        hair3 = Circle(17)
        hair3.setFillColor("lightgrey")
        hair3.setBorderWidth(0)
        hair3.moveTo(15, -280)
        self.add(hair3)
        hair4 = Circle(17)
        hair4.setFillColor("lightgrey")
        hair4.setBorderWidth(0)
        hair4.moveTo(40, -265)
        self.add(hair4)
        hair5 = Circle(17)
        hair5.setFillColor("lightgrey")
        hair5.setBorderWidth(0)
        hair5.moveTo(65, -250)
        self.add(hair5)
        hair6 = Circle(17)
        hair6.setFillColor("lightgrey")
        hair6.setBorderWidth(0)
        hair6.moveTo(70, -225)
        self.add(hair6)
        hair7 = Circle(17)
        hair7.setFillColor("lightgrey")
        hair7.setBorderWidth(0)
        hair7.moveTo(70, -195)
        self.add(hair7)
        hair8 = Circle(17)
        hair8.setFillColor("lightgrey")
        hair8.setBorderWidth(0)
        hair8.moveTo(60, -165)
        self.add(hair8)
        hair9 = Circle(17)
        hair9.setFillColor("lightgrey")
        hair9.setBorderWidth(0)
        hair9.moveTo(50, -140)
        self.add(hair9)
        hair100 = Circle(17)
        hair100.setFillColor("lightgrey")
        hair100.setBorderWidth(0)
        hair100.moveTo(60, -130)
        self.add(hair100)
        hair10 = Circle(17)
        hair10.setFillColor("lightgrey")
        hair10.setBorderWidth(0)
        hair10.moveTo(-65, -250)
        self.add(hair10)
        hair11 = Circle(17)
        hair11.setFillColor("lightgrey")
        hair11.setBorderWidth(0)
        hair11.moveTo(-70, -225)
        self.add(hair11)
        hair12 = Circle(17)
        hair12.setFillColor("lightgrey")
        hair12.setBorderWidth(0)
        hair12.moveTo(-70, -195)
        self.add(hair12)
        hair13 = Circle(17)
        hair13.setFillColor("lightgrey")
        hair13.setBorderWidth(0)
        hair13.moveTo(-60, -165)
        self.add(hair13)
        hair14 = Circle(17)
        hair14.setFillColor("lightgrey")
        hair14.setBorderWidth(0)
        hair14.moveTo(-50, -140)
        self.add(hair14)
        hair101 = Circle(17)
        hair101.setFillColor("lightgrey")
        hair101.setBorderWidth(0)
        hair101.moveTo(-70, -130)
        self.add(hair101)
        eye1 = Circle(10)
        eye1.setFillColor("black")
        eye1.moveTo(-30, -210)
        self.add(eye1)
        eye2 = Circle(10)
        eye2.setFillColor("black")
        eye2.moveTo(30, -210)
        self.add(eye2)
        nose = Polygon(Point(0, -195), Point(-10, -175), Point(10, -175))
        nose.setFillColor(skin)
        nose.setBorderColor(skin)
        self.add(nose)
        beard = Polygon(Point(-50, -150), Point(50, -150), Point(25, -115), Point(-25, -115))
        beard.setFillColor(beard_color)
        beard.setBorderColor(beard_color)
        self.add(beard)
        body = Rectangle(160, 280)
        body.setFillColor(robe)
        body.setBorderColor(robe)
        body.moveTo(0, 30)
        self.add(body)
        left_arm = Rectangle(35, 110)
        left_arm.setFillColor(skin)
        left_arm.setBorderColor(outline)
        left_arm.moveTo(-90, -50)
        self.add(left_arm)
        right_arm = Rectangle(35, 110)
        right_arm.setFillColor(skin)
        right_arm.setBorderColor(outline)
        right_arm.moveTo(90, -50)
        self.add(right_arm)
        staff = Rectangle(20, 320)
        staff.setFillColor(staff_color)
        staff.setBorderColor(staff_color)
        staff.moveTo(-125, 10)
        self.add(staff)
        left_hand = Ellipse(45, 30)
        left_hand.setFillColor(skin)
        left_hand.setBorderColor(outline)
        left_hand.moveTo(-125, 5)
        self.add(left_hand)
        right_hand = Ellipse(45, 30)
        right_hand.setFillColor(skin)
        right_hand.setBorderColor(outline)
        right_hand.moveTo(90, 5)
        self.add(right_hand)
        left_foot = Ellipse(60, 30)
        left_foot.setFillColor(skin)
        left_foot.setBorderColor(outline)
        left_foot.moveTo(-40, 180)
        self.add(left_foot)
        right_foot = Ellipse(60, 30)
        right_foot.setFillColor(skin)
        right_foot.setBorderColor(outline)
        right_foot.moveTo(40, 180)
        self.add(right_foot)


class Wife(Layer):
    def __init__(self):
        super().__init__()
        skin = Color("peachpuff")
        robe_color = Color("plum")
        outline = Color("saddlebrown")
        hair_color = Color("lightgrey")
        head = Circle(65)
        head.setFillColor(skin)
        head.setBorderColor(outline)
        head.moveTo(0, -190)
        self.add(head)
        ht1 = Circle(20)
        ht1.setFillColor(hair_color)
        ht1.setBorderWidth(0)
        ht1.moveTo(-20, -270)
        self.add(ht1)
        ht2 = Circle(22)
        ht2.setFillColor(hair_color)
        ht2.setBorderWidth(0)
        ht2.moveTo(0, -270)
        self.add(ht2)
        ht3 = Circle(20)
        ht3.setFillColor(hair_color)
        ht3.setBorderWidth(0)
        ht3.moveTo(20, -270)
        self.add(ht3)
        ht4 = Circle(18)
        ht4.setFillColor(hair_color)
        ht4.setBorderWidth(0)
        ht4.moveTo(-40, -250)
        self.add(ht4)
        ht5 = Circle(18)
        ht5.setFillColor(hair_color)
        ht5.setBorderWidth(0)
        ht5.moveTo(40, -250)
        self.add(ht5)
        hl1 = Circle(20)
        hl1.setFillColor(hair_color)
        hl1.setBorderWidth(0)
        hl1.moveTo(-60, -220)
        self.add(hl1)
        hl2 = Circle(20)
        hl2.setFillColor(hair_color)
        hl2.setBorderWidth(0)
        hl2.moveTo(-65, -185)
        self.add(hl2)
        hl3 = Circle(20)
        hl3.setFillColor(hair_color)
        hl3.setBorderWidth(0)
        hl3.moveTo(-60, -150)
        self.add(hl3)
        hl4 = Circle(20)
        hl4.setFillColor(hair_color)
        hl4.setBorderWidth(0)
        hl4.moveTo(-50, -115)
        self.add(hl4)
        hr1 = Circle(20)
        hr1.setFillColor(hair_color)
        hr1.setBorderWidth(0)
        hr1.moveTo(60, -220)
        self.add(hr1)
        hr2 = Circle(20)
        hr2.setFillColor(hair_color)
        hr2.setBorderWidth(0)
        hr2.moveTo(65, -185)
        self.add(hr2)
        hr3 = Circle(20)
        hr3.setFillColor(hair_color)
        hr3.setBorderWidth(0)
        hr3.moveTo(60, -150)
        self.add(hr3)
        hr4 = Circle(20)
        hr4.setFillColor(hair_color)
        hr4.setBorderWidth(0)
        hr4.moveTo(50, -115)
        self.add(hr4)
        eyeL = Circle(10)
        eyeL.setFillColor("black")
        eyeL.moveTo(-20, -195)
        self.add(eyeL)
        eyeR = Circle(10)
        eyeR.setFillColor("black")
        eyeR.moveTo(20, -195)
        self.add(eyeR)
        nose = Polygon(Point(0, -185), Point(-8, -170), Point(8, -170))
        nose.setFillColor(skin)
        nose.setBorderColor(skin)
        self.add(nose)
        mouth = Polygon(Point(-12, -155), Point(12, -155), Point(0, -145))
        mouth.setFillColor("lightcoral")
        mouth.setBorderColor("lightcoral")
        self.add(mouth)
        body = Rectangle(170, 260)
        body.setFillColor(robe_color)
        body.setBorderColor(robe_color)
        body.moveTo(0, 30)
        self.add(body)
        armL = Rectangle(35, 110)
        armL.setFillColor(skin)
        armL.setBorderColor(outline)
        armL.moveTo(-85, -80)
        self.add(armL)
        armR = Rectangle(35, 110)
        armR.setFillColor(skin)
        armR.setBorderColor(outline)
        armR.moveTo(85, -80)
        self.add(armR)
        handL = Ellipse(45, 30)
        handL.setFillColor(skin)
        handL.setBorderColor(outline)
        handL.moveTo(-85, -20)
        self.add(handL)
        handR = Ellipse(45, 30)
        handR.setFillColor(skin)
        handR.setBorderColor(outline)
        handR.moveTo(85, -20)
        self.add(handR)
        footL = Ellipse(60, 30)
        footL.setFillColor(skin)
        footL.setBorderColor(outline)
        footL.moveTo(-35, 180)
        self.add(footL)
        footR = Ellipse(60, 30)
        footR.setFillColor(skin)
        footR.setBorderColor(outline)
        footR.moveTo(35, 180)
        self.add(footR)


class Kid(Layer):
    def __init__(self):
        super().__init__()
        skin = Color("peachpuff")
        hair_color = Color("sienna")
        tunic_color = Color("peru")
        sash_color = Color("saddlebrown")
        outline = Color("sienna")
        head = Circle(55)
        head.setFillColor(skin)
        head.setBorderColor(outline)
        head.moveTo(0, -190)
        self.add(head)
        hair_positions = [
            (-40, -220), (-20, -232), (0, -237), (20, -232), (40, -220),
            (-45, -195), (45, -195)
        ]
        for (dx, dy) in hair_positions:
            h = Circle(15)
            h.setFillColor(hair_color)
            h.setBorderWidth(0)
            h.moveTo(dx, dy)
            self.add(h)
        eye1 = Circle(10)
        eye1.setFillColor("black")
        eye1.moveTo(-15, -195)
        self.add(eye1)
        eye2 = Circle(10)
        eye2.setFillColor("black")
        eye2.moveTo(15, -195)
        self.add(eye2)
        smile = Polygon(
            Point(0, -165),
            Point(-20, -180),
            Point(20, -180)
        )
        smile.setFillColor("lightcoral")
        smile.setBorderColor("lightcoral")
        self.add(smile)
        tunic = Rectangle(130, 180)
        tunic.setFillColor(tunic_color)
        tunic.setBorderColor(outline)
        tunic.moveTo(0, -50)
        self.add(tunic)
        sash = Rectangle(160, 40)
        sash.setFillColor(sash_color)
        sash.setBorderColor(sash_color)
        sash.moveTo(0, -85)
        self.add(sash)
        wrap = Polygon(
            Point(-50, -40),
            Point(50, -40),
            Point(40, 30),
            Point(-40, 30)
        )
        wrap.setFillColor(tunic_color)
        wrap.setBorderColor(outline)
        self.add(wrap)
        armL = Rectangle(30, 110)
        armL.setFillColor(skin)
        armL.setBorderColor(outline)
        armL.moveTo(-75, -50)
        self.add(armL)
        armR = Rectangle(30, 110)
        armR.setFillColor(skin)
        armR.setBorderColor(outline)
        armR.moveTo(75, -50)
        self.add(armR)
        handL = Ellipse(45, 28)
        handL.setFillColor(skin)
        handL.setBorderColor(outline)
        handL.moveTo(-75, 10)
        self.add(handL)
        handR = Ellipse(45, 28)
        handR.setFillColor(skin)
        handR.setBorderColor(outline)
        handR.moveTo(75, 10)
        self.add(handR)
        legL = Rectangle(30, 90)
        legL.setFillColor(skin)
        legL.setBorderColor(outline)
        legL.moveTo(-25, 80)
        self.add(legL)
        legR = Rectangle(30, 90)
        legR.setFillColor(skin)
        legR.setBorderColor(outline)
        legR.moveTo(25, 80)
        self.add(legR)
        footL = Ellipse(55, 25)
        footL.setFillColor(skin)
        footL.setBorderColor(outline)
        footL.moveTo(-25, 135)
        self.add(footL)
        footR = Ellipse(55, 25)
        footR.setFillColor(skin)
        footR.setBorderColor(outline)
        footR.moveTo(25, 135)
        self.add(footR)
        for dx in (-25, 25):
            strap = Rectangle(50, 6)
            strap.setFillColor("saddlebrown")
            strap.setBorderColor("saddlebrown")
            strap.moveTo(dx, 130)
            self.add(strap)


class Ark(Layer):
    def __init__(self):
        super().__init__()
        boat = Polygon(
            Point(-300, -50), Point(300, -50), Point(200, 120), Point(-200, 120)
        )
        boat.setFillColor("saddlebrown")
        boat.setBorderColor("peru")
        boat.setBorderWidth(3)
        self.add(boat)
        house_width = 225
        house_height = 135
        house_bottom_y = -50
        house_center_y = house_bottom_y - (house_height / 2)
        house = Rectangle(house_width, house_height, Point(0, house_center_y))
        house.setFillColor("burlywood")
        house.setBorderColor("peru")
        house.setBorderWidth(3)
        self.add(house)
        window = Rectangle(28, 28, Point(-30, house_center_y))
        window.setFillColor("brown")
        window.setBorderColor("saddlebrown")
        window.setBorderWidth(3)
        self.add(window)
        roof_top_y = house_center_y - (house_height / 2)
        roof_peak_y = roof_top_y - 60
        left_x = 0 - (house_width / 2)
        right_x = 0 + (house_width / 2)
        roof_left = Polygon(
            Point(left_x, roof_top_y),
            Point(0, roof_peak_y),
            Point(0, roof_top_y)
        )
        roof_left.setFillColor("tan")
        roof_left.setBorderColor("saddlebrown")
        roof_left.setBorderWidth(3)
        self.add(roof_left)
        roof_right = Polygon(
            Point(0, roof_peak_y),
            Point(right_x, roof_top_y),
            Point(0, roof_top_y)
        )
        roof_right.setFillColor("chocolate")
        roof_right.setBorderColor("saddlebrown")
        roof_right.setBorderWidth(3)
        self.add(roof_right)
        # Add door
        self.door = Rectangle(60, 100, Point(-150, 70))
        self.door.setFillColor("coral")
        self.door.setBorderColor("chocolate")
        self.door.setBorderWidth(5)
        self.add(self.door)


class ThunderStorm(Layer):
    def __init__(self, x, y, size=1.0):
        super().__init__()
        base_lightning_points = [
            Point(-25, -45),  # top-left corner
            Point(-10, -20),  # first zig down-right
            Point(-20, -5),  # second zig down-left
            Point(0, 10),  # center point (widest part)
            Point(-10, 25),  # third zig down-left
            Point(5, 40),  # fourth zig down-right
            Point(15, 60)  # bottom tip (pointed end)
        ]
        for i in range(3):
            lightning = Polygon(*base_lightning_points)
            lightning.setFillColor("yellow")
            lightning.setBorderColor("orange1")
            lightning.setBorderWidth(2)
            lightning.scale(size)
            if i == 0:
                lightning.rotate(-5)
            elif i == 1:
                lightning.rotate(0)
            else:
                lightning.rotate(5)
            lightning.move(x + i * 70 * size, y)
            self.add(lightning)


def animate_thunder_blink(canvas, storm_layer, duration=5, blink_rate=0.3):
    canvas.setAutoRefresh(False)
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        for obj in storm_layer.getContents():
            obj.setFillColor("yellow")
            obj.setBorderColor("orange1")
        canvas.refresh()
        time.sleep(blink_rate / 2)
        for obj in storm_layer.getContents():
            obj.setFillColor("black")
            obj.setBorderColor("black")
        canvas.refresh()
        time.sleep(blink_rate / 2)
    canvas.setAutoRefresh(True)


class Raindrop(Layer):
    def __init__(self, x, y):
        super().__init__()
        stem = Path(Point(x, y), Point(x, y + 30))
        stem.setBorderColor('blue2')
        stem.setBorderWidth(2)
        stem.setDepth(41)
        head = Ellipse(6, 4, Point(x, y + 32))
        head.setFillColor('blue2')
        head.setBorderColor('blue2')
        head.setDepth(41)
        self.add(stem)
        self.add(head)


def animate_rain(canvas, drops, duration=5):
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        for d in drops:
            d.move(0, 15)
            ref_point = d.getReferencePoint()
            if ref_point.getY() > 600:
                new_y = -30
                new_x = ref_point.getX()
                d.moveTo(new_x, new_y)
        canvas.refresh()
        time.sleep(0.05)


class WaterWave(Ellipse):
    def __init__(self, y_offset, wave_intensity=1.0):
        super().__init__(1000, 20 * wave_intensity, Point(500, 500 + y_offset))
        self.setFillColor(Color("navy"))
        self.setBorderColor(Color("blue"))
        self.setBorderWidth(0)
        self.setDepth(49)


def animate_flood(canvas, ark, waves, duration=15, intensity_factor=1.0):
    canvas.setAutoRefresh(False)
    start_time = time.time()
    end_time = start_time + duration
    ark_initial_x = ark.getReferencePoint().getX()
    ark_initial_y = ark.getReferencePoint().getY()
    for wave in waves:
        canvas.add(wave)
    frame_rate = 20
    frame_duration = 1.0 / frame_rate
    wave_phase = 0
    pitch_phase = 0
    roll_phase = 0
    while time.time() < end_time:
        elapsed = time.time() - start_time
        time_ratio = elapsed / duration
        wave_phase += 0.1
        pitch_phase += 0.08
        roll_phase += 0.06
        ark_vertical_movement = math.sin(wave_phase * 1.1) * 10 * intensity_factor
        ark.moveTo(ark_initial_x, ark_initial_y + ark_vertical_movement)
        canvas.refresh()
        time.sleep(frame_duration)
    canvas.setAutoRefresh(True)


def create_continuous_rain_effect(canvas, duration=15):
    all_drops = []
    for set_num in range(3):
        drops = []
        cols = 15
        rows = 5
        spacing_x = 50
        spacing_y = 60
        offset_x = set_num * 200
        for r in range(rows):
            for c in range(cols):
                start_x = (30 + c * spacing_x + offset_x) % 1000
                start_y = 20 + r * spacing_y - (set_num * 200)
                drop = Raindrop(start_x, start_y)
                drops.append(drop)
                canvas.add(drop)
        all_drops.extend(drops)
    canvas.setAutoRefresh(False)
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        for drop in all_drops:
            drop.move(0, 15)
            ref_point = drop.getReferencePoint()
            if ref_point.getY() > 650:
                new_y = -30
                new_x = ref_point.getX()
                drop.moveTo(new_x, new_y)
        canvas.refresh()
        time.sleep(0.05)
    canvas.setAutoRefresh(True)


def animate_ground_flood(canvas, ground, duration=10):
    canvas.setAutoRefresh(False)
    steps = 100
    step_duration = duration / steps
    for i in range(steps + 1):
        t = i / steps
        orig_r, orig_g, orig_b = 0, 128, 0
        target_r, target_g, target_b = 0, 0, 205
        r = int(orig_r + (target_r - orig_r) * t)
        g = int(orig_g + (target_g - orig_g) * t)
        b = int(orig_b + (target_b - orig_b) * t)
        new_color = Color((r, g, b))
        ground.setFillColor(new_color)
        ground.setBorderColor(new_color)
        canvas.refresh()
        time.sleep(step_duration)
    canvas.setAutoRefresh(True)


def animate_ground_recovery(canvas, ground, duration=10):
    canvas.setAutoRefresh(False)
    steps = 100
    step_duration = duration / steps
    for i in range(steps + 1):
        t = i / steps
        orig_r, orig_g, orig_b = 0, 0, 205
        target_r, target_g, target_b = 0, 128, 0
        r = int(orig_r + (target_r - orig_r) * t)
        g = int(orig_g + (target_g - orig_g) * t)
        b = int(orig_b + (target_b - orig_b) * t)
        new_color = Color((r, g, b))
        ground.setFillColor(new_color)
        ground.setBorderColor(new_color)
        canvas.refresh()
        time.sleep(step_duration)
    canvas.setAutoRefresh(True)


def animate_rain_and_lightning(canvas, duration=15):
    canvas.setAutoRefresh(False)
    start_time = time.time()
    end_time = start_time + duration
    all_drops = []
    for set_num in range(3):
        drops = []
        cols = 15
        rows = 5
        spacing_x = 50
        spacing_y = 60
        offset_x = set_num * 200
        for r in range(rows):
            for c in range(cols):
                start_x = (30 + c * spacing_x + offset_x) % 1000
                start_y = 20 + r * spacing_y - (set_num * 200)
                drop = Raindrop(start_x, start_y)
                drops.append(drop)
                canvas.add(drop)
        all_drops.extend(drops)
    thunder = ThunderStorm(400, 300, 1.2)
    canvas.add(thunder)
    frame_rate = 20
    frame_duration = 1.0 / frame_rate
    last_lightning_time = time.time()
    lightning_active = False
    lightning_duration = 0.2
    lightning_timer = 0
    while time.time() < end_time:
        current_time = time.time()
        if not lightning_active and (current_time - last_lightning_time) > 3:
            for obj in thunder.getContents():
                obj.setFillColor("yellow")
                obj.setBorderColor("orange1")
            lightning_active = True
            lightning_timer = current_time
            last_lightning_time = current_time
        elif lightning_active and (current_time - lightning_timer) >= lightning_duration:
            for obj in thunder.getContents():
                obj.setFillColor("black")
                obj.setBorderColor("black")
            lightning_active = False
        for drop in all_drops:
            drop.move(0, 15)
            ref_point = drop.getReferencePoint()
            if ref_point.getY() > 650:
                new_y = -30
                new_x = ref_point.getX()
                drop.moveTo(new_x, new_y)
        canvas.refresh()
        time.sleep(frame_duration)
    canvas.remove(thunder)
    for drop in all_drops:
        canvas.remove(drop)
    canvas.setAutoRefresh(True)


def create_rainbow(canvas, center_x=500, center_y=600, radius=500,
                   colors=['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink'], duration=5):
    rainbow_layer = Layer()
    num_colors = len(colors)
    arc_width = radius / num_colors
    canvas.setAutoRefresh(False)
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        rainbow_layer.clear()
        elapsed = time.time() - start_time
        progress = min(elapsed / duration, 1.0)
        for i, color in enumerate(colors):
            outer_r = radius - i * arc_width
            inner_r = outer_r - arc_width
            max_angle = math.pi * progress
            points = []
            num_points = 100
            for j in range(num_points + 1):
                angle = max_angle * j / num_points
                x_outer = center_x + outer_r * math.cos(angle)
                y_outer = center_y - outer_r * math.sin(angle)
                points.append(Point(x_outer, y_outer))
            for j in range(num_points, -1, -1):
                angle = max_angle * j / num_points
                x_inner = center_x + inner_r * math.cos(angle)
                y_inner = center_y - inner_r * math.sin(angle)
                points.append(Point(x_inner, y_inner))
            arc = Polygon(*points)
            arc.setFillColor(color)
            arc.setBorderColor(color)
            arc.setDepth(51)
            rainbow_layer.add(arc)
        canvas.refresh()
        time.sleep(0.05)
    canvas.setAutoRefresh(True)
    return rainbow_layer


class StoryAnimation:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.setAutoRefresh(False)

    def run(self):
        self.canvas.setBackgroundColor("light blue")
        self.canvas.setTitle("Noah's Ark Story")

        ground_top_y = 450
        ground = Rectangle(1000, 150)
        ground.move(500, 525)
        ground.setFillColor("green")
        ground.setBorderColor("green")
        ground.setDepth(50)
        self.canvas.add(ground)
        self.canvas.refresh()

        sun_radius = 40
        sun = Circle(sun_radius)
        sun.move(80, 80)
        sun.setFillColor("yellow")
        sun.setBorderColor("orange")
        sun.setDepth(49)
        self.canvas.add(sun)
        self.canvas.refresh()

        rays = add_sun_rays(80, 80, sun_radius)
        for ray in rays:
            self.canvas.add(ray)
        self.canvas.refresh()

        mountain1 = Mountain(350, 300, (200, 150), "cornsilk4")
        self.canvas.add(mountain1)
        mountain2 = Mountain(180, 120, (800, 330), "brown")
        self.canvas.add(mountain2)
        self.canvas.refresh()

        tree2 = Tree((850, 600))
        self.canvas.add(tree2)
        self.canvas.refresh()

        cloud1_layer = Layer()
        for offset in [(-20, 0), (0, -15), (20, 0)]:
            part = Ellipse(40, 20)
            part.move(200 + offset[0], 100 + offset[1])
            part.setFillColor("white")
            part.setBorderColor("lightgray")
            cloud1_layer.add(part)
        cloud1_layer.setDepth(39)
        self.canvas.add(cloud1_layer)
        cloud2_layer = Layer()
        for offset in [(-20, 0), (0, -15), (20, 0)]:
            part = Ellipse(60, 30)
            part.move(400 + offset[0], 150 + offset[1])
            part.setFillColor("white")
            part.setBorderColor("lightgray")
            cloud2_layer.add(part)
        cloud2_layer.setDepth(39)
        self.canvas.add(cloud2_layer)
        cloud3_layer = Layer()
        for offset in [(-20, 0), (0, -15), (20, 0)]:
            part = Ellipse(50, 20)
            part.move(600 + offset[0], 120 + offset[1])
            part.setFillColor("white")
            part.setBorderColor("lightgray")
            cloud3_layer.add(part)
        cloud3_layer.setDepth(39)
        self.canvas.add(cloud3_layer)
        cloud4_layer = Layer()
        for offset in [(-20, 0), (0, -15), (20, 0)]:
            part = Ellipse(45, 25)
            part.move(800 + offset[0], 150 + offset[1])
            part.setFillColor("white")
            part.setBorderColor("lightgray")
            cloud4_layer.add(part)
        cloud4_layer.setDepth(39)
        self.canvas.add(cloud4_layer)
        self.canvas.refresh()

        cloud5_layer = Layer()
        for offset in [(-20, 0), (0, -15), (20, 0)]:
            part = Ellipse(40, 20)
            part.move(200 + offset[0], 100 + offset[1])
            part.setFillColor("azure4")
            part.setBorderColor("lightgray")
            cloud5_layer.add(part)
        cloud5_layer.setDepth(39)
        cloud6_layer = Layer()
        for offset in [(-20, 0), (0, -15), (20, 0)]:
            part = Ellipse(60, 30)
            part.move(400 + offset[0], 150 + offset[1])
            part.setFillColor("azure4")
            part.setBorderColor("lightgray")
            cloud6_layer.add(part)
        cloud6_layer.setDepth(39)
        cloud7_layer = Layer()
        for offset in [(-20, 0), (0, -15), (20, 0)]:
            part = Ellipse(50, 20)
            part.move(600 + offset[0], 120 + offset[1])
            part.setFillColor("azure4")
            part.setBorderColor("lightgray")
            cloud7_layer.add(part)
        cloud7_layer.setDepth(39)
        cloud8_layer = Layer()
        for offset in [(-20, 0), (0, -15), (20, 0)]:
            part = Ellipse(45, 25)
            part.move(800 + offset[0], 150 + offset[1])
            part.setFillColor("azure4")
            part.setBorderColor("lightgray")
            cloud8_layer.add(part)
        cloud8_layer.setDepth(39)

        noah_feet_relative = 180
        wife_feet_relative = 180
        kid_feet_relative = 135

        character_scale = 0.25
        kid_scale = 0.15


        def animate_walk_in(obj, start_x, start_y, end_x, end_y, steps=50, sleep_time=0.2):
            dx = (end_x - start_x) / steps
            dy = (end_y - start_y) / steps
            obj.move(start_x, start_y)
            obj.setDepth(41)
            self.canvas.add(obj)
            self.canvas.refresh()
            for i in range(steps):
                obj.move(dx, dy)
                if i % 4 < 2:
                    obj.move(0, -2)
                else:
                    obj.move(0, 2)
                self.canvas.refresh()
                time.sleep(sleep_time)

        noah = Noah()
        noah.scale(character_scale)
        start_x_noah = 1200
        start_y_noah = ground_top_y - noah_feet_relative * character_scale
        end_x_noah = 520
        end_y_noah = start_y_noah
        animate_walk_in(noah, start_x_noah, start_y_noah, end_x_noah, end_y_noah)
        time.sleep(5)
        text1 = Text("God spoke to Noah: 'Build an ark, for a great flood is coming.'", 18)
        text1.move(500, 100)
        text1.setDepth(10)
        self.canvas.add(text1)
        self.canvas.refresh()
        time.sleep(5)
        self.canvas.remove(text1)
        self.canvas.refresh()

        wife = Wife()
        wife.scale(character_scale)
        start_x_wife = 1200
        start_y_wife = ground_top_y - wife_feet_relative * character_scale
        end_x_wife = 600
        end_y_wife = start_y_wife
        kid = Kid()
        kid.scale(kid_scale)
        start_x_kid = 1250
        start_y_kid = ground_top_y - kid_feet_relative * kid_scale
        end_x_kid = 650
        end_y_kid = start_y_kid

        steps = 50
        sleep_time = 0.2
        dx_wife = (end_x_wife - start_x_wife) / steps
        dy_wife = (end_y_wife - start_y_wife) / steps
        dx_kid = (end_x_kid - start_x_kid) / steps
        dy_kid = (end_y_kid - start_y_kid) / steps
        wife.move(start_x_wife, start_y_wife)
        wife.setDepth(41)
        self.canvas.add(wife)
        kid.move(start_x_kid, start_y_kid)
        kid.setDepth(41)
        self.canvas.add(kid)
        self.canvas.refresh()
        for i in range(steps):
            wife.move(dx_wife, dy_wife)
            kid.move(dx_kid, dy_kid)
            if i % 4 < 2:
                wife.move(0, -2)
                kid.move(0, -2)
            else:
                wife.move(0, 2)
                kid.move(0, 2)
            self.canvas.refresh()
            time.sleep(sleep_time)
        time.sleep(3)
        text2 = Text("Noah and his family began building the ark.", 18)
        text2.move(500, 100)
        text2.setDepth(10)
        self.canvas.add(text2)
        self.canvas.refresh()
        time.sleep(7)
        self.canvas.remove(text2)
        self.canvas.refresh()

        ark_scale = 4.0
        initial_scale = 0.15
        ark = Ark()
        ark.scale(initial_scale)
        ark_bottom_relative = 120 * ark_scale
        ark_y = ground_top_y - ark_bottom_relative + 425
        ark_x = 200
        ark.move(ark_x, ark_y)
        ark.setDepth(42)
        self.canvas.add(ark)
        self.canvas.refresh()
        current_scale = initial_scale
        for i in range(30):
            ark.scale(1.05)
            current_scale *= 1.05
            self.canvas.refresh()
            time.sleep(0.5)
        time.sleep(3)

        door = ark.door
        door_center = door.getReferencePoint()
        dx = -30 * current_scale
        dy = 0
        door.adjustReference(dx, dy)
        for i in range(18):
            door.rotate(-5)
            self.canvas.refresh()
            time.sleep(0.3)
        time.sleep(2)

        entrance_x = ark_x + (door_center.getX() + dx) * current_scale
        entrance_y = ground_top_y

        text3 = Text("Then the animals came two by two to enter the ark.", 18)
        text3.move(500, 100)
        text3.setDepth(10)
        self.canvas.add(text3)
        self.canvas.refresh()
        time.sleep(5)
        self.canvas.remove(text3)
        self.canvas.refresh()


        def animate_entry(animal1, animal2, start_x, start_y1, start_y2, steps=100, sleep_time=0.1):
            if isinstance(animal1, Layer):
                animal1_layer = animal1
                def animal1_move(dx, dy):
                    animal1.move(dx, dy)
                animal1_set_depth = animal1.setDepth
            else:
                animal1_layer = animal1.layer
                def animal1_move(dx, dy):
                    animal1_layer.move(dx, dy)
                    animal1.x += dx
                    animal1.y += dy
                animal1_set_depth = animal1_layer.setDepth
            if isinstance(animal2, Layer):
                animal2_layer = animal2
                def animal2_move(dx, dy):
                    animal2.move(dx, dy)
                animal2_set_depth = animal2.setDepth
            else:
                animal2_layer = animal2.layer
                def animal2_move(dx, dy):
                    animal2_layer.move(dx, dy)
                    animal2.x += dx
                    animal2.y += dy
                animal2_set_depth = animal2_layer.setDepth
            animal1_move(start_x, start_y1)
            animal2_move(start_x + 50, start_y2)
            animal1_set_depth(41)
            animal2_set_depth(41)
            self.canvas.add(animal1_layer)
            self.canvas.add(animal2_layer)
            self.canvas.refresh()
            dx = (entrance_x - start_x) / steps
            for i in range(steps):
                animal1_move(dx, 0)
                animal2_move(dx, 0)
                if i % 4 < 2:
                    animal1_move(0, -2)
                    animal2_move(0, -2)
                else:
                    animal1_move(0, 2)
                    animal2_move(0, 2)
                if not isinstance(animal1, Layer):
                    if isinstance(animal1, Giraffe):
                        animal1.walk()
                        animal1.sway_neck()
                    elif isinstance(animal1, Elephant):
                        animal1.walk()
                        animal1.swing_trunk()
                if not isinstance(animal2, Layer):
                    if isinstance(animal2, Giraffe):
                        animal2.walk()
                        animal2.sway_neck()
                    elif isinstance(animal2, Elephant):
                        animal2.walk()
                        animal2.swing_trunk()
                self.canvas.refresh()
                time.sleep(sleep_time)
            animal1_set_depth(43)
            animal2_set_depth(43)
            self.canvas.refresh()
            time.sleep(0.5)
            for _ in range(10):
                animal1_move(5, 0)
                animal2_move(5, 0)
                self.canvas.refresh()
                time.sleep(0.05)
            self.canvas.remove(animal1_layer)
            self.canvas.remove(animal2_layer)
            self.canvas.refresh()
            time.sleep(1)


        goat_start_x = 1100
        goat_start_y = ground_top_y - 20
        goat1 = Goat(x=0, y=0)
        goat2 = Goat(x=0, y=0)
        animate_entry(goat1, goat2, goat_start_x, goat_start_y, goat_start_y + 20)

        chicken_start_x = 1100
        chicken_start_y = ground_top_y - 15
        chicken1 = Chicken(x=0, y=0)
        chicken2 = Chicken(x=0, y=0)
        animate_entry(chicken1, chicken2, chicken_start_x, chicken_start_y, chicken_start_y + 10)


        def animate_fly_entry(bird1, bird2, start_x, start_y1, start_y2, steps=100, sleep_time=0.1):
            bird1.move(start_x, start_y1)
            bird2.move(start_x + 50, start_y2)
            bird1.setDepth(41)
            bird2.setDepth(41)
            self.canvas.add(bird1)
            self.canvas.add(bird2)
            self.canvas.refresh()
            dx = (entrance_x - start_x) / steps
            entrance_y_bird = entrance_y - 50
            dy1 = (entrance_y_bird - start_y1) / steps
            dy2 = (entrance_y_bird - start_y2) / steps
            for i in range(steps):
                bird1.move(dx, dy1 + math.sin(i * 0.1) * 5)
                bird2.move(dx, dy2 + math.sin(i * 0.1) * 5)
                self.canvas.refresh()
                time.sleep(sleep_time)
            bird1.setDepth(43)
            bird2.setDepth(43)
            self.canvas.refresh()
            time.sleep(0.5)
            for _ in range(10):
                bird1.move(5, 0)
                bird2.move(5, 0)
                self.canvas.refresh()
                time.sleep(0.05)
            self.canvas.remove(bird1)
            self.canvas.remove(bird2)
            self.canvas.refresh()
            time.sleep(1)


        bird_start_x = 1100
        bird_start_y = 200
        bird1 = Bird(x=0, y=0)
        bird2 = Bird(x=0, y=0)
        animate_fly_entry(bird1, bird2, bird_start_x, bird_start_y, bird_start_y + 20)

        giraffe_start_x = 1100
        giraffe_start_y = ground_top_y - 70
        giraffe1 = Giraffe(0, 0)
        giraffe2 = Giraffe(0, 0)
        giraffe1.layer.scale(0.4)
        giraffe2.layer.scale(0.4)
        animate_entry(giraffe1, giraffe2, giraffe_start_x, giraffe_start_y, giraffe_start_y + 30)

        elephant_start_x = 1100
        elephant_start_y = ground_top_y - 60
        elephant1 = Elephant(0, 0)
        elephant2 = Elephant(0, 0)
        animate_entry(elephant1, elephant2, elephant_start_x, elephant_start_y, elephant_start_y + 40)

        rabbit_start_x = 1100
        rabbit_start_y = ground_top_y - 15
        rabbit1 = Rabbit(0, 0)
        rabbit2 = Rabbit(0, 0)
        animate_entry(rabbit1, rabbit2, rabbit_start_x, rabbit_start_y, rabbit_start_y + 10)

        text4 = Text("And they all entered the ark as God commanded.", 18)
        text4.move(500, 100)
        text4.setDepth(10)
        self.canvas.add(text4)
        self.canvas.refresh()
        time.sleep(10)
        self.canvas.remove(text4)
        self.canvas.refresh()

        text5 = Text("Noah and his family enter the ark", 18)
        text5.move(500, 100)
        text5.setDepth(10)
        self.canvas.add(text5)
        self.canvas.refresh()
        time.sleep(5)
        self.canvas.remove(text5)
        self.canvas.refresh()


        def animate_entry_single(person, steps=100, sleep_time=0.1):
            current_x = person.getReferencePoint().getX()
            current_y = person.getReferencePoint().getY()
            dx = (entrance_x - current_x) / steps
            dy = (entrance_y - current_y) / steps
            person.setDepth(41)
            for i in range(steps):
                person.move(dx, dy)
                if i % 4 < 2:
                    person.move(0, -2)
                else:
                    person.move(0, 2)
                self.canvas.refresh()
                time.sleep(sleep_time)
            person.setDepth(43)
            self.canvas.refresh()
            time.sleep(0.5)
            for _ in range(10):
                person.move(5, 0)
                self.canvas.refresh()
                time.sleep(0.05)
            self.canvas.remove(person)
            self.canvas.refresh()
            time.sleep(1)


        animate_entry_single(noah)
        animate_entry_single(wife)
        animate_entry_single(kid)

        for i in range(18):
            door.rotate(5)
            self.canvas.refresh()
            time.sleep(0.3)
        time.sleep(2)

        thunder = ThunderStorm(400, 300, 1.2)
        self.canvas.add(thunder)
        animate_thunder_blink(self.canvas, thunder, 5, 0.3)
        self.canvas.remove(thunder)
        self.canvas.refresh()

        drops = []
        cols = 15
        rows = 5
        spacing_x = 50
        spacing_y = 60
        for r in range(rows):
            for c in range(cols):
                start_x = 30 + c * spacing_x
                start_y = 20 + r * spacing_y
                drop = Raindrop(start_x, start_y)
                self.canvas.add(drop)
                drops.append(drop)

        animate_rain(self.canvas, drops, 5)

        self.canvas.setBackgroundColor("darkgrey")
        self.canvas.remove(sun)
        for ray in rays:
            self.canvas.remove(ray)
        self.canvas.remove(cloud1_layer)
        self.canvas.remove(cloud2_layer)
        self.canvas.remove(cloud3_layer)
        self.canvas.remove(cloud4_layer)
        self.canvas.add(cloud5_layer)
        self.canvas.add(cloud6_layer)
        self.canvas.add(cloud7_layer)
        self.canvas.add(cloud8_layer)
        self.canvas.refresh()

        animate_rain(self.canvas, drops, 7)

        self.canvas.remove(tree2)
        for drop in drops:
            self.canvas.remove(drop)
        self.canvas.refresh()

        animate_ground_flood(self.canvas, ground, duration=10)

        waves = []
        for i in range(5):
            wave = WaterWave(i * 40, 1.5)
            waves.append(wave)

        flood_text = Text("The Great Flood Begins: 40 Days and 40 Nights", 20)
        flood_text.move(500, 100)
        flood_text.setDepth(10)
        self.canvas.add(flood_text)
        self.canvas.refresh()
        time.sleep(5)
        self.canvas.remove(flood_text)
        self.canvas.refresh()

        animate_rain_and_lightning(self.canvas, duration=15)

        animate_flood(self.canvas, ark, waves, duration=15, intensity_factor=1.0)

        for wave in waves:
            self.canvas.remove(wave)

        end_text = Text("The ark floats safely on the turbulent waters.", 18)
        end_text.move(500, 100)
        end_text.setDepth(10)
        self.canvas.add(end_text)
        self.canvas.refresh()
        time.sleep(5)
        self.canvas.remove(end_text)
        self.canvas.refresh()

        animate_ground_recovery(self.canvas, ground, duration=10)

        self.canvas.setBackgroundColor("light blue")
        self.canvas.refresh()

        self.canvas.add(sun)
        for ray in rays:
            self.canvas.add(ray)
        self.canvas.refresh()

        self.canvas.add(tree2)
        self.canvas.refresh()

        recovery_text = Text("The waters receded and life returned to the land.", 18)
        recovery_text.move(500, 100)
        recovery_text.setDepth(10)
        self.canvas.add(recovery_text)
        self.canvas.refresh()
        time.sleep(5)
        self.canvas.remove(recovery_text)
        self.canvas.refresh()

        rainbow = create_rainbow(self.canvas, radius=500, duration=8)
        rainbow.setDepth(51)
        self.canvas.add(rainbow)
        self.canvas.refresh()

        rainbow_text = Text("God promised never again to destroy all life on earth by a worldwide flood (Genesis 9:11–17)", 18)
        rainbow_text.move(500, 100)
        rainbow_text.setDepth(10)
        self.canvas.add(rainbow_text)
        self.canvas.refresh()
        time.sleep(5)
        self.canvas.remove(rainbow_text)
        self.canvas.refresh()

        door.adjustReference(dx, dy)
        for i in range(18):
            door.rotate(-5)
            self.canvas.refresh()
            time.sleep(0.3)
        time.sleep(2)

        exit_x = ark_x + (door_center.getX() + dx) * current_scale
        exit_y = ground_top_y


        def animate_exit_single(person, start_x, start_y, end_x, end_y, steps=100, sleep_time=0.1):
            person.moveTo(start_x, start_y)
            person.setDepth(40)
            self.canvas.add(person)
            self.canvas.refresh()
            dx = (end_x - start_x) / steps
            dy = (end_y - start_y) / steps
            for i in range(steps):
                person.move(dx, dy)
                if i % 4 < 2:
                    person.move(0, -2)
                else:
                    person.move(0, 2)
                self.canvas.refresh()
                time.sleep(sleep_time)
            person.setDepth(40)
            self.canvas.refresh()
            time.sleep(1)


        noah_original_x = 520
        noah_original_y = ground_top_y - noah_feet_relative * character_scale
        wife_original_x = 600
        wife_original_y = ground_top_y - wife_feet_relative * character_scale
        kid_original_x = 650
        kid_original_y = ground_top_y - kid_feet_relative * kid_scale

        animate_exit_single(noah, exit_x, exit_y, noah_original_x, noah_original_y, steps=100, sleep_time=0.1)
        animate_exit_single(wife, exit_x + 80, exit_y, wife_original_x, wife_original_y, steps=100, sleep_time=0.1)
        animate_exit_single(kid, exit_x + 160, exit_y, kid_original_x, kid_original_y, steps=100, sleep_time=0.1)

        final_text = Text("Noah's family stepped out onto the renewed earth, grateful for God's protection.", 18)
        final_text.move(500, 100)
        final_text.setDepth(10)
        self.canvas.add(final_text)
        self.canvas.refresh()


if __name__ == "__main__":
    canvas = Canvas(1000, 600, 'black', "Noah's Ark Story")

    open_anim = OpeningAnimation(canvas)
    open_anim.run()

    story_anim = StoryAnimation(canvas)
    story_anim.run()
    canvas.clear()

    close_anim = ClosingAnimation(canvas)
    close_anim.run()

    canvas.wait()
    canvas.close()
