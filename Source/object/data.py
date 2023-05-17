import pygame
import cv2
import mediapipe as mp

# INIT VALUE BEGIN---------------------------------------------------------
# videocapture
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
PTIME = 0
C_TIME = 0

# constant
HEIGHT = 350
WIDTH = 700
ACC = 0.3
FRIC = -0.10
COUNT = 0

# background-----------------------------------------------------
bg = pygame.image.load("./utils/background/Background1.png")
ground = pygame.image.load("./utils/background/Ground1.png")

#img player---------------------------------------------------------
img_player = pygame.image.load("./utils/background/Player_Sprite_R.png")

# Run animation for the Right- -------------------------------------------------------------------
run_ani_R = [pygame.image.load("./utils/player_animation/Player_Sprite_R.png"), pygame.image.load("./utils/player_animation/Player_Sprite2_R.png"),
             pygame.image.load("./utils/player_animation/Player_Sprite3_R.png"), pygame.image.load("./utils/player_animation/Player_Sprite4_R.png"),
             pygame.image.load("./utils/player_animation/Player_Sprite5_R.png"), pygame.image.load("./utils/player_animation/Player_Sprite6_R.png"),
             pygame.image.load("./utils/player_animation/Player_Sprite_R.png")]

# Run animation for the LEFT- -------------------------------------------------------------------
run_ani_L = [pygame.image.load("./utils/player_animation/Player_Sprite_L.png"), pygame.image.load("./utils/player_animation/Player_Sprite2_L.png"),
             pygame.image.load("./utils/player_animation/Player_Sprite3_L.png"), pygame.image.load("./utils/player_animation/Player_Sprite4_L.png"),
             pygame.image.load("./utils/player_animation/Player_Sprite5_L.png"), pygame.image.load("./utils/player_animation/Player_Sprite6_L.png"),
             pygame.image.load("./utils/player_animation/Player_Sprite_L.png")]

# Attack animation for the RIGHT- -------------------------------------------------------------------
attack_ani_R = [pygame.image.load("./utils/player_animation/Player_Sprite_R.png"), pygame.image.load("./utils/player_attach/Player_Attack_R.png"),
                pygame.image.load("./utils/player_attach/Player_Attack2_R.png"), pygame.image.load("./utils/player_attach/Player_Attack2_R.png"),
                pygame.image.load("./utils/player_attach/Player_Attack3_R.png"), pygame.image.load("./utils/player_attach/Player_Attack3_R.png"),
                pygame.image.load("./utils/player_attach/Player_Attack4_R.png"), pygame.image.load("./utils/player_attach/Player_Attack4_R.png"),
                pygame.image.load("./utils/player_attach/Player_Attack5_R.png"), pygame.image.load("./utils/player_attach/Player_Attack5_R.png"),
                pygame.image.load("./utils/player_animation/Player_Sprite_R.png")]

# Attack animation for the LEFT-- ------------------------------------------------------------------
attack_ani_L = [pygame.image.load("./utils/player_animation/Player_Sprite_L.png"), pygame.image.load("./utils/player_attach/Player_Attack_L.png"),
                pygame.image.load("./utils/player_attach/Player_Attack2_L.png"), pygame.image.load("./utils/player_attach/Player_Attack2_L.png"),
                pygame.image.load("./utils/player_attach/Player_Attack3_L.png"), pygame.image.load("./utils/player_attach/Player_Attack3_L.png"),
                pygame.image.load("./utils/player_attach/Player_Attack4_L.png"), pygame.image.load("./utils/player_attach/Player_Attack4_L.png"),
                pygame.image.load("./utils/player_attach/Player_Attack5_L.png"), pygame.image.load("./utils/player_attach/Player_Attack5_L.png"),
                pygame.image.load("./utils/player_animation/Player_Sprite_L.png")]
# heart ---------------------------------------------------------------------------------------
heart = pygame.image.load("./utils/heart/heart.png")

# enemy --------------------------------------------------------------------
enemy_R = pygame.image.load("./utils/enemy/Fall.png")
enemy_R = pygame.transform.scale(enemy_R, (40, 60))
enemy_L = pygame.transform.flip(enemy_R, True, False)
enemy_L = pygame.transform.scale(enemy_L, (40, 60))
# icon button -------------------------------------------------------
home = pygame.image.load("./utils/image_button/home.png")
interrogation = pygame.image.load("./utils/image_button/interrogation.png")
play_alt = pygame.image.load("./utils/image_button/play-alt.png")
setting = pygame.image.load("./utils/image_button/settings.png")
volume = pygame.image.load("./utils/image_button/volume.png")
