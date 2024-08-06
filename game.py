import pygame

pygame.init()
width, height = 600, 680
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

size = 40
pygame.display.set_caption("Pacman-Plus")

# Colors
BLACK = (0, 0 , 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

collision_walls = []
decorative_walls = []

# Walls that will be used for collision handling

# Outer Walls
for row in range(width - 30):
    collision_walls.append(pygame.Rect(row + 10, 10, 10, 10))
for row in range(width - 30):
    collision_walls.append(pygame.Rect(row + 10, height - 20, 10, 10))

for col in range(height - 30):
    collision_walls.append(pygame.Rect(10, col + 10, 10, 10))
for col in range(height - 30):
    collision_walls.append(pygame.Rect(width - 20, col + 10, 10, 10))
collision_walls.append(pygame.Rect(width/2 - 10, 10, 10, 80))
collision_walls.append(pygame.Rect(width/2 - 10, 580, 10, 80))

# Inner Walls

collision_walls.append(pygame.Rect(width/2 - 60, height/2 - 50, 110, 70))
collision_walls.append(pygame.Rect(width/3 - 60, 60, 110, 70))
collision_walls.append(pygame.Rect(width/2 + 40, 60, 110, 70))

collision_walls.append(pygame.Rect(width/3 - 60, 545, 110, 70))
collision_walls.append(pygame.Rect(width/2 + 40, 545, 110, 70))

collision_walls.append(pygame.Rect(width/3 - 140, 60, 40, 70))
collision_walls.append(pygame.Rect(width/2 + 195, 60, 40, 70))

collision_walls.append(pygame.Rect(width/3 - 140, 60, 40, 70))
collision_walls.append(pygame.Rect(width/2 + 195, 60, 40, 70))

collision_walls.append(pygame.Rect(width/3 - 140, 545, 40, 70))
collision_walls.append(pygame.Rect(width/2 + 195, 545, 40, 70))


# Walls used solely for aesthetic purposes

# Outer Walls
for row in range(width - 30):
    decorative_walls.append(pygame.Rect(row + 13, 13, 3.5, 3.5))
for row in range(width - 30):
    decorative_walls.append(pygame.Rect(row + 13, height - 17, 3.5, 3.5))
for col in range(height - 30):
    decorative_walls.append(pygame.Rect(13, col + 13, 3.5, 3.5))
for col in range(height - 30):
    decorative_walls.append(pygame.Rect(width - 17, col + 13, 3.5, 3.5))
decorative_walls.append(pygame.Rect(width/2 - 6, 15, 3.5, 72))
decorative_walls.append(pygame.Rect(width/2 - 6, 585, 3.5, 78))

# Inner Walls

decorative_walls.append(pygame.Rect(width/2 - 55, height/2 - 45, 100, 60))
decorative_walls.append(pygame.Rect(width/3 - 55, 65, 100, 60))
decorative_walls.append(pygame.Rect(width/2 + 45, 65, 100, 60))

decorative_walls.append(pygame.Rect(width/3 - 55, 550, 100, 60))
decorative_walls.append(pygame.Rect(width/2 + 45, 550, 100, 60))

decorative_walls.append(pygame.Rect(width/3 - 135, 65, 30, 60))
decorative_walls.append(pygame.Rect(width/2 + 200, 65, 30, 60))

decorative_walls.append(pygame.Rect(width/3 - 135, 550, 30, 60))
decorative_walls.append(pygame.Rect(width/2 + 200, 550, 30, 60))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for wall in collision_walls:
        pygame.draw.rect(screen, BLUE, wall)
    for wall in decorative_walls:
        pygame.draw.rect(screen, BLACK, wall)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()