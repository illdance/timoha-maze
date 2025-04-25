from pygame import *
mixer.init()
font.init()
f0nt = font.Font(None, 70)
win = f0nt.render(
    'YOU FOUND PIROJOK!', True, (0, 255, 0)
)
loose = f0nt.render(
    'YOU ATE PIROJOK!', True, (255, 0, 0)
)
#mixer.music.load('jungles.ogg')
#mixer.music.play(0)
#kick = mixer.Sound('kick.ogg')
#money = mixer.Sound('money.ogg')

window = display.set_mode((720, 500))
display.set_caption('Resident of walking evil of us within a maze')
background = transform.scale(image.load('background.jpg'), (720, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, filename, w, h, speed, x, y):
        super().__init__()
        self.image = transform.scale(
            image.load(filename),
            (w, h)
        )
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,
                    (self.rect.x, self.rect.y)
                    )

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= 1
        if keys_pressed[K_d] and self.rect.x < 720:
            self.rect.x += 1
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 1
        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += 1

class Enemy(GameSprite):
    direction = 'left'
    speed = 1
    def update(self):
        if self.rect.x <= 468:
            self.direction = 'right'
        if self.rect.x >= 640:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill((45, 230, 193))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = Player('hero.png', 75, 75, 1, 20, 20)
villian = Enemy('cyborg.png', 50, 50, 1, 595, 250)
treasure = GameSprite('treasure.png', 100, 100, 0, 590, 410)
wall1 = Wall(20, 450, 156, 100)
wall2 = Wall(20, 450, 312, -50)
wall3 = Wall(20, 450, 468, 100)
walls = sprite.Group()
walls.add(wall1, wall2, wall3)

clock = time.Clock()
clock.tick(60)
display.update()
finish = False

game = True
while game == True:
    if finish != True:

        window.blit(background, (0, 0))
        player.reset()
        villian.reset()
        treasure.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        player.update()
        villian.update()
        if sprite.collide_rect(player, treasure):
            window.blit(win, (200, 200))
            finish = True
            #money.play()
        if sprite.collide_rect(player, villian):
            window.blit(loose, (200, 200))
            finish = True
            #kick.play()
        if len(sprite.spritecollide(player, walls, False)) > 0:
            player.rect.x = 20
            player.rect.y = 20
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()