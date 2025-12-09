from cs1graphics import *

canvas = Canvas(700, 800)
canvas.setBackgroundColor("white")
canvas.setTitle("Noah's Kid – Tunic Style")

kid = Layer()
canvas.add(kid)

# Colors
skin = Color("peachpuff")
hair_color = Color("sienna")
tunic_color = Color("peru")
sash_color = Color("saddlebrown")
outline = Color("sienna")

# ===================== HEAD (moved closer to body) =====================
head = Circle(55)
head.setFillColor(skin)
head.setBorderColor(outline)
head.moveTo(350, 210)   # ↓ moved down from 180 → 210
kid.add(head)

# ===================== HAIR (adjusted down by +30) =====================
hair_positions = [
    (310,180), (330,168), (350,163), (370,168), (390,180),
    (305,205), (395,205)
]

for (x,y) in hair_positions:
    h = Circle(15)
    h.setFillColor(hair_color)
    h.setBorderWidth(0)
    h.moveTo(x,y)
    kid.add(h)

# ===================== EYES (also moved down) =====================
eye1 = Circle(10); eye1.setFillColor("black"); eye1.moveTo(335,205); kid.add(eye1)
eye2 = Circle(10); eye2.setFillColor("black"); eye2.moveTo(365,205); kid.add(eye2)

# ===================== MOUTH (also moved down) =====================
smile = Polygon(
    Point(350,235),
    Point(330,220),
    Point(370,220)
)
smile.setFillColor("lightcoral")
smile.setBorderColor("lightcoral")
kid.add(smile)

# ===================== BODY - TUNIC (short) =====================
tunic = Rectangle(130, 180)
tunic.setFillColor(tunic_color)
tunic.setBorderColor(outline)
tunic.moveTo(350, 350)
kid.add(tunic)

# ===================== SASH (sabuk) =====================
sash = Rectangle(160, 40)
sash.setFillColor(sash_color)
sash.setBorderColor(sash_color)
sash.moveTo(350, 315)
kid.add(sash)

# ===================== FABRIC WRAP (kain lilit) =====================
wrap = Polygon(
    Point(300, 360),
    Point(400, 360),
    Point(390, 430),
    Point(310, 430)
)
wrap.setFillColor(tunic_color)
wrap.setBorderColor(outline)
kid.add(wrap)

# ===================== ARMS =====================
armL = Rectangle(30, 110)
armL.setFillColor(skin); armL.setBorderColor(outline)
armL.moveTo(275, 350)
kid.add(armL)

armR = Rectangle(30, 110)
armR.setFillColor(skin); armR.setBorderColor(outline)
armR.moveTo(425, 350)
kid.add(armR)

# Hands
handL = Ellipse(45, 28); handL.setFillColor(skin); handL.setBorderColor(outline); handL.moveTo(275,410); kid.add(handL)
handR = Ellipse(45, 28); handR.setFillColor(skin); handR.setBorderColor(outline); handR.moveTo(425,410); kid.add(handR)

# ===================== LEGS =====================
legL = Rectangle(30, 90)
legL.setFillColor(skin); legL.setBorderColor(outline)
legL.moveTo(325, 480)
kid.add(legL)

legR = Rectangle(30, 90)
legR.setFillColor(skin); legR.setBorderColor(outline)
legR.moveTo(375, 480)
kid.add(legR)

# ===================== SANDALS =====================
footL = Ellipse(55, 25)
footL.setFillColor(skin); footL.setBorderColor(outline)
footL.moveTo(325, 535)
kid.add(footL)

footR = Ellipse(55, 25)
footR.setFillColor(skin); footR.setBorderColor(outline)
footR.moveTo(375, 535)
kid.add(footR)

# sandal straps
for x in (325, 375):
    strap = Rectangle(50, 6)
    strap.setFillColor("saddlebrown")
    strap.setBorderColor("saddlebrown")
    strap.moveTo(x, 530)
    kid.add(strap)
