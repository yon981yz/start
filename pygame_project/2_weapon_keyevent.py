from tkinter import W
import pygame
import os
from random import *
##############################################################################
#기본 초기화 (반드시 해야하는 것들)
pygame.init()

#화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))


#화명 타이틀 설정
pygame.display.set_caption("PROJECT")

# FPS
clock = pygame.time.Clock()
##############################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트 등)

# 배경 이미지를 위한 위치 반환 및 images 폴더 위치 반환
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]


#캐릭터 만들기
character =  pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# 무기 만들기

weapon =  pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 반에 여러 발 발사 가능
weapons = []



#이동할 죄표
character_to_x = 0
character_to_y = 0


# 이동 속도
character_speed = 0.6
enemy_speed = 5
weapon_speed = 10

# 적 enemy

enemy = pygame.image.load("C:/Users/USER/Desktop/PythonWorkspace2/pygame_basic/enemy_quiz.png")
enemy_size = character.get_rect().size
enemy_width = character_size[0]
enemy_height = character_size[1]
enemy_x_pos = randint(0, (screen_width - enemy_width))
enemy_y_pos = 0

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 300

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()


#이벤트 루프
running = True
while running:
    dt = clock.tick(60)

    # print("fps : " + str(clock.get_fps()))
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0


    character_x_pos += character_to_x * dt

    # 3. 게임 캐릭터 위치 정의

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if enemy_x_pos < 0:
        enemy_x_pos = 0
    elif enemy_x_pos > screen_width - enemy_width:
        enemy_x_pos = screen_width - enemy_width
    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 무기 위치 조정
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]

    #천장에 닿은 무기 없애기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]
   
    enemy_y_pos += enemy_speed

    enemy_y_pos += character_to_y * dt

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = randint(1, screen_width - enemy_width)


    
    
    # 4. 충돌 처리

    # 충돌 처리를 위한 reft 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False


    
    # 5. 화면에 그리기

    # screen.fill((90, 0, 255))
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))


    # 타이머 집어 넣기 
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자 색상

    screen.blit(timer, (10, 10))

    #만약 시간이 0 이하라면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update()

pygame.time.delay(1500)
        
# pygame 종료
pygame.quit()