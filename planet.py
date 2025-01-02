from vpython import *
import random

# Pengaturan canvas untuk fullscreen
scene.width = 1500  # Lebar layar (sesuaikan dengan resolusi layar)
scene.height = 725  # Tinggi layar
scene.fullscreen = True  # Aktifkan mode fullscreen

# Buat Matahari
sun = sphere(pos=vector(0, 0, 0), radius=2, texture="sunmap.jpg")

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

# Fungsi untuk membuat orbit putus-putus
def create_dashed_orbit(radius, color, segments=100, gap_ratio=0.5):
    orbit = []
    for i in range(segments):
        angle_start = 2 * pi * i / segments
        angle_end = 2 * pi * (i + (1 - gap_ratio)) / segments
        start = vector(radius * cos(angle_start), 0, radius * sin(angle_start))
        end = vector(radius * cos(angle_end), 0, radius * sin(angle_end))
        orbit.append(curve(pos=[start, end], color=color, radius=0.02))
    return orbit

# Orbit planet (putus-putus)
orbit_merkurius = create_dashed_orbit(radius=5, color=color.white)
orbit_venus = create_dashed_orbit(radius=9, color=color.white)
orbit_bumi = create_dashed_orbit(radius=13, color=color.white)
orbit_mars = create_dashed_orbit(radius=17, color=color.white)
orbit_jupiter = create_dashed_orbit(radius=21, color=color.white)
orbit_saturnus = create_dashed_orbit(radius=25, color=color.white)
orbit_uranus = create_dashed_orbit(radius=29, color=color.white)
orbit_neptunus = create_dashed_orbit(radius=33, color=color.white)

# label untuk Matahari
label(pos=sun.pos + vector(0, 3.5, 0), text="Sun", height=20, box=False, color=color.white)

# Buat merkurius
merkurius = sphere(pos=vector(5, 0, 0), radius=0.2, texture="mercurymap.jpg")

# nama untuk merkurius
merkurius_label = label(pos=merkurius.pos + vector(0, 1.5, 0), text="merkurius", height=15, box=False, color=color.white)

# Buat venus
venus = sphere(pos=vector(9, 0, 0), radius=0.3, texture="venusmap.jpg")

# nama untuk venus
venus_label = label(pos=venus.pos + vector(0, 1.5, 0), text="venus", height=15, box=False, color=color.white)

# Buat bumi
bumi = sphere(pos=vector(13, 0, 0), radius=0.5, texture="earthmap1k.jpg")

# nama untuk bumi
bumi_label = label(pos=bumi.pos + vector(0, 1.5, 0), text="Earth", height=15, box=False, color=color.white)

# Buat mars
mars = sphere(pos=vector(17, 0, 0), radius=0.4, texture="marsmap1k.jpg")

# nama untuk mars
mars_label = label(pos=mars.pos + vector(0, 1.5, 0), text="Mars", height=15, box=False, color=color.white)

# Buat jupiter
jupiter = sphere(pos=vector(21, 0, 0), radius=1, texture="jupitermap.jpg")

# nama untuk jupiter
jupiter_label = label(pos=jupiter.pos + vector(0, 1.5, 0), text="jupiter", height=15, box=False, color=color.white)

# Buat saturnus
saturnus = sphere(pos=vector(25, 0, 0), radius=0.7, texture="saturnmap.jpg")

# Fungsi untuk membuat lapisan cincin saturnus
def create_ring(radius, thickness, texture):
    return ring(pos=saturnus.pos, axis=vector(0.2, 1, 0), radius=radius, thickness=thickness, texture=texture)

# Buat lapisan cincin saturnus
rings = [
    create_ring(radius=1.2, thickness=0.05, texture="saturnringcolor.jpg"),  # Cincin dalam
    create_ring(radius=1.3, thickness=0.07, texture="saturnringcolor.jpg"),  # Cincin tengah
    create_ring(radius=1.5, thickness=0.1, texture="saturnringcolor.jpg"),   # Cincin luar
]

