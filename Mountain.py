from cs1graphics import *
import math
import time # Import time module untuk animasi

# Membuat canvas utama
canvas = Canvas(1000, 600)  # Ukuran canvas bisa disesuaikan
canvas.setBackgroundColor("light blue")
canvas.setTitle("Noah's Ark Scene - Initial")

# Membuat dan menambahkan tanah (ground)
ground = Rectangle(1000, 150)  # Lebar 1000, tinggi 150
ground.move(500, 525)  # Pusat di (500, 525) agar dasar ground ada di y=600
ground.setFillColor("green")
ground.setBorderColor("green")
canvas.add(ground)

# Membuat dan menambahkan matahari
sun_radius = 40
sun = Circle(sun_radius)  # Radius 40
sun.move(80, 80)  # Pojok kiri atas
sun.setFillColor("yellow")
sun.setBorderColor("orange")
canvas.add(sun)

# --- Fungsi untuk Membuat Pohon ---
def make_tree(position=(170, 600), trunk_width=30, trunk_height=250, leaves_size=(150, 100)):
    """
    Membuat pohon sebagai Layer.
    :param position: Titik tengah batang pohon (x, y)
    :param trunk_width: Lebar batang
    :param trunk_height: Tinggi batang
    :param leaves_size: Ukuran elips daun (lebar, tinggi)
    :return: Objek Layer yang berisi seluruh bagian pohon
    """
    tree_layer = Layer()

    # Batang
    trunk = Rectangle(trunk_width, trunk_height, Point(position[0], position[1]))
    trunk.setFillColor('brown')
    trunk.setBorderWidth(0)
    trunk.setDepth(44)
    tree_layer.add(trunk)

    # Cabang 1
    branch1 = Polygon(Point(position[0] + 10, position[1] - 10),
                      Point(position[0] + 10, position[1] - 50),
                      Point(position[0] + 110, position[1] - 120))
    branch1.setFillColor('brown')
    branch1.setBorderWidth(0)
    branch1.setDepth(44)
    tree_layer.add(branch1)

    # Cabang 2
    branch2 = Polygon(Point(position[0] - 10, position[1] + 20),
                      Point(position[0] - 10, position[1] - 20),
                      Point(position[0] - 110, position[1] - 90))
    branch2.setFillColor('brown')
    branch2.setBorderWidth(0)
    branch2.setDepth(44)
    tree_layer.add(branch2)

    # Daun (Ellipse)
    leaves = Ellipse(leaves_size[0], leaves_size[1], Point(position[0], position[1] - 230))
    leaves.setFillColor('darkGreen') # Gunakan 'darkGreen' (huruf kapital G)
    leaves.setBorderWidth(0)
    leaves.setDepth(44)
    tree_layer.add(leaves)

    # Daun tambahan (Circle)
    leaves1 = Circle(80, Point(position[0], position[1] - 175))
    leaves1.setFillColor('darkGreen')
    leaves1.setBorderWidth(0)
    leaves1.setDepth(44)
    tree_layer.add(leaves1)
    tree_layer.setDepth(40)
    return tree_layer

# --- Menggunakan Fungsi make_tree ---
# Buat pohon di posisi (170, 600)
tree = make_tree(position=(170, 600))
canvas.add(tree)

# Buat pohon kedua di posisi (850, 600) jika ingin
# tree2 = make_tree(position=(850, 600))
# canvas.add(tree2)

# --- Menambahkan Sinar Matahari ---
def add_sun_rays(center_x, center_y, radius, num_rays=8, ray_length=30, color="orange"):
    """Menambahkan sinar matahari sebagai Path dari Point."""
    rays = []
    for i in range(num_rays):
        angle_deg = i * 360 / num_rays
        angle_rad = math.radians(angle_deg)

        # Titik awal dan akhir untuk setiap sinar
        x_start = center_x + radius * math.cos(angle_rad)
        y_start = center_y - radius * math.sin(angle_rad)  # - karena Y meningkat ke bawah
        x_end = center_x + (radius + ray_length) * math.cos(angle_rad)
        y_end = center_y - (radius + ray_length) * math.sin(angle_rad)

        # Buat Path dengan dua Point: awal dan akhir
        ray = Path([Point(x_start, y_start), Point(x_end, y_end)])
        ray.setBorderColor(color)
        ray.setBorderWidth(3)
        ray.setDepth(38)  # Di atas matahari
        rays.append(ray)
        canvas.add(ray)
    return rays

