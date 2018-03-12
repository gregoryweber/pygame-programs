import pygame

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT]) #the screen

running = True
while running:
	pygame.display.flip()
	for event in pygame.event.get(): #goes through all the events in pygame
		if event.type == pygame.QUIT: #if one of those events is a quit, then quit
			running = False