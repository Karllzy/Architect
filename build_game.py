import pygame,sys
import pygame.freetype

from settings import Settings
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("我，牙尖爪利！")
    icon = pygame.image.load("timg.png")
    pygame.display.set_icon(icon)

    GOLD = pygame.Color('gold')
    RED = pygame.Color('red')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    GREY = pygame.Color('grey')
    BLACK = pygame.Color('black')
    PURPLE = pygame.Color('purple')

    for i in range(1, 22):
        pygame.draw.line(screen, RED, [361+30*i, 9], [361+30*i, 609], 1)
        pygame.draw.line(screen, RED, [391, -21+30*i], [991, -21+30*i], 1)

    r1rect = pygame.draw.rect(screen, BLACK, (20, 52.25, 160, 50), 1)
    r2rect = pygame.draw.rect(screen, BLACK, (20, 206.75, 160, 50), 1)
    r3rect = pygame.draw.rect(screen, BLACK, (20, 361.25, 160, 50), 1)
    r4rect = pygame.draw.rect(screen, BLACK, (20, 515.75, 160, 50), 1)
    r5rect = pygame.draw.rect(screen, BLACK, (205, 52.25, 160, 50), 1)
    r6rect = pygame.draw.rect(screen, BLACK, (205, 206.75, 160, 50), 1)
    r7rect = pygame.draw.rect(screen, BLACK, (205, 361.25, 160, 50), 1)
    r8rect = pygame.draw.rect(screen, BLACK, (205, 515.75, 160, 50), 1)

    f1 = pygame.freetype.Font('C://Windows//Fonts//德彪钢笔行书字库.TTF', 36)
    f1rect = f1.render_to(screen, (40, 58), "上一层", fgcolor=BLACK, size=40)
    f2rect = f1.render_to(screen, (40, 212.5), "下一层", fgcolor=BLACK, size=40)
    f3rect = f1.render_to(screen, (57, 367), "删除", fgcolor=BLACK, size=40)
    f4rect = f1.render_to(screen, (57, 521.5), "完成", fgcolor=BLACK, size=40)
    f5rect = f1.render_to(screen, (225, 58), "长砖块", fgcolor=BLACK, size=40)
    f6rect = f1.render_to(screen, (225, 212.5), "短砖块", fgcolor=BLACK, size=40)
    f7rect = f1.render_to(screen, (225, 367), "厚砖块", fgcolor=BLACK, size=40)
    f8rect = f1.render_to(screen, (225, 521.5), "其他块", fgcolor=BLACK, size=40)

    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen)

run_game()
