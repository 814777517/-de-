import pygame

# 初始化Pygame窗口
pygame.init()
win_width = 640
win_height = 480
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Super Mario")

# 玛丽的起始坐标和速度
mario_x = 50
mario_y = 410
mario_speed = 5

# 加载图片资源
bg = pygame.image.load('background.png')
mario = pygame.image.load('mario.png')

# 游戏循环体
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 绘制背景和玛丽
    screen.blit(bg, (0, 0))
    screen.blit(mario, (mario_x, mario_y))

    # 处理键盘事件
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario_x -= mario_speed
    if keys[pygame.K_RIGHT]:
        mario_x += mario_speed
    if keys[pygame.K_UP]:
        mario_y -= mario_speed
    if keys[pygame.K_DOWN]:
        mario_y += mario_speed

    # 更新窗口
    pygame.display.update()

# 退出Pygame
pygame.quit()