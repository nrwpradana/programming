from cs1graphics import *

canvas = Canvas(1000, 600)
canvas.setBackgroundColor("white")
canvas.setTitle("Noah's Ark")


# ARK
boat = Polygon(
    Point(200, 350),   # top-left
    Point(800, 350),   # top-right
    Point(700, 520),   # bottom-right
    Point(300, 520)    # bottom-left
)
boat.setFillColor("saddlebrown")
boat.setBorderColor("peru")
boat.setBorderWidth(3)
canvas.add(boat)

# House 


house_width = 225    
house_height = 135      
house_bottom_y = 350    
house_center_y = house_bottom_y - (house_height / 2)

house = Rectangle(house_width, house_height, Point(500, house_center_y))
house.setFillColor("burlywood")
house.setBorderColor("peru")
house.setBorderWidth(3)
canvas.add(house)


# Window
window = Rectangle(28, 28, Point(470, house_center_y))
window.setFillColor("brown")
window.setBorderColor("saddlebrown")
window.setBorderWidth(3)
canvas.add(window)

# Roof
roof_top_y = house_center_y - (house_height / 2)
roof_peak_y = roof_top_y - 60      

left_x = 500 - (house_width / 2)
right_x = 500 + (house_width / 2)

# Roof left
roof_left = Polygon(
    Point(left_x, roof_top_y),
    Point(500, roof_peak_y),
    Point(500, roof_top_y)
)
roof_left.setFillColor("tan")
roof_left.setBorderColor("saddlebrown")
roof_left.setBorderWidth(3)
canvas.add(roof_left)

# Roof Right
roof_right = Polygon(
    Point(500, roof_peak_y),
    Point(right_x, roof_top_y),
    Point(500, roof_top_y)
)
roof_right.setFillColor("chocolate")
roof_right.setBorderColor("saddlebrown")
roof_right.setBorderWidth(3)
canvas.add(roof_right)
