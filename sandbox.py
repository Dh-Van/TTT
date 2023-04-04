import pygame


pygame.init()
# Sets the screen size to 1000x1000
screen = pygame.display.set_mode((1000, 1000))
# Sets the window title to TTT-AI
pygame.display.set_caption("TTT-AI")

img = pygame.image.load('reset.png')
img.convert()

rect = img.get_rect()
rect.center = 100, 100

screen.fill("gray")
screen.blit(img, rect)
pygame.draw.rect(screen, "red", rect, 1)
# pygame.display.update()

run = True

# Main game loop
while run:
    # Loops through every event in the event queue
    for event in pygame.event.get():
        # Check if the event is of type QUIT
        if (event.type == pygame.QUIT):
            # If the event was of type QUIT, ends the main game loop
            run = False

        pygame.display.flip()
# Deactivates pygame
pygame.quit()