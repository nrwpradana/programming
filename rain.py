from cs1graphics import *
from time import sleep

# --- Konfigurasi Canvas ---
canvas = Canvas(800, 600)
canvas.setBackgroundColor('white')
canvas.setTitle('Animasi Hujan')


# --- Fungsi Buat Satu Tetesan Hujan ---
def create_raindrop(x, y):
    layer = Layer()

    # Batang hujan: garis vertikal dari (x, y) ke (x, y+30)
    stem = Path(Point(x, y), Point(x, y + 30))
    stem.setBorderColor('lightBlue')
    stem.setBorderWidth(2)

    # Kepala tetesan: oval kecil di bawah batang
    head = Ellipse(6, 4, Point(x, y + 32))  # Lebar=6, tinggi=4
    head.setFillColor('lightBlue')
    head.setBorderColor('lightBlue')

    layer.add(stem)
    layer.add(head)
    return layer


# --- Buat Banyak Tetesan ---
drops = []
cols = 15
rows = 5
spacing_x = 50
spacing_y = 60

for r in range(rows):
    for c in range(cols):
        start_x = 30 + c * spacing_x
        start_y = 20 + r * spacing_y
        drop = create_raindrop(start_x, start_y)
        canvas.add(drop)
        drops.append(drop)

# --- Animasi Jatuh Terus-Menerus ---
while True:  # Loop tak berujung
    for d in drops:
        d.move(0, 15)  # Jatuh 15 piksel ke bawah

        # Periksa apakah tetesan sudah keluar dari layar
        # Ambil titik referensi (center) dari layer
        ref_point = d.getReferencePoint()
        if ref_point.getY() > 600:  # Jika pusat tetesan sudah di bawah layar (y > 600)
            # Pindahkan kembali ke atas, dengan posisi acak sedikit untuk efek alami
            new_y = -30  # Mulai dari atas layar (atau sedikit di atas)
            new_x = ref_point.getX()  # Pertahankan posisi x-nya
            d.moveTo(new_x, new_y)

    sleep(0.05)  # Tunggu sebentar untuk efek animasi halus