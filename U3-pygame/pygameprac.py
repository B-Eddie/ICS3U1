import math
import pygame  


pygame.init()   
BLUE =(0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW=(255,255,0)
SIZE = (800, 600)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode(SIZE)
screen.fill(WHITE)

pygame.draw.rect(screen, RED, (150, 100, 400, 300))
pygame.draw.rect(screen, BLACK, (175, 125, 350, 250))
pygame.draw.line(screen, YELLOW, (175, 125), (525, 375), 1)
pygame.draw.line(screen, YELLOW, (525, 125), (175, 375), 1)
pygame.draw.ellipse(screen, BLUE, (175, 125, 350, 250))


pygame.display.flip()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()