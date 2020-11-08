import random
import pygame
import sys
from pygame.locals import *
#Defining game items
SCREENHEIGHT = 1280
SCREENWIDTH = 720
PLAYER = "gallery/sprites/bird.png"
PIPE = "gallery/sprites/pipe.png"
FPS = 60
BACKGROUND = "gallery/sprites/background.png"
GROUND = "gallery/sprites/base.png"
WELCOME = "gallery/sprites/message.png"
GAME_SPRITES = {}
GAME_SOUNDS = {}
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
#defining positions
GROUNDY = 1250
BACKGROUNDY = 0
BACKGROUNDX = 0

def welcomescreen():
	'''For welcome screen'''
	PLAYERX = int(SCREENWIDTH/5)
	PLAYERY = int((SCREENHEIGHT- GAME_SPRITES['player'].get_height())/2)
	WELCOMEX = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
	WELCOMEY = int((SCREENHEIGHT - GAME_SPRITES['message'].get_height())/2)
	GROUNDX = 0
	
	while True:
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			elif event.type==KEYDOWN and (event.key == K_SPACE):
				return
			else:
				SCREEN.blit(GAME_SPRITES["background"], (BACKGROUNDX, BACKGROUNDY))
				SCREEN.blit(GAME_SPRITES['message'], (WELCOMEX, WELCOMEY))
				SCREEN.blit(GAME_SPRITES['player'], (PLAYERX, PLAYERY))
				SCREEN.blit(GAME_SPRITES['base'], (GROUNDX, GROUNDY))
				pygame.display.update()
				FPSCLOCK.tick(FPS)

def maingame():
	"""function for starting maingame"""
	score = 0
	
	PLAYERX = int(SCREENWIDTH/5)
	PLAYERY = int((SCREENHEIGHT- GAME_SPRITES['player'].get_height())/2)
	GROUNDX = 0
	
	newPipe1 = getRandomPipe()
	newPipe2 = getRandomPipe()
	global upperPipes
	upperPipes = [
		{"x": SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
		{'x': (SCREENWIDTH +200) + (SCREENWIDTH/0.5), 'y': newPipe2[0]['y']}
	]
	global lowerPipes
	lowerPipes = [
		{'x': SCREENWIDTH +200, 'y': newPipe1[1]['y']},
		{'x': (SCREENWIDTH +200) +(SCREENWIDTH/0.5), 'y': newPipe2[1]['y']}
	]
	
	pipeVelX = -4
	playerVelY = -9
	playerMaxVelY = 10
	playerMinVelY = -8
	playerAccY = 1
	playerFlapAccVel = -8
	playerFlapped = False
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN and (event.key == K_SPACE):
				if PLAYERY > 0:
					playerVelY = playerFlapAccVel
					playerFlapped = True
					GAME_SOUNDS['wing'].play()
		
		crashTest = isCollide(PLAYERX, PLAYERY, upperPipes, lowerPipes) # This function will return true if the player is crashed
		if crashTest:
			return  
		
		playerMidPos = PLAYERX + GAME_SPRITES['player'].get_width()/2
		for pipe in upperPipes:
			pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
			if pipeMidPos <= playerMidPos < pipeMidPos + 4:
				score += 1
				print(f"Your score is {score}")
				GAME_SOUNDS['point'].play()
				
		if playerVelY <playerMaxVelY and not playerFlapped:
			playerVelY += playerAccY

		if playerFlapped:
			playerFlapped = False  
		playerHeight = GAME_SPRITES['player'].get_height()
		PLAYERY = PLAYERY + min(playerVelY, GROUNDY - PLAYERY - playerHeight)

		for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
			upperPipe['x'] += pipeVelX
			lowerPipe['x'] += pipeVelX
		
		if 0>upperPipes[0]['x']<5:
			newpipe = getRandomPipe()
			upperPipes.append(newpipe[0])
			lowerPipes.append(newpipe[1])
		if upperPipes[0]['x'] < -10:
			upperPipes.pop()
			lowerPipes.pop()
		
		SCREEN.blit(GAME_SPRITES['background'], (0,0))
		for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
			SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
			SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))
		SCREEN.blit(GAME_SPRITES['base'], (GROUNDX, GROUNDY))
		SCREEN.blit(GAME_SPRITES['player'], (PLAYERX, PLAYERY))
		myDigits = [int(x) for x in list(str(score))]
		width = 0
		for digit in myDigits:
			width += GAME_SPRITES['numbers'][digit].get_width()
			xOffSet = (SCREENWIDTH - width)/2
		
		for digit in myDigits:
			SCREEN.blit(GAME_SPRITES['numbers'][digit], (xOffSet, 100))
			xOffSet += GAME_SPRITES['numbers'][digit].get_width()
			pygame.display.update()
			FPSCLOCK.tick(FPS)
		
def isCollide(PLAYERX, PLAYERY, pipeX, pipeY):
	#checks the collision between player and pipes
	if (PLAYERY>GROUNDY) or (PLAYERY<0):
		GAME_SOUNDS['hit'].play()
		return True
		
	for pipe in upperPipes:
		pipeHeight = GAME_SPRITES['pipe'][0].get_height()
		if(PLAYERY < pipeHeight + pipe['y'] and abs(PLAYERX - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
			GAME_SOUNDS['hit'].play()
			return True

	for pipe in lowerPipes:
		if (PLAYERY + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(PLAYERX - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
			GAME_SOUNDS['hit'].play()
			return True
		
	return False
	
def getRandomPipe():
	pipeHeight = GAME_SPRITES['pipe'][0].get_height()
	pipeX = SCREENWIDTH +20
	offset = int(SCREENHEIGHT/3)
	y2 = random.randrange(400, SCREENHEIGHT - GAME_SPRITES['base'].get_height())
	y1 = y2 - pipeHeight - offset
	global pipes
	pipes = [
		{'x': pipeX, 'y': y1},
		{'x': pipeX , 'y': y2}
		]
	return pipes
	
	
if __name__ == '__main__':
	pygame.init()
	GAME_SPRITES['numbers'] = (
		pygame.image.load('gallery/sprites/0.png').convert_alpha(),
		pygame.image.load('gallery/sprites/1.png').convert_alpha(),
		pygame.image.load('gallery/sprites/2.png').convert_alpha(),
		pygame.image.load('gallery/sprites/3.png').convert_alpha(),
		pygame.image.load('gallery/sprites/4.png').convert_alpha(),
		pygame.image.load('gallery/sprites/5.png').convert_alpha(),
		pygame.image.load('gallery/sprites/6.png').convert_alpha(),
		pygame.image.load('gallery/sprites/7.png').convert_alpha(),
		pygame.image.load('gallery/sprites/8.png').convert_alpha(),
		pygame.image.load('gallery/sprites/9.png').convert_alpha()
	)
	FPSCLOCK = pygame.time.Clock()
	pygame.display.set_caption("Flappy Birds by Vishal Singh")
	GAME_SPRITES['player'] = (
		pygame.image.load(PLAYER).convert_alpha()
	)
	GAME_SPRITES['pipe'] = (
		pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
		pygame.image.load(PIPE).convert_alpha()
	)
	GAME_SPRITES['background'] = (
		pygame.image.load(BACKGROUND).convert()
		)
	GAME_SPRITES['base'] = (
		pygame.image.load(GROUND).convert_alpha()
		)
	GAME_SPRITES["message"] = pygame.image.load(WELCOME)
	
	GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
	GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
	GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
	GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
	GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')
	#Here the games starts
	while True:
		welcomescreen()
		maingame()