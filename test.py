import pydialog
import pygame

WIDTH = 640
HEIGHT = 480
FPS = 60
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("test")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pydialog.alert("Hello, world!", pydialog.WARNING, pydialog.YES_NO):
                    print("YES!")
                else:
                    print("noooooo")
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    pygame.display.flip()       

pygame.quit()