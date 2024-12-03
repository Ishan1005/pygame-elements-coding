import pygame
import sys

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont('Arial', 36)

def draw_shapes():
    pygame.draw.polygon(screen, RED, [(400, 100), (350, 200), (450, 200)])
    pygame.draw.polygon(screen, BLUE, [(300, 400), (500, 400), (500, 500), (300, 500)])
    pygame.draw.polygon(screen, GREEN, [(600, 300), (650, 350), (625, 425), (575, 425), (550, 350)])

def show_text(text, color, position):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    draw_shapes()

    show_text("Welcome to My Game!", BLACK, (250, 50))
    show_text("Red Triangle, Blue Rectangle, Green Pentagon", BLACK, (150, 500))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()