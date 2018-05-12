import pygame
import winsound
import random
import time

done = False
pygame.init()
screen = pygame.display.set_mode((700, 700))
screen.fill((0, 0, 0))
clock = pygame.time.Clock()

class Tile:

    COLOR_RED = (255, 0, 0)
    COLOR_BLUE = (0, 0, 255)
    COLOR_YELLOW = (255, 255, 0)
    COLOR_GREEN = (0, 255, 0)

    def __init__(self, x, y, frequency, color, width=345, height=345):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.frequency = frequency
        self.color = color
        self.shape = None

    def draw(self):
        self.shape = pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def activate(self):
        self.flash()
        self.beep()

    def beep(self):
        winsound.Beep(self.frequency, 200)

    def flash(self):
        save_color = self.color
        self.color = (255, 255, 255)
        self.draw()
        pygame.display.update()
        pygame.time.wait(50)
        self.color = save_color
        self.draw()
        pygame.display.update()

    def collidepoint(self, pos):
        if self.shape.collidepoint(pos):
            self.activate()


tile_blue = Tile(0, 355, 200, Tile.COLOR_BLUE)
tile_blue.draw()
tile_red = Tile(0, 0, 473, Tile.COLOR_RED)
tile_red.draw()
tile_yellow = Tile(355, 355, 1385, Tile.COLOR_YELLOW)
tile_yellow.draw()
tile_green = Tile(355, 0, 941, Tile.COLOR_GREEN)
tile_green.draw()

while not done:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
             done = True
        if event.type is pygame.MOUSEBUTTONDOWN:
            mouse1, mouse2, mouse3 = pygame.mouse.get_pressed()
            if mouse1:
                pos = pygame.mouse.get_pos()
                tile_blue.collidepoint(pos)
                tile_yellow.collidepoint(pos)
                tile_red.collidepoint(pos)
                tile_green.collidepoint(pos)

    pygame.display.update()
  #  clock.tick(60)