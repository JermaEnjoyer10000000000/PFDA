import pygame

# 1. Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

running = True
while running:
    # 2. Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. Fill the background
    screen.fill((255, 255, 255)) # White

    # 4. Draw Circles
    # Draw a filled Blue circle (width=0)
    pygame.draw.circle(screen, (0, 0, 255), (100, 150), 50)

    # Draw a hollow Red circle with 5px border thickness
    pygame.draw.circle(screen, (255, 0, 0), (300, 150), 50, width=5)

    # 5. Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
