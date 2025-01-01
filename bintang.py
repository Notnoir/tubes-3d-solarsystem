from vpython import *
import random

# Pengaturan canvas untuk fullscreen
scene.width = 1500  # Lebar layar (sesuaikan dengan resolusi layar)
scene.height = 725  # Tinggi layar
scene.fullscreen = True  # Aktifkan mode fullscreen

def create_stars_with_reflection(num_stars=200):
    stars = []
    for _ in range(num_stars):
        # Bintang dengan posisi acak
        star_size = 0.1  # Ukuran acak untuk bintang
        x_pos = random.uniform(-50, 50)
        y_pos = random.uniform(-50, 50)
        z_pos = random.uniform(-50, 50)
        
        # Buat bintang pada posisi acak
        star = sphere(pos=vector(x_pos, y_pos, z_pos), radius=star_size, color=color.white, emissive=True)
        stars.append(star)

        # Refleksi bintang terhadap sumbu X
        reflected_star = sphere(pos=vector(-x_pos, y_pos, z_pos), radius=star_size, color=color.white, emissive=True)
        stars.append(reflected_star)
        
    return stars

# Buat bintang dengan refleksi
stars = create_stars_with_reflection(200)

# Variabel untuk animasi
angle = 0

while True:
    rate(60)  # 60 frame per detik