from cs1graphics import *
import time

# Create canvas
canvas = Canvas(1000, 600, 'black', 'Noah Story - Opening')

# Film flicker transition effect
def film_flicker():
    """Creates a black-white-black flicker effect like old film projectors"""
    # Create white rectangle for flicker
    flicker = Rectangle(1000, 600, Point(500, 300))
    flicker.setFillColor('white')
    flicker.setBorderWidth(0)
    
    # Quick flickers
    for _ in range(3):
        canvas.add(flicker)
        time.sleep(0.05)
        canvas.remove(flicker)
        time.sleep(0.05)

# Scene 1: Noah's Ark Story with Description (0-20 seconds)
def scene1():
    # Change background to dark slate gray
    canvas.setBackgroundColor('darkslategray')
    
    # Create main title
    title = Text("The Noah's Ark Story", 18)
    title.setFontColor('white')
    title.setFontSize(58)
    title.moveTo(500, 100)
    canvas.add(title)
    
    # Create Bible reference
    bible_ref = Text("Based on the Bible - Genesis 6-9", 18)
    bible_ref.setFontColor('gold')
    bible_ref.setFontSize(24)
    bible_ref.moveTo(500, 160)
    
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
        desc.moveTo(500, y_start + (i * 50))
        description_texts.append(desc)
    
    # Fade in title by adjusting depth
    time.sleep(0.5)
    
    # Add Bible reference with delay
    time.sleep(0.5)
    canvas.add(bible_ref)
    time.sleep(0.5)
    
    # Add description line by line
    for desc in description_texts:
        canvas.add(desc)
        time.sleep(0.5)
    
    # Hold the complete scene
    time.sleep(3)
    
    # Remove all elements
    canvas.remove(title)
    canvas.remove(bible_ref)
    for desc in description_texts:
        canvas.remove(desc)
    
    # Keep dark slate gray background for scene 2
    time.sleep(0.3)

# Scene 2: Created by Team (20-35 seconds)
def scene2():
    # Background is already dark slate gray from scene 1
    
    # Create "A Produced by" text
    created = Text("A Produced by", 18)
    created.setFontColor('lightgray')
    created.setFontSize(32)
    created.moveTo(500, 80)
    canvas.add(created)
    
    # Add decorative lines
    line1 = Path(Point(250, 120), Point(450, 120))
    line1.setBorderColor('gold')
    line1.setBorderWidth(3)
    canvas.add(line1)
    
    line2 = Path(Point(550, 120), Point(750, 120))
    line2.setBorderColor('gold')
    line2.setBorderWidth(3)
    canvas.add(line2)
    
    time.sleep(0.8)
    
    # Create team members information
    team_members = [
        "22457001 - Nadhiar Ridho Wahyu Pradana",
        "22457001 - Devy Puspitasari",
        "22547008 - Jerome Mwandoki Mwamunzoyo"
    ]
    
    member_objects = []
    y_positions = [200, 300, 400]
    
    # Add each member with animation
    for i, (member, y_pos) in enumerate(zip(team_members, y_positions)):
        # Create background rectangle
        bg_rect = Rectangle(700, 70, Point(500, y_pos))
        bg_rect.setFillColor('darkblue')
        bg_rect.setBorderColor('cyan')
        bg_rect.setBorderWidth(2)
        canvas.add(bg_rect)
        
        # Create member text
        member_text = Text(member, 18)
        member_text.setFontColor('white')
        member_text.setFontSize(28)
        member_text.moveTo(500, y_pos)
        canvas.add(member_text)
        
        member_objects.append((bg_rect, member_text))
        time.sleep(0.7)
    
    # Hold the scene
    time.sleep(3.5)
    
    # Remove all elements
    canvas.remove(created)
    canvas.remove(line1)
    canvas.remove(line2)
    for bg_rect, member_text in member_objects:
        canvas.remove(bg_rect)
        canvas.remove(member_text)
    
    # Change background back to black for scene 3
    canvas.setBackgroundColor('black')
    time.sleep(0.3)

