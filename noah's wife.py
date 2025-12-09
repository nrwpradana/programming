from cs1graphics import *

canvas = Canvas(800, 800)
canvas.setBackgroundColor("white")
canvas.setTitle("Noah's Wife")


# ----------------------------------------
# Noah's Wife Character
# ----------------------------------------

noahs_wife = Layer()
canvas.add(noahs_wife)

# Colors
skin = Color("peachpuff")
robe_color = Color("plum")       # soft purple
outline = Color("saddlebrown")
hair_color = Color("lightgrey")


# === HEAD ===
head = Circle(65)
head.setFillColor(skin)
head.setBorderColor(outline)
head.moveTo(400, 210)
noahs_wife.add(head)

# === HAIR (full top + curls down both sides, no face covering) ===
hair_color = Color("lightgrey")

# --- Top crown (menutup bagian atas yang kosong) ---
ht1 = Circle(20); ht1.setFillColor(hair_color); ht1.setBorderWidth(0); ht1.moveTo(380,130); noahs_wife.add(ht1)
ht2 = Circle(22); ht2.setFillColor(hair_color); ht2.setBorderWidth(0); ht2.moveTo(400,130); noahs_wife.add(ht2)
ht3 = Circle(20); ht3.setFillColor(hair_color); ht3.setBorderWidth(0); ht3.moveTo(420,130); noahs_wife.add(ht3)
ht4 = Circle(18); ht4.setFillColor(hair_color); ht4.setBorderWidth(0); ht4.moveTo(360,150); noahs_wife.add(ht4)
ht5 = Circle(18); ht5.setFillColor(hair_color); ht5.setBorderWidth(0); ht5.moveTo(440,150); noahs_wife.add(ht5)

# --- Left curl side (downward) ---
hl1 = Circle(20); hl1.setFillColor(hair_color); hl1.setBorderWidth(0); hl1.moveTo(340,180); noahs_wife.add(hl1)
hl2 = Circle(20); hl2.setFillColor(hair_color); hl2.setBorderWidth(0); hl2.moveTo(335,215); noahs_wife.add(hl2)
hl3 = Circle(20); hl3.setFillColor(hair_color); hl3.setBorderWidth(0); hl3.moveTo(340,250); noahs_wife.add(hl3)
hl4 = Circle(20); hl4.setFillColor(hair_color); hl4.setBorderWidth(0); hl4.moveTo(350,285); noahs_wife.add(hl4)

# --- Right curl side (downward) ---
hr1 = Circle(20); hr1.setFillColor(hair_color); hr1.setBorderWidth(0); hr1.moveTo(460,180); noahs_wife.add(hr1)
hr2 = Circle(20); hr2.setFillColor(hair_color); hr2.setBorderWidth(0); hr2.moveTo(465,215); noahs_wife.add(hr2)
hr3 = Circle(20); hr3.setFillColor(hair_color); hr3.setBorderWidth(0); hr3.moveTo(460,250); noahs_wife.add(hr3)
hr4 = Circle(20); hr4.setFillColor(hair_color); hr4.setBorderWidth(0); hr4.moveTo(450,285); noahs_wife.add(hr4)


# === EYES ===
eyeL = Circle(10)
eyeL.setFillColor("black")
eyeL.moveTo(380, 205)
noahs_wife.add(eyeL)

eyeR = Circle(10)
eyeR.setFillColor("black")
eyeR.moveTo(420, 205)
noahs_wife.add(eyeR)

# === NOSE (smaller + feminine) ===
nose = Polygon(Point(400, 215), Point(392, 230), Point(408, 230))
nose.setFillColor(skin)
nose.setBorderColor(skin)
noahs_wife.add(nose)

# === MOUTH ===
mouth = Polygon(Point(388,245), Point(412,245), Point(400,255))
mouth.setFillColor("lightcoral")
mouth.setBorderColor("lightcoral")
noahs_wife.add(mouth)


# === BODY ===
body = Rectangle(170, 260)
body.setFillColor(robe_color)
body.setBorderColor(robe_color)
body.moveTo(400, 430)
noahs_wife.add(body)

# === ARMS ===
armL = Rectangle(35, 110)
armL.setFillColor(skin)
armL.setBorderColor(outline)
armL.moveTo(315, 420)
noahs_wife.add(armL)

armR = Rectangle(35, 110)
armR.setFillColor(skin)
armR.setBorderColor(outline)
armR.moveTo(485, 420)
noahs_wife.add(armR)


# === HANDS ===
handL = Ellipse(45, 30)
handL.setFillColor(skin)
handL.setBorderColor(outline)
handL.moveTo(315, 480)
noahs_wife.add(handL)

handR = Ellipse(45, 30)
handR.setFillColor(skin)
handR.setBorderColor(outline)
handR.moveTo(485, 480)
noahs_wife.add(handR)


# === FEET ===
footL = Ellipse(60, 30)
footL.setFillColor(skin)
footL.setBorderColor(outline)
footL.moveTo(365, 580)
noahs_wife.add(footL)

footR = Ellipse(60, 30)
footR.setFillColor(skin)
footR.setBorderColor(outline)
footR.moveTo(435, 580)
noahs_wife.add(footR)
