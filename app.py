import pygame
import sys
from pygame.locals import *
import myplane
import All_Enemy
import bullet

# 定义为常量
WIDTH = 480  # 窗口宽度
HEIGHT = 720  # 窗口高度
FPS = 60  # 游戏帧率
pygame.init()  # pygame初始化，必须有，必须在开头
# 颜色
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
# 创建主窗体
clock = pygame.time.Clock()  # 用于控制刷新频率的对象
surface = pygame.display.set_mode((WIDTH, HEIGHT))
# 设置窗口标题
pygame.display.set_caption("打飞机")
# 设置背景
background = pygame.image.load("images/background.png").convert_alpha()

# 添加背景音乐
pygame.mixer.music.load("sound/game_music.wav")
pygame.mixer.music.set_volume(0.06)
bef_s = pygame.mixer.Sound("sound/big_spaceship_flying.wav")
bef_s.set_volume(0.2)
me_down_sound = pygame.mixer.Sound("sound/game_over.wav")
me_down_sound.set_volume(0.2)
smae_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
smae_down_sound.set_volume(0.2)
mide_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
mide_down_sound.set_volume(0.2)
bige_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
bige_down_sound.set_volume(0.2)
bul_s = pygame.mixer.Sound("sound/bullet.wav")
bul_s.set_volume(0.1)
bomb_s = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_s.set_volume(0.5)
pygame.mixer.music.play(-1)


def add_small_enemy(group1, group2, num):
    for e1 in range(num):
        e1 = All_Enemy.Small_Enemy(WIDTH, HEIGHT)
        group1.add(e1)
        group2.add(e1)


def add_mid_enemy(group1, group2, num):
    for e2 in range(num):
        e2 = All_Enemy.Mid_Enemy(WIDTH, HEIGHT)
        group1.add(e2)
        group2.add(e2)


def add_big_enemy(group1, group2, num):
    for e3 in range(num):
        e3 = All_Enemy.Big_Enemy(WIDTH, HEIGHT)
        group1.add(e3)
        group2.add(e3)


