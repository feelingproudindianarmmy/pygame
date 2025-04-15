import pygame
pygame.init()
screen = pygame.display.set_mode((400,300))
done = False

while not done:

# Clear the event queue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
pygame.display.flip()
