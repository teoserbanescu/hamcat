#0 - nothing 1 - wall 2 - lever 3 - score bar 4 - door 5 - hole 6 - blackhole 7 - chest 8 - sugar

import pygame, sys
import random
#from moving import *
#import drunkie

from pygame.locals import *

m = [
		[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
		[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 2],
		[0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
		[0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
		[1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
		[0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
		[5, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
		[0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
		[0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
		[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
		[0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
		[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]
	]

holesx = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		]
holesy = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		]
colors = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		]

m1 = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
weapons = [
		[]
		]
others = [
		[]	
		]
pygame.mixer.pre_init(44100, 16, 2, 2048)
pygame.init()
pygame.display.init()
pygame.font.init()
#LEVEL 1

L = 60
nrcat = 0

def drawWall(i, j, ind):
	screen.blit(bricks[ind], (60*i, 60*j))
def drawSugar(i, j):
	screen.blit(sugar, (60*i, 60*j))
creditsfont = pygame.font.SysFont("monospace", 15, True, True)
font = pygame.font.SysFont("monospace", 55, True, True)
bigfont = pygame.font.SysFont("monospace", 75, True, True)
question = pygame.image.load("bar/question.png")
question = pygame.transform.scale(question, (L, L))
menu = pygame.image.load("bar/menu.png")
menu = pygame.transform.scale(menu, (L, L))
pause = pygame.image.load("bar/pause.png")
pause = pygame.transform.scale(pause, (L, L))
play = pygame.image.load("bar/play.png")
play = pygame.transform.scale(play, (L, L))
sound_on = pygame.image.load("bar/sound_on.png")
sound_on = pygame.transform.scale(sound_on, (L, L))
sound_off = pygame.image.load("bar/sound_off.png")
sound_off = pygame.transform.scale(sound_off, (L, L))
restart = pygame.image.load("bar/restart.png")
restart = pygame.transform.scale(restart, (L, L))
#settings = pygame.image.load("settings.png")
#settings = pygame.transform.scale(settings, (L, L))


ak_width = 6 * L
ak_height = 3 * L
arrow_keys = pygame.image.load("help/arrow_keys.png")
arrow_keys = pygame.transform.scale(arrow_keys, (ak_width, ak_height))
sk_width = 8 * L
sk_height = 2 * L
space_key = pygame.image.load("help/space_key.png")
space_key = pygame.transform.scale(space_key, (sk_width, sk_height))
disco_width = 6 * L
disco_height = 4 * L
disco_globe = pygame.image.load("help/disco.png")
disco_globe = pygame.transform.scale(disco_globe, (disco_width, disco_height))


fundal1 = pygame.image.load("background/fundal1.jpg")
fundal1 = pygame.transform.scale(fundal1, (1320, 960))

fundal2 = pygame.image.load("background/fundal2.jpg")
fundal2 = pygame.transform.scale(fundal2, (1320, 480))

"""fundal3 = pygame.image.load("fundal3.jpg")
fundal3 = pygame.transform.scale(fundal3, (720, 480))
fundal3 = pygame.transform.rotate(fundal3, 180)
"""
world = pygame.Rect((0, 0), (1320, 960))
clock = pygame.time.Clock()

screen = pygame.display.set_mode(world.size)
pygame.display.set_caption("Lazy hamcat")

music = True
pygame.mixer.music.load("music/M.O.O.N.-Crystals.mp3")
pygame.mixer.music.play(3)

paused = False
help = False

key = False

Key = pygame.image.load("help/key.png").convert_alpha()
Key = pygame.transform.scale(Key, (L, L))

Key1 = pygame.image.load("bar/menu_key.png").convert_alpha()
Key1 = pygame.transform.scale(Key1, (L, L))

keyloops = 0

key_warning = False
keywindow = pygame.Surface((1020, 600), pygame.SRCALPHA, 32)
keywindow.fill((200, 50, 255, 200))
bigkey = pygame.transform.scale(Key, (300, 420))

ok_button = pygame.image.load("help/ok_button.png").convert_alpha()
ok_button = pygame.transform.scale(ok_button, (240, 120))

snore = pygame.mixer.Sound("music/silly_snoring.wav")

#doors m 4
doorx1 = 11
doory1 = 12
door1 = False
m[doory1][doorx1] = 4

door_oriz = pygame.Surface((L, L // 6))
door_oriz.fill(pygame.Color("brown"))

door_verti = pygame.Surface((L // 6, L))
door_verti.fill(pygame.Color("brown"))

door_open = pygame.mixer.Sound("music/door-open.wav")
door_closed = pygame.mixer.Sound("music/door-close.wav")

#lever wall disappear

switch_lever = pygame.mixer.Sound("music/switch_lever.wav")

lever_off = pygame.image.load("objects/lever_off.png").convert_alpha()
lever_off = pygame.transform.scale(lever_off, (L, L))

lever_on = pygame.image.load("objects/lever_on.png").convert_alpha()
lever_on = pygame.transform.scale(lever_on, (L, L))

attention = pygame.Surface((L, L), pygame.SRCALPHA, 32)
attention.fill((200, 50, 255, 200))

lever = False

leverloops = 0

#tick = pygame.mixer.Sound("tick.mp3")

lx = 21
ly = 1

m[ly][lx] = 2

#false wall
fx = 16
fy = 8


#treasure m 7
chestx = 4
chesty = 12
chest = pygame.image.load("objects/treasure.png").convert_alpha()
chest = pygame.transform.scale(chest, (L, L))
m[chesty][chestx] = 7

#holes usual 5 final 6
hole = pygame.image.load("objects/hole6.png").convert_alpha()
hole = pygame.transform.scale(hole, (L, L))
holex1 = 0
holey1 = 6
holex2 = 12
holey2 = 14

holesx[holey1][holex1] = holex2
holesy[holey1][holex1] = holey2

holesx[holey2][holex2] = holex1
holesy[holey2][holex2] = holey1

m[holey1][holex1] = 5
m[holey2][holex2] = 5
hole_change = pygame.mixer.Sound("music/whip_plop.wav")
changing = False

#final hole
surprisehole = pygame.image.load("objects/hole2.png").convert_alpha()
surprisehole = pygame.transform.scale(surprisehole, (L, L))
finalx = 21
finaly = 9
m[finaly][finalx] = 6

#instructions dimensions
hx = 0
hy = L

score_background = pygame.image.load("background/ScoreBackground.jpg")
score_background = pygame.transform.scale(score_background, (L, L))

#brick walls

bricks = []
def append_bricks(brick):
	brick1 = pygame.image.load(brick).convert()
	bricks.append(pygame.transform.scale((brick1), (L, L)))

append_bricks("background/red_brick.jpg")
append_bricks("background/green_brick.jpg")
append_bricks("background/purple_brick.jpg")

#disco mode
disco = pygame.image.load("bar/disco.png").convert_alpha()
disco = pygame.transform.scale(disco, (L, L))
disco_mode = False
i = 0
while i < 16:
	j = 0
	while j < 22:
		if m[i][j] == 1:
			colors[i][j] = random.randint(0, 1)
		j += 1
	i +=1


#targets

sugar = pygame.image.load("mobs/hamilton1.png").convert_alpha()
sugar = pygame.transform.scale(sugar, (L, L))

wows = []

wow1 = pygame.image.load("help/wow1.png").convert_alpha()
wow1 = pygame.transform.scale(wow1, (L, L))
wows.append(wow1)

wow2 = pygame.image.load("help/wow2.png").convert_alpha()
wow2 = pygame.transform.scale(wow2, (L, L))
wows.append(wow2)

wow3 = pygame.image.load("help/wow3.png").convert_alpha()
wow3 = pygame.transform.scale(wow3, (L, L))
wows.append(wow3)

ham = []
Rham = []

def append_positions(direction):
	ham1 = pygame.image.load(direction).convert_alpha()
	ham.append(pygame.transform.scale(ham1, (L, L)))
	Rham.append(ham1.get_rect(top = L, left = 0))

append_positions("cat/hamcat1_right.png")
append_positions("cat/hamcat1_left.png")
append_positions("cat/hamcat4down1.png")
append_positions("cat/hamcat4up1.png")


dx = 0
dy = 1

start_time = 15
frame_count_lever = 0
frame_rate = 15

frame_count_target = 0
#wow
wx = 0
wy = 0

#target m 8

#sus stanga
tx = random.randint(0, 11)
ty = random.randint(1, 7)
while (tx == dx and ty == dy) or m[ty][tx] != 0 :
	tx = random.randint(0, 11)
	ty = random.randint(1, 7)
m[ty][tx] = 8

#sus dreapta
tx = random.randint(12, 21)
ty = random.randint(1, 7)
while (tx == dx and ty == dy) or m[ty][tx] != 0 :
	tx = random.randint(12, 21)
	ty = random.randint(1, 7)
m[ty][tx] = 8

#jos stanga
tx = random.randint(0, 10)
ty = random.randint(8, 15)
while (tx == dx and ty == dy) or m[ty][tx] != 0 :
	tx = random.randint(0, 10)
	ty = random.randint(8, 15)
m[ty][tx] = 8

#jos dreapta
tx = random.randint(12, 21)
ty = random.randint(8, 15)
while (tx == dx and ty == dy) or m[ty][tx] != 0 or (tx <= 16 and ty == 9) or (tx == 12 and ty <= 12):
	tx = random.randint(12, 21)
	ty = random.randint(8, 15)
m[ty][tx] = 8

energy_count = 0

#KEY

kx = random.randint(0, 21)
ky = random.randint(1, 7)
while (kx == dx and ky == dy) or m[ky][kx] != 0:
	kx = random.randint(0, 21)
	ky = random.randint(1, 7)

#can hamcat fly?
haswings = False
fall = pygame.mixer.Sound("music/fall.wav")

scor = 0
wow = wows[random.randint(0, 2)]

level1 = True

#Energy

life = 3

hamlife = pygame.image.load("bar/hamlife.png").convert_alpha()
hamlife = pygame.transform.scale(hamlife, (L, L))

hamlifegone = pygame.image.load("bar/hamlifegone.png").convert_alpha()
hamlifegone = pygame.transform.scale(hamlifegone, (L, L))

battery = []
energy = 4
def append_battery(bat):
	bat1 = pygame.image.load(bat).convert_alpha()
	battery.append(pygame.transform.scale(bat1, (L, L)))

append_battery("bar/battery1.png")
append_battery("bar/battery2.png")
append_battery("bar/battery3.png")
append_battery("bar/battery4.png")
append_battery("bar/battery5.png")

frame_count_energy = 0

frame_count_sleep = 0
sleeping = False
sleep = pygame.image.load("cat/sleep.png").convert_alpha()
sleep = pygame.transform.scale(sleep, (L, L))

#mobs

mob1 = pygame.image.load("mobs/shell1left.png").convert_alpha()
mob1 = pygame.transform.scale(mob1, (L, L))
mx = 21
my = 6

m[my][mx] = 9

#pearl

pearl = pygame.image.load("mobs/pearl.png").convert_alpha()
pearl = pygame.transform.scale(pearl, (L // 2, L // 2))

frame_count_pearl = 0
frame_count_hurt = 0
gata = False

pearlx = 20 * L + L // 2
pearly = 6 * L + L // 4


# 0 - dreapta 1 - stanga 2 - jos 3 - sus

#LEVEL 2

px = 0
py = 3

L1 = 120

wings = []
Rwings = []

def append_wings(thewings):
    wingspic = pygame.image.load(thewings).convert_alpha()
    wings.append(pygame.transform.scale(wingspic, (L1, L1)))
    Rwings.append(wingspic.get_rect(top = 3 * L1, left = 0))    

append_wings("animations/wings1.png")
append_wings("animations/wings2.png")
append_wings("animations/wings3.png")
append_wings("animations/wings4.png")
append_wings("animations/wings5.png")
append_wings("animations/wings6.png")
append_wings("animations/wings7.png")
append_wings("animations/wings8.png")
append_wings("animations/wings9.png")
append_wings("animations/wings10.png")
append_wings("animations/wings11.png")
append_wings("animations/wings12.png")
append_wings("animations/wings13.png")

nrwings = 0

blackholes = []

def append_blackholes(hole):
    hole1 = pygame.image.load(hole).convert_alpha()
    blackholes.append(pygame.transform.scale(hole1, (4 * L1, 900)))

append_blackholes("objects/blh2.png")
append_blackholes("objects/blh1.png")
append_blackholes("objects/blh0.png")

nrblackholes = 0

frame_count_space = 0

paused = False

bx = 1320
screenWidth = 1320


back = pygame.image.load("background/nightbackground.jpg").convert_alpha()
back = pygame.transform.scale(back, (1320, 960))
back2 = pygame.image.load("background/nightbackground.jpg").convert_alpha()
back2 = pygame.transform.scale(back2, (1320, 960))

level2 = False


#LOST GAME!!!
lostwindow = pygame.Surface((world.width, world.height - L), pygame.SRCALPHA, 32)
lostwindow.fill((200, 50, 255, 200))

cry = pygame.image.load("cat/cry.png").convert_alpha()
cry = pygame.transform.scale(cry, (480, 480))

playagain = pygame.image.load("help/replay.png").convert_alpha()
playagain = pygame.transform.scale(playagain, (240, 240))
quitgame = pygame.image.load("help/exit.png").convert_alpha()
quitgame = pygame.transform.scale(quitgame, (240, 240))
lost = False

gameover = pygame.image.load("help/gameover.png").convert_alpha()
gameover = pygame.transform.scale(gameover, (660, 240))

#wings screen

wing_warning = False
wingwindow = pygame.Surface((1020, 600), pygame.SRCALPHA, 32)
wingwindow.fill((200, 50, 255, 200))

wing = []
Rwing = []

def append_wing(thewing):
    wingpic = pygame.image.load(thewing).convert_alpha()
    wing.append(pygame.transform.scale(wingpic, (300, 420)))
    Rwing.append(wingpic.get_rect(top = 270, left = 510))    

append_wing("animations/wing1.png")
append_wing("animations/wing2.png")
append_wing("animations/wing3.png")
append_wing("animations/wing4.png")
append_wing("animations/wing5.png")
append_wing("animations/wing6.png")
append_wing("animations/wing7.png")
append_wing("animations/wing8.png")
append_wing("animations/wing9.png")
append_wing("animations/wing10.png")
append_wing("animations/wing11.png")
append_wing("animations/wing12.png")
append_wing("animations/wing13.png")

nrwing = 0

aripioare = pygame.image.load("bar/wing3.png").convert_alpha()
aripioare = pygame.transform.scale(aripioare, (L, L))

#drawing
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			a = pygame.mouse.get_pos()
			x = a[0]
			y = a[1]
			if (x <= L) and (y <= L):
				disco_mode = not disco_mode
			if (x >= world.width - 3 * L) and (x <= world.width - 2 * L) and (y <= L):
				music = not music
			#restart game
			if (x >= world.width - 4 * L) and (x <= world.width - 3 * L) and (y <= L):
				life = 3
				gata = False
				energy = 4
				key_warning = False
				wing_warning = False
				nrwing = 0
				lost = False
				scor = 0
				key = False
				haswings = False
				lever = False
				level1 = True
				level2 = False
				paused = False
				haswings = False
				for hamcat in Rham:
					hamcat.move_ip(-hamcat.left, -hamcat.top + 60)
				dx = 0
				dy = 1
				frame_count_pearl = 0
				frame_count_space = 0
				frame_countDoor = 0
				frame_count_lever = 0
				frame_count_target = 0
				m[fy][fx] = 1
				total_seconds = 0

				i = 0
				while i <= 15:
					j = 0
					while j <= 21:
						if m[i][j] == 8:
							m[i][j] = 0
						j+=1
					i +=1

				#sus stanga
				tx = random.randint(0, 11)
				ty = random.randint(1, 7)
				while (tx == dx and ty == dy) or m[ty][tx] != 0 :
					tx = random.randint(0, 11)
					ty = random.randint(1, 7)
				m[ty][tx] = 8

				#sus dreapta
				tx = random.randint(12, 21)
				ty = random.randint(1, 7)
				while (tx == dx and ty == dy) or m[ty][tx] != 0 :
					tx = random.randint(12, 21)
					ty = random.randint(1, 7)
				m[ty][tx] = 8

				#jos stanga
				tx = random.randint(0, 10)
				ty = random.randint(8, 15)
				while (tx == dx and ty == dy) or m[ty][tx] != 0 :
					tx = random.randint(0, 10)
					ty = random.randint(8, 15)
				m[ty][tx] = 8

				#jos dreapta
				tx = random.randint(12, 21)
				ty = random.randint(8, 15)
				while (tx == dx and ty == dy) or m[ty][tx] != 0 or (tx <= 16 and ty == 9) or (tx == 12 and ty <= 12):
					tx = random.randint(12, 21)
					ty = random.randint(8, 15)
				m[ty][tx] = 8


				#key
				kx = random.randint(0, 21)
				ky = random.randint(1, 7)
				while (kx == dx and ky == dy) or m[ky][kx] != 0:
					kx = random.randint(0, 21)
					ky = random.randint(1, 7)
			if lost:
				if x >= 300 and x <=540 and y >= 660 and y <= 900:
					print "next"
					m[fy][fx] = 1
					life = 3
					energy = 4
					lost = False
					scor = 0
					key = False
					haswings = False
					lever = False
					level1 = True
					level2 = False
					paused = False
					for hamcat in Rham:
						hamcat.move_ip(-hamcat.left, -hamcat.top + 60)
					dx = 0
					dy = 1
					frame_count_pearl = 0
					frame_count_space = 0
					frame_countDoor = 0
					frame_count_lever = 0
					frame_count_target = 0
				if x >= 780 and x <= 1020 and y>= 660 and y <= 900:
					pygame.quit()
					sys.exit()
			elif key_warning or wing_warning:
				if x >= 540 and x <= 780 and y >= 660 and y <= 780:
					key_warning = False
					wing_warning = False
					nrwing = 0
					paused = False
			else:
				if (x >= world.width - 2 * L) and (x <= world.width - L) and (y <= L):
					paused = not paused
					help = False
				if (x >= world.width - L) and (y <= L):
					help = True
					paused = True
	if level1:
		#screen.fill(pygame.Color("magenta"))
		screen.blit(fundal1, (0, 0))
		screen.blit(fundal2, (0, 480))
		#screen.blit(fundal3, (720, 480))
	if level1:

		#score bar
		i = 0
		while i < 22:
			screen.blit(score_background, (L * i, 0))
			i += 1

		#movement

		pressed = pygame.key.get_pressed()

		if key_warning or wing_warning:
			print "wingwarning"
			if pressed[pygame.K_RETURN]:
				key_warning = False
				wing_warning = False
				nrwing = 0
				paused = False

		if not paused and not sleeping:
			if not changing:
				change_count = 0
				#pressed = pygame.key.get_pressed()
				if key_warning or wing_warning:
					print "avertizare"
					if pressed[pygame.K_RETURN]:
						key_warning = False
						wing_warning = False
						nrwing = 0
						paused = False
				if dy < 15 and pressed[pygame.K_DOWN]:
					nrcat = 2
					if m[dy + 1][dx] == 6:
						level2 = True
						level1 = False
						dy += 1
						for hamcat in Rham:
							hamcat.move_ip(L, 0)
					else:
						if m[dy + 1][dx] == 5:
							mutx = holesx[dy + 1][dx]
							muty = holesy[dy + 1][dx]
							for hamcat in Rham: 
								hamcat.move_ip((mutx - dx) * L, (muty - dy) * L)
							dx = mutx
							dy = muty
							changing = True
							hole_change.play()
						else: 
							if m[dy + 1][dx] == 0 or m[dy + 1][dx] == 8:
								for hamcat in Rham:
									hamcat.move_ip(0, L)
								dy += 1

				if dy > 0 and pressed[pygame.K_UP]:
					nrcat = 3
					if m[dy - 1][dx] == 6:
						level2 = True
						level1 = False
						dy -= 1
						for hamcat in Rham:
							hamcat.move_ip(L, 0)
					else:
						if m[dy - 1][dx] == 5:
							mutx = holesx[dy - 1][dx]
							muty = holesy[dy - 1][dx]
							for hamcat in Rham: 
								hamcat.move_ip((mutx - dx) * L, (muty - dy) * L)
							dx = mutx
							dy = muty
							changing = True
							hole_change.play()
						else:
							if m[dy - 1][dx] == 0 or m[dy - 1][dx] == 8:
								for hamcat in Rham:
									hamcat.move_ip(0, -L)
								dy -= 1
				if dx > 0 and pressed[pygame.K_LEFT]:
					nrcat = 1
					if m[dy][dx - 1] == 6:
						level2 = True
						level1 = False
						dx -= 1
						for hamcat in Rham:
							hamcat.move_ip(L, 0)
					else:
						if m[dy][dx - 1] == 5:
							mutx = holesx[dy][dx - 1]
							muty = holesy[dy][dx - 1]
							for hamcat in Rham: 
								hamcat.move_ip((mutx - dx) * L, (muty - dy) * L)
							dx = mutx
							dy = muty
							changing = True
							hole_change.play()
						else: 
							if m[dy][dx - 1] == 0 or m[dy][dx - 1] == 8:
								for hamcat in Rham:
									hamcat.move_ip(-L, 0)
								dx -= 1
				if dx < 21 and pressed[pygame.K_RIGHT]:
					nrcat = 0
					if m[dy][dx + 1] == 6:
						level2 = True
						level1 = False
						dx += 1
						for hamcat in Rham:
							hamcat.move_ip(L, 0)
					else:
						if m[dy][dx + 1] == 5:
							mutx = holesx[dy][dx + 1]
							muty = holesy[dy][dx + 1]
							for hamcat in Rham: 
								hamcat.move_ip((mutx - dx) * L, (muty - dy) * L)
							dx = mutx
							dy = muty
							changing = True
							hole_change.play()
						else: 
							if m[dy][dx + 1] == 0 or m[dy][dx + 1] == 8:
								for hamcat in Rham:
									hamcat.move_ip(L, 0)
								dx += 1

				if pressed[pygame.K_SPACE]:
					if nrcat == 0 and dx < 21:
						if m[dy][dx + 1] == 2:
							lever = not lever
							switch_lever.play()
							m[fy][fx] = not m[fy][fx]
						if m[dy][dx + 1] == 4:
							frame_countDoor = 0
							door1 = not door1
							m[doory1][doorx1] = 0
					if nrcat == 1 and dx > 0:
						if m[dy][dx - 1] == 2:
							lever = not lever
							switch_lever.play()
							m[fy][fx] = not m[fy][fx]
						if m[dy][dx - 1] == 4:
							frame_countDoor = 0
							door1 = not door1
							m[doory1][doorx1] = 0
					if nrcat == 2 and dy < 15:
						if m[dy + 1][dx] == 2:
							lever = not lever
							switch_lever.play()
							m[fy][fx] = not m[fy][fx]
						if m[dy + 1][dx] == 4:
							frame_countDoor = 0
							door1 = not door1
							m[doory1][doorx1] = 0
					if nrcat == 3 and dy > 1:
						if m[dy - 1][dx] == 2:
							lever = not lever
							switch_lever.play()
							m[fy][fx] = not m[fy][fx]
						if m[dy - 1][dx] == 4:
							frame_countDoor = 0
							door1 = not door1
							m[doory1][doorx1] = 0
						if m[dy-1][dx] == 7:
							if key:
								haswings = True
								print "haswings"
								wing_warning = True
								paused = True
								#show wings
							else:
								#key warning
								key_warning = True
								paused = True	
				#Rham[nrcat].clamp_ip(world)
				if m[dy][dx] == 8:
					energy += 1
					m[dy][dx] = 0
					frame_count_target = 0
					scor += 50
					wow = wows[random.randint(0, 2)]
					wx = dx
					wy = dy
					if dy < 8:
						if dx < 12:
							tx = random.randint(0, 11)
							ty = random.randint(1, 7)
							while (tx == dx and ty == dy) or m[ty][tx] != 0:
								tx = random.randint(0, 11)
								ty = random.randint(1, 7)
						else:
							tx = random.randint(12, 21)
							ty = random.randint(1, 7)
							while (tx == dx and ty == dy) or m[ty][tx] != 0:
								tx = random.randint(12, 21)
								ty = random.randint(1, 7)
					else:
						if dx < 11:
							tx = random.randint(0, 10)
							ty = random.randint(8, 15)
							while (tx == dx and ty == dy) or m[ty][tx] != 0:
								tx = random.randint(0, 10)
								ty = random.randint(8, 15)
						else:
							tx = random.randint(12, 21)
							ty = random.randint(8, 15)
							while (tx == dx and ty == dy) or m[ty][tx] != 0 or (tx <= 16 and ty == 9) or (tx == 12 and ty <= 12):
								tx = random.randint(12, 21)
								ty = random.randint(8, 15)
					m[ty][tx] = 8

				#frame_count_lever += 1
			else:
				change_count += 1
				if change_count == 10:
					changing = False

		#lever
		if lever:
			leverloops += 1
			if leverloops == 1:
				frame_count_lever = 0
			screen.blit(lever_on, (lx * L, ly * L + L // 2))
		else:
			leverloops = 0
			screen.blit(lever_off, (lx * L, ly * L))

		#chest
		screen.blit(chest, (chestx * L, chesty * L))


		#show doors
		if not door1:
			screen.blit (door_verti, (doorx1 * L + (L - L // 6) // 2, doory1 * L))
		else:
			frame_countDoor += 1
			if frame_countDoor == 1:
				door_open.play()
			total_secondsDoor = frame_countDoor // frame_rate
			if total_secondsDoor < 1:
				screen.blit(door_oriz, ((doorx1 - 1) * L, doory1 * L))
			else:
				door1 = False
				m[doory1][doorx1] = 4
				door_closed.play()
				screen.blit(door_verti, (doorx1 * L + (L - L // 6) // 2, doory1 * L))

		#holes
		screen.blit(hole, (holex1 * L, holey1 * L))
		screen.blit(hole, (holex2 * L, holey2 * L))
		
		#key to collect
		if not key:
				screen.blit(Key,(kx * L, ky * L))
				if dx == kx and dy == ky:
					key = True
		
		#surprise hole
		screen.blit(surprisehole, (finalx * L, finaly * L))
		
		#labyrinth
		i = 0
		while i < 22:
			j = 0
			while j < 16:
				if m[j][i] == 1:
					if not disco_mode:
						drawWall(i, j, len(bricks) - 1)
					else:
						drawWall(i, j, random.randint(0, 2))
				j += 1
			i += 1
		
		#mobs
		screen.blit(mob1, (mx * L, my * L))

		#pearl
		frame_count_pearl += 1
		frame_count_hurt += 1
		if frame_count_pearl <= 14:
			pearlx -= L // 2
		#print pearlx // L
		if frame_count_pearl == 30:
			frame_count_pearl = 0
			pearlx = 20 * L + L // 2
			gata = False
		if m[pearly // L][pearlx // L] == 1:
			print frame_count_pearl
			pearlx = 20 * L + L // 2
			gata = True
		if (pearly // L == dy) and (pearlx // L == dx):
			if life > 0 and frame_count_hurt >= 15:
				print pearlx // L
				print dx
				frame_count_hurt = 0
				life -= 1
			gata = True
		if not gata:
			screen.blit(pearl, (pearlx, pearly))

		if life == 0:
			lost = True
			paused = True
			message1 = bigfont.render("Shells are evil", 1, (255, 255, 255))
			message2 = bigfont.render("   creatures   ", 1, (255, 255, 255))

		#poor hamcat
		if sleeping:
			screen.blit(sleep, (dx * L, dy * L))
			if changing:
				lost = True
				paused = True
				message1 = bigfont.render(" Sleeping underground", 1, (255, 255, 255))
				message2 = bigfont.render("is not a very good idea", 1, (255, 255, 255))
		elif not changing:
			screen.blit(ham[nrcat], Rham[nrcat])
		#target

		i = 0
		while i < 22:
			j = 0
			while j < 16:
				if m[j][i] == 8:
					drawSugar(i,j)
				j += 1
			i += 1
		#screen.blit(sugar, (tx*L, ty*L))

		if not paused:
			frame_count_lever += 1
		#timer
		if lever:
			total_seconds_lever = frame_count_lever // frame_rate
			if total_seconds_lever < 2 or total_seconds_lever > 87:
				if (frame_count_lever % 5) < 3:
					screen.blit(attention, (fx * L, fy * L))

			
			total_seconds = start_time - (frame_count_lever // frame_rate)
			if total_seconds < 0:
				total_seconds = 0
				lever  = False
				m[fy][fx] = 1
				if dx <= fx and dy >= fy:
					lost = True
					paused = True
					message1 = bigfont.render("You are trapped", 1, (255, 255, 255))
					message2 = bigfont.render(" in this room!", 1, (255, 255, 255))
					#GAME OVER
			minutes = total_seconds // 60
			seconds = total_seconds % 60
			timing = "Time:{0:02}:{1:02}".format(minutes,seconds)

			timp = font.render(timing, True, pygame.Color("white"))
			screen.blit(timp, (9 * L, 0))
		#wow
		frame_count_target += 1
		total_seconds_target = frame_count_target // frame_rate
		if scor > 0:
			if total_seconds_target < 2:
				if (frame_count_target % 5) < 3:
					screen.blit(wow, (wx * L, wy * L))
	if level2:
		#print bx
		if frame_count_space == 0:
			py = 3
		screen.blit(back, (bx - screenWidth, 0))
		screen.blit(back2,(bx, 0))
		if haswings:
			if not paused:
				pressed = pygame.key.get_pressed()
				if pressed[pygame.K_DOWN]:
					if py < 7:
						py += 0.5
						for wing in Rwings:
							wing.move_ip(0, L1/2)
				if pressed[pygame.K_UP]:
					if py > 0.5:
						py -= 0.5
						for wing in Rwings:
							wing.move_ip(0, -L1/2)
				if pressed[pygame.K_LEFT]:
					if px > 0:
						px -= 0.5
						for wing in Rwings:
							wing.move_ip(-L1/2, 0)
				if pressed[pygame.K_RIGHT]:
					if px < 10:
						px += 0.5
						for wing in Rwings:
							wing.move_ip(L1/2, 0)
			nrwings += 1
			if nrwings > 12:
				nrwings = 0
		else:
			if not lost:
				if frame_count_space == 0:
					fall.play()
					Rham[2].move_ip(-screenWidth + L, 0)
				Rham[2].move_ip(0, L1/4)
				py += 0.25
				if py > 7:
					paused = True
					lost = True
					message1 = bigfont.render("Sorry, Hamcats cannot", 1, (255, 255, 255))
					message2 = bigfont.render(" fly without wings", 1, (255, 255, 255))

		if frame_count_space < 200:
			if not paused:
				bx -= 3
		else:
			blackhole = blackholes[nrblackholes]
			if frame_count_space % 2 == 0:
			  	nrblackholes += 1
			if nrblackholes > 2 :
				nrblackholes = 0
			screen.blit(blackhole, (world.width - 4 * L1, L1))

		if haswings:
			screen.blit(wings[nrwings], Rwings[nrwings])
		else:
			screen.blit(ham[2], Rham[2])
		if bx <= 0:
			bx = screenWidth

		#score bar
		i = 0
		while i < 22:
			screen.blit(score_background, (L * i, 0))
			i += 1

		if not paused:
			frame_count_space += 1
	    #print frame_count_space

	#text, menu bar, credits

	"""#score bar
				i = 0
				while i < 22:
					screen.blit(score_background, (L * i, 0))
					i += 1"""
	if level1:
		level = "Level 1"
	else:
		level = "Level 2"
	score = font.render(level, True, pygame.Color("white"))
	screen.blit(score, (60, 0))

	if key and not haswings and not level2: 
		#keyloops += 1
		screen.blit(Key1, (world.width - 6 * L, 0))
		"""if keyloops == 1:
									pygame.mixer.music.fadeout(5000)
									snore.play()"""
	if haswings and not level2:
		screen.blit(aripioare, (world.width - 6 * L, 0))


	screen.blit(restart, (world.width - 4 * L, 0))

	#Energy
	if not paused and not level2 and not sleeping:
		frame_count_energy += 1
		if frame_count_energy % 90 == 0:
			energy -= 1
		nrbat = energy
		if nrbat > 4:
			nrbat = 4
		if nrbat < 0:
			nrbat = 0

		if nrbat == 0:
			sleeping = True
	if sleeping:
		frame_count_sleep += 1
		if frame_count_sleep == 1:
			snore.play()
		if frame_count_sleep >= 105:
			energy = 4
			sleeping = False
			frame_count_sleep = 0 
	if not level2:
		screen.blit(battery[nrbat],(world.width - 5 * L, 0))

	if music:
		screen.blit(sound_on, (world.width - 3 * L, 0))
		pygame.mixer.music.unpause()
	else:
		screen.blit(sound_off, (world.width - 3 * L, 0))
		pygame.mixer.music.pause()
	if paused:
		screen.blit(play, (world.width - 2 * L, 0))
	else:
		screen.blit(pause, (world.width - 2 * L, 0))

	screen.blit(question, (world.width - L, 0))
	
	if help:
		instructions = pygame.Surface((world.width, world.height - L), pygame.SRCALPHA, 32)
		instructions.fill((200, 50, 255, 200))
		screen.blit(instructions, (hx, hy))
		screen.blit(arrow_keys, (hx, hy))
		inst1 = font.render("To move your avatar,", 1, (255, 255, 255))
		screen.blit(inst1, (hx + 9 * L, hy))
		inst1 = font.render(" use the arrow keys", 1, (255, 255, 255))
		screen.blit(inst1, (hx + 9 * L, hy + L)) 
		screen.blit(space_key, (hx, hy + 4 * L))
		inst2 = font.render("To open doors, chests,", 1, (255, 255, 255))
		screen.blit(inst2, (hx + 9 * L, hy + 3 * L))
		inst3 = font.render(" switch levers, press", 1, (255, 255, 255))
		screen.blit(inst3, (hx + 9 * L, hy + 4 * L))
		inst4 = font.render("     the spacebar", 1, (255, 255, 255))
		screen.blit(inst4, (hx + 9 * L, hy + 5 * L))
		screen.blit(disco_globe, (hx, hy + 7 * L))
		inst5 = font.render("To activate disco mode,", 1, (255, 255, 255))
		screen.blit(inst5, (hx + 9 * L, hy + 7 * L))
		inst6 = font.render(" click the disco ball", 1, (255, 255, 255))
		screen.blit(inst6, (hx + 9 * L, hy + 8 * L))
	if lost:
		screen.blit(lostwindow, (0, 60))
		screen.blit(cry, (840, 120))
		screen.blit(playagain, (300, 660))
		screen.blit(quitgame, (780, 660))
		screen.blit(gameover, (120, 120))
		"""message1 = bigfont.render("Sorry, Hamcats cannot", 1, (255, 255, 255))
								message2 = bigfont.render(" fly without wings", 1, (255, 255, 255))"""
		screen.blit(message1, (120, 420))
		screen.blit(message2, (120, 540))
	if key_warning:
		screen.blit(keywindow, (150, 210))
		screen.blit(ok_button, (540, 660))
		screen.blit(bigkey, (780, 270))
		message1 = bigfont.render("You must have", 1, (255, 255, 255))
		message2 = bigfont.render("a key to open", 1, (255, 255, 255))
		message3 = bigfont.render("  the chest", 1, (255, 255, 255))
		screen.blit(message1, (180, 300))
		screen.blit(message2, (180, 420))
		screen.blit(message3, (180, 540))

	# nrwing += 1
	# if nrwing > 12:
	# 	nrwing = 0
	# screen.blit(wing[nrwing], Rwing[nrwing])
	# print nrwing

	#screen.blit(wing[8], Rwing[8])

	if wing_warning:
		screen.blit(wingwindow, (150, 210))
		screen.blit(ok_button,(540, 660))
		nrwing += 1
		if nrwing > 12:
			nrwing = 0
		print nrwing
		screen.blit(wing[nrwing],Rwing[nrwing])
		message1 = bigfont.render("Yay! You can fly now!", 1, (255, 255, 255))
		screen.blit(message1, (180, 240))

	for k in range(0, life):
		screen.blit(hamlife, ((5 + k) * L, 0))
	k = life
	while k < 3:
		screen.blit(hamlifegone, ((5 + k) * L, 0))
		k += 1

	#credits
	credits = creditsfont.render("Copyrighted by", 1, (255, 255, 255))
	screen.blit(credits, (world.width - 5 * L / 2, world.height - L));
	credits = creditsfont.render("Denise 'Dee' Chavez", 1, (255, 255, 255))
	screen.blit(credits, (world.width - 3 * L, world.height - L / 2));
	

	
	#for k in (life, 3):
	#	screen.blit(hamlifegone, ((5 + k) * L, 0))
	#screen.blit(hamlife, (5 * L, 0))
	#screen.blit(hamlife, (6 * L, 0))
	#screen.blit(hamlife, (7 * L, 0))

	screen.blit(disco, (0, 0))
	clock.tick(frame_rate)
	pygame.display.flip()
