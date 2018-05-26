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
        winsound.Beep(self.frequency, 300)

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

    def check_clicked(self, pos):
        return self.shape.collidepoint(pos)

class Game:

    def __init__(self, max_levels, blue, red, yellow, green):
        self.over = False
        self.simon = Simon(blue, red, yellow, green)
        self.player = Player()
        self.level = self.simon.get_level_number()
        self.max_levels = max_levels
        self.regular_mode = False
        self.timeout = 2
        self.waiting = False

    def next_level(self):
        print("next level")
        self.simon.add_color()
        self.player.increase_score()
        self.show_level()
        self.waiting = True
        self.timeout = self.timeout - (self.timeout * 0.1)

    def show_level(self):
        for tile in self.simon.history:
            tile.activate()

    def get_random_color(self):
        random_color_tuple = random.choice(self.simon.colors)
        random_color = self.get_color(random_color_tuple)
        return random_color

    def test_player(self, pos):
        if tile.check_clicked(pos):
            print("You have passed this test. On to the next.")
            self.player.increase_score()
            self.waiting = False
        else:
            print("You lose.")
            self.over = True

class Simon:

    def __init__(self, blue, red, yellow, green):
        self.history = []
        self.colors = [blue, red, yellow, green]

    def get_level_number(self):
        return len(self.history)

    def add_color(self):
        self.history.append(random.choice(self.colors))

class Player:

    def __init__(self):
        self.score = 0

    def increase_score(self):
        self.score = self.score + 1

tile_blue = Tile(0, 355, 200, Tile.COLOR_BLUE)
tile_blue.draw()
tile_red = Tile(0, 0, 473, Tile.COLOR_RED)
tile_red.draw()
tile_yellow = Tile(355, 355, 1385, Tile.COLOR_YELLOW)
tile_yellow.draw()
tile_green = Tile(355, 0, 941, Tile.COLOR_GREEN)
tile_green.draw()

game = Game(22, tile_blue, tile_red, tile_yellow, tile_green)

while not game.over:
    if not game.waiting:
        game.next_level()
    for tile in game.simon.history:
        pygame.event.wait()
        mouse1, mouse2, mouse3 = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        game.test_player(pos)

    pygame.display.update()