# Tambahkan sinar matahari
sun_rays = add_sun_rays(80, 80, sun_radius, num_rays=8, ray_length=30, color="orange")

# --- Menambahkan Gunung ---
def make_mountain(base_width, height, position, color="brown"):
    """Membuat gunung sederhana menggunakan Polygon (segitiga)."""
    mountain = Polygon(
        Point(position[0] - base_width // 2, position[1] + height),  # Kaki kiri
        Point(position[0], position[1]),  # Puncak
        Point(position[0] + base_width // 2, position[1] + height)  # Kaki kanan
    )
    mountain.setFillColor(color)
    mountain.setBorderColor("black")
    mountain.setDepth(45)  # Di atas tanah, di bawah awan
    return mountain

# Gunung pertama (kiri)
mountain1 = make_mountain(base_width=350, height=300, position=(200, 150), color="saddlebrown")
canvas.add(mountain1)

# Gunung kedua (kanan)
mountain2 = make_mountain(base_width=180, height=120, position=(800, 330), color="brown")
canvas.add(mountain2)

# Membuat dan menambahkan awan pertama
cloud1_layer = Layer()
for offset in [(-20, 0), (0, -15), (20, 0)]:  # Menggunakan loop untuk membuat bagian awan
    part = Ellipse(40, 20)
    part.move(200 + offset[0], 100 + offset[1])  # Posisi awan 1
    part.setFillColor("white")
    part.setBorderColor("lightgray")
    cloud1_layer.add(part)
canvas.add(cloud1_layer)

# Membuat dan menambahkan awan kedua
cloud2_layer = Layer()
for offset in [(-20, 0), (0, -15), (20, 0)]:
    part = Ellipse(60, 30)
    part.move(400 + offset[0], 150 + offset[1])  # Posisi awan 2
    part.setFillColor("white")
    part.setBorderColor("lightgray")
    cloud2_layer.add(part)
canvas.add(cloud2_layer)

# Membuat dan menambahkan awan ketiga
cloud3_layer = Layer()
for offset in [(-20, 0), (0, -15), (20, 0)]:
    part = Ellipse(50, 20)
    part.move(600 + offset[0], 120 + offset[1])  # Posisi awan 3
    part.setFillColor("white")
    part.setBorderColor("lightgray")
    cloud3_layer.add(part)
canvas.add(cloud3_layer)

# Membuat dan menambahkan awan keempat
cloud4_layer = Layer()
for offset in [(-20, 0), (0, -15), (20, 0)]:
    part = Ellipse(45, 25)
    part.move(800 + offset[0], 150 + offset[1])  # Posisi awan 4
    part.setFillColor("white")
    part.setBorderColor("lightgray")
    cloud4_layer.add(part)
canvas.add(cloud4_layer)

# --- Fungsi untuk Membuat Hewan (diperbarui untuk menghadap kiri) ---

def make_goat(color="white", position=(0, 550)):
    """Membuat kambing sebagai Layer, menghadap ke kiri."""
    goat_layer = Layer()

    # Tubuh (posisi tubuh adalah titik referensi utama)
    body = Ellipse(60, 30, Point(position[0], position[1]))
    body.setFillColor(color)
    body.setBorderColor("black")
    body.setDepth(42)
    goat_layer.add(body)

    # Kepala (ditempatkan di sisi kiri tubuh untuk menghadap kiri)
    head = Circle(12, Point(position[0] - 30, position[1] - 10))
    head.setFillColor(color)
    head.setBorderColor("black")
    head.setDepth(41)
    goat_layer.add(head)

    # Telinga
    ear1 = Ellipse(8, 15, Point(position[0] - 35, position[1] - 20))
    ear1.setFillColor(color)
    ear1.setBorderColor("black")
    ear1.setDepth(40)
    ear2 = Ellipse(8, 15, Point(position[0] - 25, position[1] - 20))
    ear2.setFillColor(color)
    ear2.setBorderColor("black")
    ear2.setDepth(40)
    goat_layer.add(ear1)
    goat_layer.add(ear2)

    # Mata
    eye = Circle(3, Point(position[0] - 33, position[1] - 12))
    eye.setFillColor("black")
    eye.setDepth(39)
    goat_layer.add(eye)

    # Kaki
    leg1 = Rectangle(5, 20, Point(position[0] + 15, position[1] + 20))
    leg1.setFillColor(color)
    leg1.setBorderColor("black")
    leg1.setDepth(43)
    leg2 = Rectangle(5, 20, Point(position[0] - 15, position[1] + 20))
    leg2.setFillColor(color)
    leg2.setBorderColor("black")
    leg2.setDepth(43)
    leg3 = Rectangle(5, 20, Point(position[0] + 5, position[1] + 20))
    leg3.setFillColor(color)
    leg3.setBorderColor("black")
    leg3.setDepth(43)
    leg4 = Rectangle(5, 20, Point(position[0] - 25, position[1] + 20))
    leg4.setFillColor(color)
    leg4.setBorderColor("black")
    leg4.setDepth(43)
    goat_layer.add(leg1)
    goat_layer.add(leg2)
    goat_layer.add(leg3)
    goat_layer.add(leg4)

    # Ekor (sederhana, di sisi kanan tubuh)
    tail = Path([Point(position[0] + 30, position[1]), Point(position[0] + 40, position[1] - 10)])
    tail.setBorderColor("black")
    tail.setBorderWidth(2)
    tail.setDepth(43)
    goat_layer.add(tail)

    return goat_layer

def make_chicken(color="yellow", position=(0, 550)): # Warna diubah ke kuning
    """Membuat ayam sebagai Layer, menghadap ke kiri."""
    chicken_layer = Layer()

    # Tubuh
    body = Ellipse(40, 25, Point(position[0], position[1]))
    body.setFillColor(color)
    body.setBorderColor("black")
    body.setDepth(42)
    chicken_layer.add(body)

    # Kepala (ditempatkan di sisi kiri tubuh)
    head = Circle(10, Point(position[0] - 20, position[1] - 8))
    head.setFillColor(color)
    head.setBorderColor("black")
    head.setDepth(41)
    chicken_layer.add(head)

    # Paruh
    beak = Polygon(Point(position[0] - 28, position[1] - 8), Point(position[0] - 35, position[1] - 5), Point(position[0] - 28, position[1] - 2))
    beak.setFillColor("orange")
    beak.setBorderColor("orange")
    beak.setDepth(40)
    chicken_layer.add(beak)

    # Mata
    eye = Circle(2, Point(position[0] - 23, position[1] - 10))
    eye.setFillColor("white")
    eye.setDepth(39)
    pupil = Circle(1, Point(position[0] - 23, position[1] - 10))
    pupil.setFillColor("black")
    pupil.setDepth(38)
    chicken_layer.add(eye)
    chicken_layer.add(pupil)

    # Kaki
    leg1 = Rectangle(3, 15, Point(position[0] + 10, position[1] + 15))
    leg1.setFillColor("orange")
    leg1.setBorderColor("orange")
    leg1.setDepth(43)
    leg2 = Rectangle(3, 15, Point(position[0] - 10, position[1] + 15))
    leg2.setFillColor("orange")
    leg2.setBorderColor("orange")
    leg2.setDepth(43)
    chicken_layer.add(leg1)
    chicken_layer.add(leg2)

    # Ekor
    tail = Ellipse(20, 15, Point(position[0] + 20, position[1]))
    tail.setFillColor(color)
    tail.setBorderColor("black")
    tail.setDepth(43)
    chicken_layer.add(tail)

    return chicken_layer

# --- Main Execution ---
# Tampilkan scene awal selama 5 detik
print("Menampilkan scene awal...")
time.sleep(5)

# Tambahkan teks "On a sunny day"
sunny_text = Text("On a sunny day", 20)
sunny_text.move(500, 100)
sunny_text.setDepth(15) # Di atas elemen lain
canvas.add(sunny_text)

# Tunggu teks tampil selama 3 detik
print("Menampilkan teks 'On a sunny day'...")
time.sleep(3)

# Hapus teks
canvas.remove(sunny_text)
print("Teks 'On a sunny day' dihilangkan.")

# --- Animasi Hewan ---
print("Memasukkan hewan...")

# Buat 2 kambing (masuk dari kanan, menghadap kiri)
goat1 = make_goat(color="white", position=(1100, 550)) # Mulai dari luar kanan canvas
goat2 = make_goat(color="white", position=(1150, 570)) # Mulai dari luar kanan canvas, posisi sedikit berbeda
canvas.add(goat1)
canvas.add(goat2)

# Animasi kambing berjalan masuk selama 5 detik
print("Kambing berjalan masuk dari kanan...")
for _ in range(50): # 25 langkah dalam 5 detik (5 detik / 0.2 detik per langkah)
    goat1.move(-10, 0) # Gerak 10 pixel ke kiri
    goat2.move(-10, 0)
    time.sleep(0.2)

# Setelah berjalan masuk, geser kambing lebih ke kiri (ke tengah) agar tidak terlalu di pojok
print("Geser kambing lebih ke tengah...")
goat1.move(-20, 0) # Geser 100 pixel ke kiri
goat2.move(-20, 0)
time.sleep(1) # Jeda sebentar untuk melihat perubahan

# Animasi kambing makan rumput selama 10 detik
print("Kambing mulai makan rumput...")
for _ in range(20): # 20 iterasi dalam 10 detik (10 detik / 0.5 detik per iterasi)
    # Simulasikan gerakan kepala naik-turun untuk kambing
    goat1.move(0, 5) # Kepala turun (pindahkan layer kambing sedikit)
    goat2.move(0, 5)
    time.sleep(0.25)
    # Kepala naik (kembali ke posisi semula)
    goat1.move(0, -5)
    goat2.move(0, -5)
    time.sleep(0.25)

print("Kambing selesai makan.")

# --- Ayam masuk setelah kambing selesai makan ---
print("Ayam masuk dengan loncat-loncat...")
# Buat 2 ayam (masuk dari kanan, menghadap kiri) setelah kambing selesai makan
chicken1 = make_chicken(color="yellow", position=(1200, 550)) # Mulai dari luar kanan canvas
chicken2 = make_chicken(color="yellow", position=(1250, 560)) # Mulai dari luar kanan canvas, posisi sedikit berbeda
canvas.add(chicken1)
canvas.add(chicken2)

# Animasi ayam masuk dengan loncat-loncat selama 5 detik
for _ in range(30): # 25 langkah dalam 5 detik
    chicken1.move(-10, 0) # Gerak ke kiri
    chicken2.move(-10, 0)
    # Simulasikan loncatan sederhana dengan menggerakkan ke atas-bawah cepat
    # Naik
    chicken1.move(0, -5)
    chicken2.move(0, -5)
    time.sleep(0.1)
    # Turun
    chicken1.move(0, 5)
    chicken2.move(0, 5)
    time.sleep(0.1)

# Setelah ayam masuk, geser ayam lebih ke kiri (ke tengah) agar berada di depan kambing dan tidak terlalu di pojok
print("Geser ayam lebih ke tengah...")
chicken1.move(-50, 0) # Geser 150 pixel ke kiri
chicken2.move(-50, 0)
time.sleep(1) # Jeda sebentar

print("Ayam berhenti di depan kambing (ayam lebih kiri).")

# Menunggu interaksi pengguna sebelum menutup (opsional)
# canvas.wait()
# canvas.close()

print("Program selesai.")