def main():
    # 创建我方飞机
    me = myplane.MyPlan(WIDTH, HEIGHT)

    # 生成所有敌机组
    enemies = pygame.sprite.Group()
    # 创建一个小敌机
    small_enemies = pygame.sprite.Group()  # 创建一个精灵组
    add_small_enemy(enemies, small_enemies, 25)
    # 创建一个中敌机
    mid_enemies = pygame.sprite.Group()  # 创建一个精灵组
    add_mid_enemy(enemies, mid_enemies, 15)
    # 创建一个大敌机
    big_enemies = pygame.sprite.Group()  # 创建一个精灵组
    add_big_enemy(enemies, big_enemies, 10)

    # 计时，用了动态切换图片
    delay = 100
    # 开关，用来动态切换图片
    switch_image = True

    # 死亡动画轮循下标
    me_down_index = 0
    smae_down_index = 0
    mide_down_index = 0
    bige_down_index = 0
    # 创建子弹
    bullet1 = []
    bullet1_index = 0
    BULLET_NUM = 4

    for i in range(0, BULLET_NUM):
        bullet1.append(bullet.Bullet(me.rect.midtop))
    # 暂停或恢复
    paused = False
    pause_nor_image = pygame.image.load("images/game_pause_nor.png").convert_alpha()
    resume_nor_image = pygame.image.load("images/game_resume_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load("images/game_pause_pressed.png").convert_alpha()
    resume_pressed_image = pygame.image.load("images/game_resume_pressed.png").convert_alpha()
    pause_rect = pause_nor_image.get_rect()
    pause_rect.right, pause_rect.top = \
        WIDTH - 10, 10
    pause_image = pause_nor_image

    # 全屏boom
    bomb_image = pygame.image.load("images/bomb.png").convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font("font/Marker Felt.ttf", 30)
    bomb_num = 99

    pygame.image.load("images/game_pause_nor.png").convert_alpha()
    # 统计得分
    score = 0
    score_font = pygame.font.Font("font/Marker Felt.ttf", 36)
    # 游戏结束
    gameover = False
    gameover_image = pygame.image.load("images/quit_nor.png").convert_alpha()
    restart_image = pygame.image.load("images/restart_nor.png").convert_alpha()
    gameover_font = pygame.font.Font("font/HYShangWeiShouShuW.ttf", 72)
    gameover_rect = gameover_image.get_rect()
    restart_rect = restart_image.get_rect()
    # 访问文件限制
    recorded = False

    while True:

        # 监听事件列表
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and pause_rect.collidepoint(event.pos):
                    paused = not paused
                    if paused:
                        pause_image = resume_nor_image
                    else:
                        pause_image = pause_nor_image
                elif event.button == 1 and restart_rect.collidepoint(event.pos):
                    main()
                elif event.button == 1 and gameover_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                if pause_rect.collidepoint(event.pos):
                    if paused:
                        pause_image = resume_pressed_image
                    else:
                        pause_image = pause_pressed_image
                else:
                    if paused:
                        pause_image = resume_nor_image
                    else:
                        pause_image = pause_nor_image
            elif event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    if bomb_num > 0:
                        bomb_num -= 1
                        bomb_s.play(-1)
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False
        surface.blit(background, (0, 0))
        if not gameover:
            if not paused:
                # 检测键盘输入
                key_pressed = pygame.key.get_pressed()
                # 判断按键并绑定方法
                if key_pressed[K_w] or key_pressed[K_UP]:
                    me.moveUp()
                if key_pressed[K_s] or key_pressed[K_DOWN]:
                    me.moveDown()
                if key_pressed[K_a] or key_pressed[K_LEFT]:
                    me.moveLeft()
                if key_pressed[K_d] or key_pressed[K_RIGHT]:
                    me.moveRight()
                # 击锤
                if not (delay % 10):
                    bul_s.play()
                    bullets = bullet1
                    bullets[bullet1_index].reset(me.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % 4
                # 检测碰撞
                enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
                if enemies_down:
                    me.active = False
                    for each in enemies_down:
                        each.active = False
                        # pygame.mask.from_surface(each.image)
                        # print(each)
                # 把背景绘制到窗口
                surface.blit(background, (0, 0))

                # 判断子弹是否击中
                for b in bullets:
                    if b.active:
                        b.move()
                        surface.blit(b.image, b.rect)
                        enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                        if enemy_hit:
                            b.active = False
                            for e in enemy_hit:
                                if e in mid_enemies or e in big_enemies:
                                    e.ph -= b.attack
                                    e.hit = True
                                    if e.ph <= 0:
                                        e.active = False
                                else:
                                    e.active = False
                # 绘制大敌机
                for each in big_enemies:
                    if each.active:
                        each.move()
                        if each.hit:
                            surface.blit(each.image_hit, each.rect)
                            each.hit = False
                        else:
                            if switch_image:
                                surface.blit(each.image1, each.rect)
                            else:
                                surface.blit(each.image2, each.rect)
                            if each.rect.bottom == -50:
                                bef_s.play(-1)
                        # 绘制血条
                        pygame.draw.line(surface, BLACK,
                                         (each.rect.left, each.rect.top - 5),
                                         (each.rect.right, each.rect.top - 5),
                                         2)
                        # 绘制血量， 0-20% 红 20%-100% 绿
                        ph_remain = each.ph / All_Enemy.Big_Enemy.ph
                        if ph_remain > 0.2:
                            color_change = GREEN
                        else:
                            color_change = RED
                        pygame.draw.line(surface, color_change,
                                         (each.rect.left, each.rect.top - 5),
                                         (each.rect.left + each.rect.width * ph_remain, each.rect.top - 5),
                                         2)

                    else:
                        # 毁灭
                        if not (delay % 5):
                            if bige_down_index == 0:
                                bef_s.stop()
                                bige_down_sound.play()
                                score += 10000
                            surface.blit(each.down_images[bige_down_index], each.rect)
                            # 第一种方式
                            # me_down_index += 1
                            # if me_down_index == len(me.down_images):
                            #     me.reset()
                            bige_down_index = (bige_down_index + 1) % len(each.down_images)
                            if bige_down_index == 0:
                                each.reset()
                # 绘制中敌机
                for each in mid_enemies:
                    if each.active:
                        each.move()
                        if each.hit:
                            surface.blit(each.image_hit, each.rect)
                            each.hit = False
                        else:
                            surface.blit(each.image, each.rect)
                        # 绘制血条
                        pygame.draw.line(surface, BLACK,
                                         (each.rect.left, each.rect.top - 5),
                                         (each.rect.right, each.rect.top - 5),
                                         2)
                        # 绘制血量， 0-20% 红 20%-100% 绿
                        ph_remain = each.ph / All_Enemy.Mid_Enemy.ph
                        if ph_remain > 0.2:
                            color_change = GREEN
                        else:
                            color_change = RED
                        pygame.draw.line(surface, color_change,
                                         (each.rect.left, each.rect.top - 5),
                                         (each.rect.left + each.rect.width * ph_remain, each.rect.top - 5),
                                         2)
                    else:
                        # 毁灭
                        if not (delay % 5):
                            if mide_down_index == 0:
                                mide_down_sound.play()
                                score += 1000
                            surface.blit(each.down_images[mide_down_index], each.rect)
                            # 第一种方式
                            # me_down_index += 1
                            # if me_down_index == len(me.down_images):
                            #     me.reset()
                            mide_down_index = (mide_down_index + 1) % len(each.down_images)
                            if mide_down_index == 0:
                                each.reset()
                # 绘制小敌机
                for each in small_enemies:
                    if each.active:
                        each.move()
                        surface.blit(each.image, each.rect)
                    else:
                        # 毁灭
                        if not (delay % 5):
                            if smae_down_index == 0:
                                smae_down_sound.play()
                                score += 100
                            surface.blit(each.down_images[smae_down_index], each.rect)
                            # 第一种方式
                            # me_down_index += 1
                            # if me_down_index == len(me.down_images):
                            #     me.reset()
                            smae_down_index = (smae_down_index + 1) % len(each.down_images)
                            if smae_down_index == 0:
                                each.reset()

                # 绘制我方飞机窗口
                if me.active:
                    if switch_image:
                        surface.blit(me.image1, me.rect)
                    else:
                        surface.blit(me.image2, me.rect)
                else:
                    # 毁灭
                    if not (delay % 5):
                        if me_down_index == 0:
                            me_down_sound.play()
                        surface.blit(me.down_images[me_down_index], me.rect)
                        # 第一种方式
                        # me_down_index += 1
                        # if me_down_index == len(me.down_images):
                        #     me.reset()
                        me_down_index = (me_down_index + 1) % len(me.down_images)
                        if me_down_index == 0:
                            gameover = True
                            me.reset()
            # 绘制炸弹
            surface.blit(bomb_image, (10, HEIGHT - bomb_rect.height))
            bomb_text = bomb_font.render("X%d" % bomb_num, True, WHITE)
            bomb_text_rect = bomb_text.get_rect()
            surface.blit(bomb_text, (45 + bomb_text_rect.width, HEIGHT - bomb_text_rect.height))
            # 绘制分数
            score_text = score_font.render("Score : %s" % str(score), True, WHITE)
            surface.blit(score_text, (10, 10))
            # 绘制暂停
            surface.blit(pause_image, pause_rect)
        elif gameover:
            # 背景音乐关闭
            pygame.mixer.music.stop()
            # 获取最高分
            if not recorded:
                recorded = True
                # 读取最高分
                with open("record.txt", "r") as f:
                    record_score = int(f.read())
            if score > record_score:
                record_score = score
                with open("record.txt", "w") as f:
                    f.write(str(score))
                    f.close()
            # 绘制结束画面
            best_text = gameover_font.render("Best:", True, WHITE)
            best_text_rect = best_text.get_rect()
            surface.blit(best_text, (
                (WIDTH - best_text_rect.width) // 2,
                50))
            now_text = gameover_font.render("Your Score:", True, WHITE)
            now_text_rect = now_text.get_rect()
            surface.blit(now_text, (
                (WIDTH - now_text_rect.width) // 2,
                250))
            best_score = gameover_font.render("%d" % record_score, True, WHITE)
            now_score = gameover_font.render("%d" % score, True, WHITE)
            best_score_rect = best_score.get_rect()
            now_score_rect = now_score.get_rect()
            restart_rect.left, restart_rect.top =(
                (WIDTH - restart_rect.width) // 2,
                HEIGHT - 200)
            gameover_rect.left, gameover_rect.top =(
                (WIDTH - gameover_rect.width) // 2,
                HEIGHT - 100)
            surface.blit(best_score, (
                (WIDTH - best_score_rect.width) // 2,
                150))
            surface.blit(now_score, (
                (WIDTH - now_score_rect.width) // 2,
                350))
            surface.blit(restart_image, restart_rect)
            surface.blit(gameover_image, gameover_rect)
        # 绘制屏幕
        pygame.display.flip()

        # 计时器
        if not (delay % 5):
            switch_image = not switch_image
        delay -= 1
        if not delay:
            delay = 100

        clock.tick(FPS)  # 控制循环刷新频率，每秒刷新FPS对应的次数


if __name__ == '__main__':
    main()
# # 退出所有pygame模块
# pygame.quit()