# nama untuk saturnus
saturnus_label = label(pos=saturnus.pos + vector(0, 1.5, 0), text="saturnus", height=15, box=False, color=color.white)

# Buat uranus
uranus = sphere(pos=vector(29, 0, 0), radius=0.6, texture="uranusmap.jpg")

# nama untuk uranus
uranus_label = label(pos=uranus.pos + vector(0, 1.5, 0), text="uranus", height=15, box=False, color=color.white)

# Buat neptunus
neptunus = sphere(pos=vector(33, 0, 0), radius=0.4, texture="neptunemap.jpg")

# nama untuk neptunus
neptunus_label = label(pos=neptunus.pos + vector(0, 1.5, 0), text="neptunus", height=15, box=False, color=color.white)

# Variabel untuk animasi
angle = 0 # untuk titik awal semua planet berada di posisi x = 0

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

    # rotasi sun di sumbu sendiri
    sun.rotate(angle=radians(0.5), axis=vector(0, 1, 0), origin=sun.pos)

    # Rotasi planet-planet di sumbu sendiri
    merkurius.rotate(angle=0.05, axis=vector(0, 1, 0), origin=merkurius.pos)
    venus.rotate(angle=0.04, axis=vector(0, 1, 0), origin=venus.pos)
    bumi.rotate(angle=0.03, axis=vector(0, 1, 0), origin=bumi.pos)
    mars.rotate(angle=0.02, axis=vector(0, 1, 0), origin=mars.pos)
    jupiter.rotate(angle=0.015, axis=vector(0, 1, 0), origin=jupiter.pos)
    saturnus.rotate(angle=0.01, axis=vector(0, 1, 0), origin=saturnus.pos)
    uranus.rotate(angle=0.009, axis=vector(0, 1, 0), origin=uranus.pos)
    neptunus.rotate(angle=0.008, axis=vector(0, 1, 0), origin=neptunus.pos)

    # Rotasi planet mengelilingi matahari (revolusi)
    merkurius.pos = rotate(merkurius.pos, angle=0.01, axis=vector(0, 1, 0))
    venus.pos = rotate(venus.pos, angle=0.008, axis=vector(0, 1, 0))
    bumi.pos = rotate(bumi.pos, angle=0.006, axis=vector(0, 1, 0))
    mars.pos = rotate(mars.pos, angle=0.004, axis=vector(0, 1, 0))
    jupiter.pos = rotate(jupiter.pos, angle=0.002, axis=vector(0, 1, 0))
    saturnus.pos = rotate(saturnus.pos, angle=0.0015, axis=vector(0, 1, 0))
    uranus.pos = rotate(uranus.pos, angle=0.001, axis=vector(0, 1, 0))
    neptunus.pos = rotate(neptunus.pos, angle=0.0008, axis=vector(0, 1, 0))

    # Perbarui posisi cincin untuk mengikuti Saturnus
    for ring_layer in rings:
        ring_layer.pos = saturnus.pos
        ring_layer.rotate(angle=0.005, axis=vector(0.2, 1, 0), origin=ring_layer.pos)

    # posisi label merkurius agar mengikuti merkurius
    merkurius_label.pos = merkurius.pos + vector(0, 1.5, 0)

    # posisi label venus agar mengikuti venus
    venus_label.pos = venus.pos + vector(0, 1.5, 0)

    # posisi label bumi agar mengikuti bumi
    bumi_label.pos = bumi.pos + vector(0, 1.5, 0)

    # posisi label mars agar mengikuti mars
    mars_label.pos = mars.pos + vector(0, 1.5, 0)

    # posisi label jupiter agar mengikuti jupiter
    jupiter_label.pos = jupiter.pos + vector(0, 1.5, 0)

    # posisi label saturnus agar mengikuti saturnus
    saturnus_label.pos = saturnus.pos + vector(0, 1.5, 0)

    # posisi label uranus agar mengikuti uranus
    uranus_label.pos = uranus.pos + vector(0, 1.5, 0)

    # posisi label neptunus agar mengikuti neptunus
    neptunus_label.pos = neptunus.pos + vector(0, 1.5, 0)