import pygame  
pygame.init()   
BLUE =(0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW=(255,255,0)
SIZE = (800, 600)
screen = pygame.display.set_mode(SIZE)
                             
pygame.draw.circle(screen, YELLOW, (250,250),60)
# Draw only one circle quadrant
pygame.draw.circle(screen, BLUE, (250, 250), 40, 0, draw_top_right=True)
pygame.draw.circle(screen, RED, (250, 250), 40, 30, draw_top_left=True)
pygame.draw.circle(screen, GREEN, (250, 250), 40, 20, draw_bottom_left=True)
pygame.draw.circle(screen, BLACK, (250, 250), 40, 10, draw_bottom_right=True)

pygame.display.flip()

# Game loop to keep the window open
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()