import pygame

pygame.init()
width, height = 600, 680
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

size = 40
pygame.display.set_caption("Pacman-Plus")

# Colors:
BLACK = (0, 0 , 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

collision_walls = []

for row in range(width):
    collision_walls.append(pygame.Rect(row, 0, 20, 20))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()