from ursina import *
import random
import time
import pyautogui

app = Ursina()

music = Audio(sound_file_name = "songs/Super Hang on music - Sprinter.mp3", autoplay = False, loop = True)

enemies = []
enemy1 = f"assets/Enemy_Car.glb"
enemy2 = f"assets/VW_Beetle.glb"
enemy3 = f"assets/Nissan_Tsuru.glb"
enemies.append(enemy1)
enemies.append(enemy2)
enemies.append(enemy3)

player = Entity(model = "assets/Jeep_Wrangler.glb", position = (0, 3, -2000), scale = 8, collider = "box", rotation = (0, 180, 0))
camera.z = -15
rows = [-15, -10, -5, 0, 5, 10, 15]
camera.add_script(SmoothFollow(target = player, offset = (-0.2, 2.5, -8)))
road = Entity(model = "plane", color = color.dark_gray, scale = (70, 10 , 1000000))
median_r = Entity(model = "cube", collider = "box", position = (25, 2, 0), scale = (5, 10, 1000000), color = color.white)
median_l = Entity(model = "cube", collider = "box", position = (-25, 2, 0), scale = (5, 10, 1000000), color = color.white)
speed = 200

for i in range (0, 100000, 300):
    enemy = Entity(model = random.choice(enemies), collider = "box", position = (random.choice(rows), 2.5, i), rotation = (0, 180, 0)) #, color = color.random_color())
    enemy.scale = 5

def update():
    player.z = player.z + time.dt * speed
    global rows
    if held_keys['d']:
        player.x = player.x + time.dt * 25
    if held_keys['a']:
        player.x = player.x - time.dt * 25

    if player.intersects().hit or median_r.intersects().hit or median_l.intersects().hit:
        music.stop()
        quit()

window.fullscreen = 1
Sky()

music.play()

app.run()
