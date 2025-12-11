from cs1graphics import *
import time

# Create canvas
canvas = Canvas(1000, 600, 'black', 'Noah Story - Closing')

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

# Scene 1: Fade from video (0-3 seconds)
def scene1_fade_in():
    """Gradual fade in from video"""
    # Just a pause to simulate video ending
    time.sleep(1)
    film_flicker()
    time.sleep(0.5)

# Scene 2: The End (3-8 seconds)
def scene2_film_end():
    """Classic film ending with THE END"""
    
    # Create "THE END" text
    the_end = Text("THE END", 18)
    the_end.setFontColor('white')
    the_end.setFontSize(80)
    the_end.moveTo(500, 300)
    canvas.add(the_end)
    
    # Add film frame corners
    corner_size = 40
    corners = []
    corner_positions = [
        (150, 100), (850, 100),  # Top corners
        (150, 500), (850, 500)   # Bottom corners
    ]
    
    for x, y in corner_positions:
        corner = Rectangle(corner_size, corner_size, Point(x, y))
        corner.setFillColor('white')
        corner.setBorderWidth(0)
        canvas.add(corner)
        corners.append(corner)
    
    # Hold "THE END"
    time.sleep(3)
    
    # Final film flicker
    film_flicker()
    
    # Remove all
    canvas.remove(the_end)
    for corner in corners:
        canvas.remove(corner)
    
    time.sleep(0.5)

# Scene 3: Thank You for Watching (8-25 seconds)
def scene3_thank_you():
    """Thank you message with elegant animation - no borders, no circles"""
    
    # Main thank you message
    thank_you = Text("Thank You", 18)
    thank_you.setFontColor('white')
    thank_you.setFontSize(68)
    thank_you.moveTo(500, 260)
    canvas.add(thank_you)
    
    time.sleep(0.8)
    
    # "for Watching" text
    for_watching = Text("for Watching", 18)
    for_watching.setFontColor('gold')
    for_watching.setFontSize(52)
    for_watching.moveTo(500, 340)
    canvas.add(for_watching)
    
    time.sleep(1)
    
    # Add floating sparkles around the text
    stars = []
    star_positions = [
        (250, 200), (750, 200),  # Top sides
        (250, 400), (750, 400),  # Bottom sides
        (180, 300), (820, 300),  # Far sides
        (350, 180), (650, 180),  # Upper corners
        (350, 420), (650, 420)   # Lower corners
    ]
    
    for pos in star_positions:
        star = Text("✨", 18)
        star.setFontColor('yellow')
        star.setFontSize(32)
        star.moveTo(pos[0], pos[1])
        canvas.add(star)
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
        canvas.remove(star)
    canvas.remove(thank_you)
    canvas.remove(for_watching)
    
    time.sleep(0.5)

# Main closing animation sequence
def main():
    print("=" * 60)
    print("NOAH'S ARK STORY - CLOSING ANIMATION")
    print("=" * 60)
    print("Duration: ~25 seconds")
    print("Scenes:")
    print("  1. Fade in from video (0-3s)")
    print("  2. The End (3-8s)")
    print("  3. Thank You for Watching (8-25s)")
    print("=" * 60)
    print("\nStarting closing animation...\n")
    
    # Run all closing scenes
    scene1_fade_in()  # Transition from video
    scene2_film_end()  # The End
    film_flicker()  # Transition
    scene3_thank_you()  # Thank you for watching
    
    print("\n" + "=" * 60)
    print("Closing animation complete!")
    print("=" * 60)
    
    # Keep window open
    canvas.wait()

# Run the animation
if __name__ == "__main__":
    main()