# Scene 3: Enjoy the video (35-55 seconds)
def scene3_enjoy():
    # Create main message (no circle behind)
    enjoy = Text("Enjoy the Video", 18)
    enjoy.setFontColor('white')
    enjoy.setFontSize(64)
    enjoy.moveTo(500, 300)
    canvas.add(enjoy)
    
    time.sleep(0.8)
    
    # Add sparkle stars in corners - far from the text
    stars = []
    star_positions = [
        (150, 120), (850, 120),  # Top corners
        (150, 480), (850, 480),  # Bottom corners
        (100, 300), (900, 300),  # Far left and right
        (250, 180), (750, 180),  # Upper sides
        (250, 420), (750, 420)   # Lower sides
    ]
    
    for pos in star_positions:
        star = Text("✨", 18)
        star.setFontColor('yellow')
        star.setFontSize(40)
        star.moveTo(pos[0], pos[1])
        canvas.add(star)
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
    canvas.remove(enjoy)
    for star in stars:
        canvas.remove(star)
    time.sleep(0.3)

# Scene 4: Film Countdown (55-60 seconds)
def scene4_countdown():
    """Classic film countdown: 3-2-1 with film reel circles"""
    
    # Countdown numbers
    for count in [3, 2, 1]:
        # Create outer circle (film reel)
        outer_circle = Circle(200, Point(500, 300))
        outer_circle.setFillColor('white')
        outer_circle.setBorderColor('black')
        outer_circle.setBorderWidth(8)
        canvas.add(outer_circle)
        
        # Create inner circle
        inner_circle = Circle(150, Point(500, 300))
        inner_circle.setFillColor('black')
        inner_circle.setBorderWidth(0)
        canvas.add(inner_circle)
        
        # Create countdown number
        number = Text(str(count), 18)
        number.setFontColor('white')
        number.setFontSize(120)
        number.moveTo(500, 300)
        canvas.add(number)
        
        # Create corner markers (film frame corners)
        corner_size = 30
        corners = []
        corner_positions = [
            (350, 150), (650, 150),  # Top corners
            (350, 450), (650, 450)   # Bottom corners
        ]
        
        for x, y in corner_positions:
            corner = Rectangle(corner_size, corner_size, Point(x, y))
            corner.setFillColor('white')
            corner.setBorderWidth(0)
            canvas.add(corner)
            corners.append(corner)
        
        # Add film scratches (vertical lines)
        scratch1 = Path(Point(200, 100), Point(200, 500))
        scratch1.setBorderColor('gray')
        scratch1.setBorderWidth(2)
        canvas.add(scratch1)
        
        scratch2 = Path(Point(800, 100), Point(800, 500))
        scratch2.setBorderColor('gray')
        scratch2.setBorderWidth(2)
        canvas.add(scratch2)
        
        # Hold for 1 second
        time.sleep(1)
        
        # Remove all countdown elements
        canvas.remove(outer_circle)
        canvas.remove(inner_circle)
        canvas.remove(number)
        for corner in corners:
            canvas.remove(corner)
        canvas.remove(scratch1)
        canvas.remove(scratch2)
        
        # Brief black screen
        time.sleep(0.2)
    
    # Final flicker before video starts
    film_flicker()

# Main animation sequence
def main():
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
    scene1()  # Noah's Ark Story with description
    film_flicker()  # Transition effect
    
    scene2()  # Created by team members
    film_flicker()  # Transition effect
    
    scene3_enjoy()  # Enjoy the video (no circle, stars in corners)
    
    scene4_countdown()  # Film countdown 3-2-1
    
    print("\n" + "=" * 60)
    print("Animation complete! The video is starting now...")
    print("=" * 60)
    
    # Keep window open
    canvas.wait()

# Run the animation
if __name__ == "__main__":
    main()
