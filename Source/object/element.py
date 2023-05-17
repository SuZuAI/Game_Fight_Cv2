import pygame
import random
vec = pygame.math.Vector2

HEIGHT = 350
WIDTH = 700
ACC = 0.3
FRIC = -0.10
COUNT = 0

# Background--------------------------------------------------------------------
class Background(pygame.sprite.Sprite, object):
    def __init__(self, bg, screen):
        self.screen = screen
        super().__init__()
        self.back = bg
        self.x = -5
        self.y = -5
    def render(self):
        self.screen.blit(self.back, (self.x, self.y))

# Ground--------------------------------------------------------------------
class Ground(pygame.sprite.Sprite, object):
    def __init__(self, ground, screen):
        super().__init__()
        self.image = ground
        self.screen = screen
        self.rect = self.image.get_rect(center =(350, 350))
    def render(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

# player--------------------------------------------------------------------
class Player(pygame.sprite.Sprite, object):
    def __init__(self, g_group, img_player, screen, run_ani_R, run_ani_L, attack_ani_R, attack_ani_L):
        super().__init__()
        self.point = 0
        self.screen = screen
        self.running = False
        self.g_group = g_group
        self.jumping = False
        self.image = img_player
        self.rect = self.image.get_rect()

        self.run_ani_R = run_ani_R
        self.run_ani_L = run_ani_L

        self.attack_ani_R = attack_ani_R
        self.attack_ani_L = attack_ani_L
        self.attacking = False
        self.attack_frame = 0

        self.move_frame = 0
        self.vx = 0
        self.pos = vec(340, 240)
        self.vel = vec(1, 0)
        self.acc = vec(0, 0)
        self.direction = "RIGHT"
    def render(self):
        self.screen.blit(self.image, self.rect)
    def move(self, k, img_player):
        self.acc = vec(0, 0.5)
        if abs(self.vel.x) > 0.5:
            self.running = True
        else: self.running = False

        if k == 1:
            self.acc.x = -ACC
        if k == 0:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
        if self.vel.x == 0:
            self.image = img_player
        if not self.running:
            self.image = img_player

        self.rect.midbottom = self.pos
    def jumb(self):
        self.rect.x += 1

        hits = pygame.sprite.spritecollide(self, self.g_group, False)
        self.rect.x -= 1
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -12

    def update_move(self):
        if self.move_frame > 6:
            self.move_frame = 0
        if self.jumping == False and self.running == True:
            if self.vel.x > 0:
                self.image = self.run_ani_R[self.move_frame]
                self.direction = "RIGHT"
            else:
                self.image = self.run_ani_L[self.move_frame]
                self.direction = "LEFT"
            self.move_frame += 1
        if abs(self.vel.x) < 0.2 and self.move_frame != 0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = self.run_ani_R[self.move_frame]
            elif self.direction == "LEFT":
                self.image = self.run_ani_L[self.move_frame]
    def attack(self):
        if self.attack_frame > 10:
            self.attack_frame = 0
            self.attacking = False

        if self.direction == "RIGHT":
            self.image = self.attack_ani_R[self.attack_frame]
        elif self.direction == "LEFT":
            self.correction()
            self.image = self.attack_ani_L[self.attack_frame]

        self.attack_frame += 1

    def correction(self):
        if self.attack_frame == 1:
            self.pos.x -= 20
        if self.attack_frame == 10:
            self.pos.x += 20
    def gravity_check(self):
        hits = pygame.sprite.spritecollide(self, self.g_group, False)
        if self.vel.y > 0:
            if hits:
                lowest = hits[0]
                if self.pos.y  < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel.y = 0
                    self.jumping = False

# enemy-------------------------------------------------
class Enemy(pygame.sprite.Sprite, object):
    def __init__(self, enemy_R, enemy_L, player_ground, screen):
        super().__init__()
        self.image = enemy_R
        self.left = enemy_L
        self.right = enemy_R
        self.player_ground = player_ground
        self.rect = self.image.get_rect()
        self.pos = vec(0, 0)
        self.vel = vec(0, 0)
        self.screen = screen

        self.direction = random.randint(0, 1)
        self.vel.x = random.randint(2, 10) / 2
        self.attacking = False

        if self.direction == 1:
            self.pos = vec(WIDTH, 270)
        if self.direction == 0:
            self.pos = vec(0, 270)
        self.rect.center = self.pos
    def render(self):
        self.screen.blit(self.image, self.rect)
    def move(self):
        if self.direction == 1:
            self.image = self.right
            self.pos.x -= self.vel.x - 0.5 * ACC
            if self.pos.x < 2:
                self.direction = 0

        if self.direction == 0:
            self.image = self.left
            self.pos.x += self.vel.x + 0.5 * ACC
            if self.pos.x > (WIDTH - 20):
                self.direction = 1
        self.rect.center = self.pos
    def update_move(self):
        pass

    def update_remove(self, player):
        hits = pygame.sprite.spritecollide(self, self.player_ground, False)
        if hits and player.attacking:
            if player.vel.x > 0 and player.rect.center[0] < self.rect.center[0]:
                return True
            if player.vel.x < 0 and player.rect.center[0] > self.rect.center[0] :
                return True
        else:
            return False

    def attack(self, player):
        hits = pygame.sprite.spritecollide(self, self.player_ground, False)
        if hits and not player.attacking:
            return True
        return False
