from cs1graphics import *

canvas = Canvas(800, 800)
canvas.setBackgroundColor("white")
canvas.setTitle("Noah")

noah = Layer()
canvas.add(noah)

# Colors
skin = Color("peachpuff")
robe = Color("firebrick")
head_color = Color("peru")
beard_color = Color("lightgrey")
outline = Color("saddlebrown")
staff_color = Color("chocolate")

# HEAD
head = Circle(70)
head.setFillColor(head_color)
head.setBorderColor(outline)
head.moveTo(400, 200)
noah.add(head)

# Hair
# Top row
hair1 = Circle(17); hair1.setFillColor("lightgrey"); hair1.setBorderWidth(0); hair1.moveTo(360,135); noah.add(hair1)
hair2 = Circle(17); hair2.setFillColor("lightgrey"); hair2.setBorderWidth(0); hair2.moveTo(385,120); noah.add(hair2)
hair3 = Circle(17); hair3.setFillColor("lightgrey"); hair3.setBorderWidth(0); hair3.moveTo(415,120); noah.add(hair3)
hair4 = Circle(17); hair4.setFillColor("lightgrey"); hair4.setBorderWidth(0); hair4.moveTo(440,135); noah.add(hair4)

# RIGHT SIDE 
hair5  = Circle(17); hair5.setFillColor("lightgrey"); hair5.setBorderWidth(0); hair5.moveTo(465,150); noah.add(hair5)
hair6  = Circle(17); hair6.setFillColor("lightgrey"); hair6.setBorderWidth(0); hair6.moveTo(470,175); noah.add(hair6)
hair7  = Circle(17); hair7.setFillColor("lightgrey"); hair7.setBorderWidth(0); hair7.moveTo(470,205); noah.add(hair7)
hair8  = Circle(17); hair8.setFillColor("lightgrey"); hair8.setBorderWidth(0); hair8.moveTo(460,235); noah.add(hair8)
hair9  = Circle(17); hair9.setFillColor("lightgrey"); hair9.setBorderWidth(0); hair9.moveTo(450,260); noah.add(hair9)
hair100  = Circle(17); hair100.setFillColor("lightgrey"); hair100.setBorderWidth(0); hair100.moveTo(460,270); noah.add(hair100)


# LEFT SIDE 
hair10 = Circle(17); hair10.setFillColor("lightgrey"); hair10.setBorderWidth(0); hair10.moveTo(335,150); noah.add(hair10)
hair11 = Circle(17); hair11.setFillColor("lightgrey"); hair11.setBorderWidth(0); hair11.moveTo(330,175); noah.add(hair11)
hair12 = Circle(17); hair12.setFillColor("lightgrey"); hair12.setBorderWidth(0); hair12.moveTo(330,205); noah.add(hair12)
hair13 = Circle(17); hair13.setFillColor("lightgrey"); hair13.setBorderWidth(0); hair13.moveTo(340,235); noah.add(hair13)
hair14 = Circle(17); hair14.setFillColor("lightgrey"); hair14.setBorderWidth(0); hair14.moveTo(350,260); noah.add(hair14)
hair14 = Circle(17); hair14.setFillColor("lightgrey"); hair14.setBorderWidth(0); hair14.moveTo(350,260); noah.add(hair14)
hair101 = Circle(17); hair101.setFillColor("lightgrey"); hair101.setBorderWidth(0); hair101.moveTo(330,270); noah.add(hair101)


# EYES
eye1 = Circle(10)
eye1.setFillColor("black")
eye1.moveTo(370, 190)
noah.add(eye1)

eye2 = Circle(10)
eye2.setFillColor("black")
eye2.moveTo(430, 190)
noah.add(eye2)

# NOSE
nose = Polygon(Point(400, 205), Point(390, 225), Point(410, 225))
nose.setFillColor(skin)
nose.setBorderColor(skin)
noah.add(nose)

# BEARD
beard = Polygon(Point(350, 250), Point(450, 250),
                Point(425, 285), Point(375, 285))
beard.setFillColor(beard_color)
beard.setBorderColor(beard_color)
noah.add(beard)

# BODY
body = Rectangle(160, 280)
body.setFillColor(robe)
body.setBorderColor(robe)
body.moveTo(400, 430)
noah.add(body)

# ARMS
left_arm = Rectangle(35, 110)
left_arm.setFillColor(skin)
left_arm.setBorderColor(outline)
left_arm.moveTo(310, 350)
noah.add(left_arm)

right_arm = Rectangle(35, 110)
right_arm.setFillColor(skin)
right_arm.setBorderColor(outline)
right_arm.moveTo(490, 350)
noah.add(right_arm)

# STAFF
staff = Rectangle(20, 320)
staff.setFillColor(staff_color)
staff.setBorderColor(staff_color)
staff.moveTo(275, 410)
noah.add(staff)

# HANDS
left_hand = Ellipse(45, 30)
left_hand.setFillColor(skin)
left_hand.setBorderColor(outline)
left_hand.moveTo(275, 405)
noah.add(left_hand)

right_hand = Ellipse(45, 30)
right_hand.setFillColor(skin)
right_hand.setBorderColor(outline)
right_hand.moveTo(490, 405)
noah.add(right_hand)

# FEET
left_foot = Ellipse(60, 30)
left_foot.setFillColor(skin)
left_foot.setBorderColor(outline)
left_foot.moveTo(360, 580)   
noah.add(left_foot)

right_foot = Ellipse(60, 30)
right_foot.setFillColor(skin)
right_foot.setBorderColor(outline)
right_foot.moveTo(440, 580)  
noah.add(right_foot)
