# My_pyagme_project
#This is basic arcade space game  which is made by using pygame module in python.
#module import 

import pygame

import random

import math

from pygame import mixer

pygame.init()

#window_setup

window=pygame.display.set_mode((1080,2340))

#image_load

image=pygame.image.load("space-invaders.png")

x=500

t=True

y=1880

x_change=0

#enemy

e_image=[]

e_x=[]

e_y=[]

e_x_change=[]

e_y_change=[]

n_enemies=6

for i in range (n_enemies):

	e_image.append(pygame.image.load("a.png"))

	e_x.append(random.randint(0,900))

	e_y.append(random.randint(0,200))

	e_x_change.append(5)

	e_y_change.append(40)

#bullets_image_load

b_image=pygame.image.load("bullets.png")

b_x=0

b_y=1800

b_x_change=0

b_y_change=10

bullet_state="ready"

#background_image_load

background=pygame.image.load("Bg.jpg")

mixer.music.load("Backmusic.mp3")

mixer.music.play(-1)

def rocket(x,y):

	window.blit(image,(x,y))

	

def e_rocket(a,b,i):

	window.blit(e_image[i],(a,b))

	

	

def b_fire(x,y):

	global bullet_state

	bullet_state="fire"

	window.blit(b_image,(x,y))

	

	

def iscollision(a,b,b_x,b_y):

	distance=math.sqrt(math.pow(a-b_x,2)+math.pow(b-b_y,2))

	if distance<25:

		return True

	else:

		return False

#score

score_value=0

font=pygame.font.Font("freesansbold.ttf",32)

t_x=50

t_y=50

def show_score(x,y):

	score=font.render("SCORE : "+str(score_value),True,(255,255,255))

	window.blit(score,(x,y))

	

	

run=True

while run:

	window.fill((0,0,0))

	window.blit(background,(0,0))

	for event in pygame.event.get():

		if event.type==pygame.QUIT:

			run=False

		if event.type==pygame.KEYDOWN:

			if event.type==pygame.K_RIGHT:

				x_change=3

			if event.type==pygame.K_LEFT:

				x_change=-3

		if event.type==pygame.K_SPACE:

					if bullet_state == "fire":

						b_x=x

						b_fire(b_x,b_y)

		if event.type==pygame.KEYUP:

			if event.type==pygame.K_RIGHT or event.type==pygame.K_LEFT:

				x_change=0

	x+=x_change

	if x<=0:

			x=0

	if x>=900:

			x=900

	

	for i in range (n_enemies):

			if e_y[i]>400:

				for j in range(n_enemies):

					e_y[j]=2340

				game_over_text()

				break

				

			e_x[i]+=e_x_change[i]

			if e_x[i]<=0:

				e_x_change[i]=4

				e_y[i]+=e_y_change[i]

			elif e_x[i]>=900:

				e_x_change[i]=-4

				e_y[i]+=e_y_change[i]

			collision=iscollision(e_x[i],e_y[i],b_x,b_y)

			if collision:

				b_y=1900

				bullet_state="ready"

				score_value+=1

				e_x[i]=random.randint(0,900)

				e_y[i]=random.randint(0,900)

				s1=mixer.Sound("Collide.wav")

				s1.play()

			e_rocket(e_x[i],e_y[i],i)

			

	if b_y<=0:

		b_y=1900

		bullet_state="ready"

		

	if bullet_state == "fire":

		b_fire(b_x,b_y)

		b_y-=b_y_change

	rocket(x,y)

	s=mixer.Sound("Bulletgo.wav")

	s.play()

	if t==False:

		game_over_text()

		break

	

	show_score(t_x,t_y)

	pygame.display.update()
