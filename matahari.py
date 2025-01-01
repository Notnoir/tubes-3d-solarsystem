from vpython import *
import random

# Buat Matahari
sun = sphere(pos=vector(0, 0, 0), radius=2, color=color.yellow)

# Buat efek sinar Matahari (lapisan aura)
aura = sphere(
    pos=sun.pos,
    radius=3,  # Radius lebih besar dari Matahari
    color=color.yellow,
    opacity=0.25,  # Transparansi untuk efek cahaya
)

# Variabel untuk transformasi skala
scale_factor = 0.005  # Kecepatan perubahan skala
max_scale = 1.5  # Skala maksimum
min_scale = 1.0  # Skala minimum
current_scale = 1.0 
scaling_up = True

# label untuk Matahari
label(pos=sun.pos + vector(0, 4.5, 0), text="Sun", height=20, box=False, color=color.white)

# Variabel untuk animasi
angle = 0

while True:
    rate(60)  # 60 frame per detik

    # Efek transformasi skala pada aura matahari
    if scaling_up:
        current_scale += scale_factor
        if current_scale >= max_scale:
            scaling_up = False
    else:
        current_scale -= scale_factor
        if current_scale <= min_scale:
            scaling_up = True

    # Terapkan transformasi skala ke aura matahari
    aura.radius = sun.radius * current_scale