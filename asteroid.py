from vpython import *
import random

# Pengaturan canvas untuk fullscreen
scene.width = 1500  # Lebar layar (sesuaikan dengan resolusi layar)
scene.height = 725  # Tinggi layar
scene.fullscreen = True  # Aktifkan mode fullscreen

# Fungsi untuk membuat asteroid kecil tak beraturan
def create_asteroid():
    parts = []  # Daftar untuk menyimpan bagian asteroid
    for _ in range(10):  # Buat 10 bagian acak
        # Buat sphere kecil dengan posisi acak di sekitar pusat asteroid
        part = sphere(pos=vector(random.uniform(-0.3, 0.3),
                                 random.uniform(-0.3, 0.3),
                                 random.uniform(-0.3, 0.3)),
                      radius=random.uniform(0.1, 0.2),
                      color=vector(0.5, 0.5, 0.5))
        parts.append(part)
    return compound(parts)  # Gabungkan semua bagian menjadi satu objek

# Fungsi untuk membuat asteroid besar tak beraturan
def create_asteroid_besar():
    parts = []  # Daftar untuk menyimpan bagian asteroid
    for _ in range(10):  # Buat 10 bagian acak
        # Buat sphere kecil dengan posisi acak di sekitar pusat asteroid
        part = sphere(pos=vector(random.uniform(-0.9, 0.9),
                                 random.uniform(-0.9, 0.9),
                                 random.uniform(-0.9, 0.9)),
                      radius=random.uniform(0.1, 0.5),
                      color=vector(0.5, 0.5, 0.5))
        parts.append(part)
    return compound(parts)  # Gabungkan semua bagian menjadi satu objek

# Buat asteroid
asteroid = create_asteroid()
asteroid2 = create_asteroid()
asteroid3 = create_asteroid()
asteroid4 = create_asteroid_besar()
asteroid5 = create_asteroid()
asteroid6 = create_asteroid()
asteroid7 = create_asteroid()
asteroid.pos = vector(-60, 10, 0)
asteroid2.pos = vector(-60, 8, 5)
asteroid3.pos = vector(-60, 13, 4)
asteroid4.pos = vector(-70, 17, -3)
asteroid5.pos = vector(-60, 15, -1)
asteroid6.pos = vector(-65, 10, -3)
asteroid7.pos = vector(-60, 6, -3)

# Variabel untuk animasi
angle = 0 # untuk titik awal semua planet berada di posisi x = 0
asteroid_velocity = vector(0.1, 0.01, 0)  # Kecepatan translasi asteroid

while True:
    rate(60)  # 60 frame per detik

    # Translasi asteroid
    asteroid.pos += asteroid_velocity
    asteroid2.pos += asteroid_velocity
    asteroid3.pos += asteroid_velocity
    asteroid4.pos += asteroid_velocity
    asteroid5.pos += asteroid_velocity
    asteroid6.pos += asteroid_velocity
    asteroid7.pos += asteroid_velocity

    # Rotasi asteroid pada sumbu acak
    asteroid.rotate(angle=0.05, axis=vector(0.5, 1, 0.3).norm(), origin=asteroid.pos)
    asteroid2.rotate(angle=0.05, axis=vector(0.5, 1, 0.3).norm(), origin=asteroid2.pos)
    asteroid3.rotate(angle=0.05, axis=vector(0.5, 1, 0.3).norm(), origin=asteroid3.pos)
    asteroid4.rotate(angle=0.05, axis=vector(0.5, 1, 0.3).norm(), origin=asteroid4.pos)
    asteroid5.rotate(angle=0.05, axis=vector(0.5, 1, 0.3).norm(), origin=asteroid5.pos)
    asteroid6.rotate(angle=0.05, axis=vector(0.5, 1, 0.3).norm(), origin=asteroid6.pos)
    asteroid7.rotate(angle=0.05, axis=vector(0.5, 1, 0.3).norm(), origin=asteroid7.pos)

    # Kembalikan asteroid ke posisi awal jika keluar dari bidang pandang
    if asteroid4.pos.x > 40:
        asteroid.pos = vector(-60, 10, 0)
        asteroid2.pos = vector(-60, 8, 10)
        asteroid3.pos = vector(-60, 13, 4)
        asteroid4.pos = vector(-70, 17, -3)
        asteroid5.pos = vector(-60, 15, -1)
        asteroid6.pos = vector(-65, 10, -3)
        asteroid7.pos = vector(-60, 6, -3)