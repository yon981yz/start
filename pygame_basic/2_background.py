import pygame

pygame.init()

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


#화명 타이틀 설정
pygame.display.set_caption("Nado Game")

background = pygame.image.load("C:/Users/USER/Desktop/PythonWorkspace2/pygame_basic/background.png")

#이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((90, 0, 255))
    screen.blit(background, (0, 0))

    pygame.display.update()


        
# pygame 종료
pygame.quit()