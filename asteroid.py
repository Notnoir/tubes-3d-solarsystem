from vpython import *
import random

# Fungsi untuk membuat asteroid tak beraturan
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

# Buat asteroid
asteroid = create_asteroid()
asteroid2 = create_asteroid()
asteroid3 = create_asteroid()
asteroid.pos = vector(-20, 0, 0)
asteroid2.pos = vector(-20, 0, 5)
asteroid3.pos = vector(-20, 5, 7)

# Variabel untuk animasi
angle = 0
asteroid_velocity = vector(0.1, 0.01, 0)  # Kecepatan translasi asteroid

while True:
    rate(60)  # 60 frame per detik

    # Translasi asteroid
    asteroid.pos += asteroid_velocity
    asteroid2.pos += asteroid_velocity
    asteroid3.pos += asteroid_velocity

    # Rotasi asteroid pada sumbu acak
    asteroid.rotate(angle=0.05, axis=vector(0.5, 1, 0.3).norm(), origin=asteroid.pos)
    asteroid2.rotate(angle=0.05, axis=vector(0.5, 1, 0.3).norm(), origin=asteroid2.pos)
    asteroid3.rotate(angle=0.05, axis=vector(0.5, 1, 0.3).norm(), origin=asteroid3.pos)

    # Kembalikan asteroid ke posisi awal jika keluar dari bidang pandang
    if asteroid.pos.x > 20 and asteroid2.pos.x > 20 and asteroid3.pos.x > 20:
        asteroid.pos = vector(-20, 0, 0)
        asteroid2.pos = vector(-20, 0, 10)
        asteroid3.pos = vector(-20, -5, 0)