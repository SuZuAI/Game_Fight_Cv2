# Package-----------------------------------------------------
import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import cv2
import mediapipe as mp
import time

from object.element import *
from object.data import *
from Start.displayRG import *

# initgital-----------------------------------------------------
pygame.init()

def INIT():
    global screen, clock
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("FIGHT")
    clock = pygame.time.Clock()

# Function --------------------------------------------------------------------
def create_enemy(player_ground):
    template_enemy = Enemy(enemy_R, enemy_L, player_ground, screen)
    return template_enemy

def draw_text(text, size, font, pos, color=(0, 0, 0)):
    font = pygame.font.SysFont(font, size)
    text = font.render(text, True, color)
    rect = text.get_rect()
    rect.center = pos
    screen.blit(text, rect)

# main-------------------------------------------------
def main():

    # init Background, Ground, Player (group)--------------------------------------------------------------------
    INIT()

    BG = Background(bg, screen)
    G = Ground(ground, screen)

    g_group = pygame.sprite.Group()
    g_group.add(G)
    player = Player(g_group, img_player, screen, run_ani_R, run_ani_L, attack_ani_R, attack_ani_L)

    # init TEST--------------------------------------------------------------------
    cnt = 0

        # test init enemy  --------------------------------------------------------------------
    player_group = pygame.sprite.Group()
    player_group.add(player)
    list_enemy: list= []
    for i in range(10):
        ran_number_enemy = random.randint(3, 5)
        list_tmp: list= []
        for j in range(ran_number_enemy):
            list_tmp.append(create_enemy(player_group))
        list_enemy.append(list_tmp)

        # test HP------------------------------------------------
    HP = 10

    # func phay game
    def play_game(run_game):
        global PTIME, C_TIME
        nonlocal cnt, HP
        while run_game == "True":
            # break game
            window.update()
            run_game = quit_py__.cget("text")
            player.gravity_check()

            # event get from videocapture--------------------------------------------------

            success, img = cap.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(imgRGB)
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    for id, lm in enumerate(handLms.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        # if id == 12 or id == 8 or id == 4 or id == 16 or id == 20:,
                        if cy < 300:
                            cv2.circle(img, (cx, cy), 25, (19, 235, 119), cv2.FILLED)
                            if id == 8:
                                player.move(1, img_player)
                            if id == 12:
                                player.move(0, img_player)
                            if id == 16:
                                player.jumb()
                            if id == 20 and not player.attacking:
                                player.attack()
                                player.attacking = True

                    mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            # show videocapture--------------------------------------------------------------
            C_TIME = time.time()
            fps = 1 / (C_TIME - PTIME)
            PTIME = C_TIME

            cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (250, 0, 255), 3)
            cv2.imshow("FIGHT", img)
            cv2.waitKey(5)

            # animation of player-----------------------------------------------------------
            player.update_move()
            if player.attacking:
                player.attack()

            # show background player ground enemy----------------------------------------------------
            BG.render()
            G.render()
            draw_text("Score: " + str(player.point), 40, "sans", (350, 100), (6, 12, 189))
            player.render()

            # test----------------------------------------------------
            for EM in list_enemy[cnt]:
                EM.update_move()
                if EM.attack(player):
                    HP -= 1
                if not EM.update_remove(player):
                    EM.render()
                    EM.move()
                else:
                    player.point += 1
                    list_enemy[cnt].remove(EM)
                for i in range(HP):
                    screen.blit(heart, (i * 35, 0))

            if len(list_enemy[cnt]) == 0:
                cnt += 1
            if cnt == 10:
                run_game = "False"
            if HP == 0: run_game == "False"

            # Run----------------------------------------------------
            player.render()
            player.move(2, img_player)

            # FPS and update display----------------------------------------------------
            clock.tick(120)
            pygame.display.update()

    # run program

    runner = "True"
    while runner == "True":

        reset()
        window.update()
        run_game = rungame__.cget("text")
        runner= quit__.cget("text")

        play_game(run_game)

    # exit pygame and sys
    pygame.quit()
    sys.exit()

main()
