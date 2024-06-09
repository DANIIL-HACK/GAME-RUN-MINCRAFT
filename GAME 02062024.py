import pygame
import random
class Block:
    def __init__(self):
        self.x = random.randint(0, 1720)
        self.y = random.randint(400, 600)
        self.img = load_img("minecraft-block11loghcggjfgfjgrhgyfyyyyffffffffffffffffffffffffffffffffffffff.jpg")
        self.img = pygame.transform.scale(self.img, (99, 99))

    def render(self):

        win.blit(self.img, (self.x, self.y))


class Field:

    def __init__(self):
        self.dist = 0
        self.spi = 10
        self.block = Block()
        self.block1 = Block()
        self.block2 = Block()
        self.block3 = Block()
        self.block28 = Block()

    def move(self):
        self.block.x -= self.spi
        self.block1.x -= self.spi
        self.block2.x -= self.spi
        self.block3.x -= self.spi
        self.block28.x -= self.spi

        if self.block.x < 0:
            self.block.x = 1720
            self.block.y = random.randint(400, 600)

        if self.block1.x < 0:
            self.block1.x = 1720
            self.block1.y = random.randint(400, 600)

        if self.block2.x < 0:
            self.block2.x = 1720
            self.block2.y = random.randint(400, 600)

        if self.block3.x < 0:
            self.block3.x = 1720
            self.block3.y = random.randint(400, 600)

        if self.block28.x < 0:
            self.block28.x = 1720
            self.block28.y = random.randint(400, 600)

    def render(self):
        self.block.render()
        #self.block1.render()
        #self.block2.render()
        #self.block3.render()
        #self.block28.render()


class Character:
    def __init__(self):
        self.x = 500
        self.y = 500
        self.img = load_img("персонаж пайноп 4012.png")
        self.sp = 10
        self.g = 20
        self.jump = False
        self.j_p = -1
        self.img = pygame.transform.scale(self.img, (60, 167))
        self.field = Field()

    def render(self):
        win.blit(self.img, (self.x, self.y))

    def move(self):
        if self.x > self.field.block.x and self.x < self.field.block.x + 60:
            if self.y > self.field.block.y - 180:
                self.y = self.field.block.y - 180


        if self.y < 500:
            self.y = self.y + self.g

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.j_p = self.j_p + 5
            if self.jump == False:
                self.jump = True
        else:
            if self.jump:
                self.y = self.y - self.j_p
                self.j_p = self.j_p - 5

        if self.j_p < 0:
            self.jump = False

        print(self.jump, self.j_p)




def load_img(name):
    img = pygame.image.load(name)
    img = img.convert()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    return img

FPS = 30
clock = pygame.time.Clock()

win = pygame.display.set_mode((1369, 700))

char = Character()


main_character = load_img("персонаж пайноп 4012.png")
zombi = load_img("зомби право.png")

zombi = pygame.transform.scale(zombi, (60, 167))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    win.fill((8,121,241))

    char.render()
    char.move()
    char.field.render()
    char.field.move()

    #win.blit(main_character, (0, 0))
    #win.blit(zombi, (100, 100))

    pygame.display.update()
    clock.tick(FPS)