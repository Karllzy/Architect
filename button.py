import pygame
from pygame.sprite import Sprite


class Button(Sprite):

    def __init__(self, ai_settings, screen, msg, position, function_num):
        super(Button, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.function_num = function_num

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 160, 50
        self.button_color = (230, 230, 230)
        self.text_color = self.ai_settings.BLACK
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topleft = position

        # 按钮的标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """
        将msg渲染成图像，并使其在按钮上居中
        :param msg:
        :return:
        """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def is_over(self):
        """判断鼠标是否在按钮上"""
        point_x, point_y = pygame.mouse.get_pos()
        x, y = self.rect.x, self.rect.y

        in_x = x < point_x < x + self.width
        in_y = y < point_y < y + self.height
        return in_x and in_y

    def update(self):
        button_color = self.button_color
        if self.is_over():
            if self.ai_settings.pressed[0] and self.ai_settings.is_upped:
                button_color = (190, 190, 190)
                self.ai_settings.mouse_state = self.function_num
                self.ai_settings.is_upped = False
            else:
                button_color = (220, 220, 220)
        self.screen.fill(button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)



    # r1rect = pygame.draw.rect(screen, BLACK, (20, 52.25, 160, 50), 1)
    # r2rect = pygame.draw.rect(screen, BLACK, (20, 206.75, 160, 50), 1)
    # r3rect = pygame.draw.rect(screen, BLACK, (20, 361.25, 160, 50), 1)
    # r4rect = pygame.draw.rect(screen, BLACK, (20, 515.75, 160, 50), 1)
    # r5rect = pygame.draw.rect(screen, BLACK, (205, 52.25, 160, 50), 1)
    # r6rect = pygame.draw.rect(screen, BLACK, (205, 206.75, 160, 50), 1)
    # r7rect = pygame.draw.rect(screen, BLACK, (205, 361.25, 160, 50), 1)
    # r8rect = pygame.draw.rect(screen, BLACK, (205, 515.75, 160, 50), 1)
    #
    # f1 = pygame.freetype.Font('德彪钢笔行书字库.TTF', 36)
    # f1rect = f1.render_to(screen, (40, 58), "上一层", fgcolor=BLACK, size=40)
    # f2rect = f1.render_to(screen, (40, 212.5), "下一层", fgcolor=BLACK, size=40)
    # f3rect = f1.render_to(screen, (57, 367), "删除", fgcolor=BLACK, size=40)
    # f4rect = f1.render_to(screen, (57, 521.5), "完成", fgcolor=BLACK, size=40)
    # f5rect = f1.render_to(screen, (225, 58), "长砖块", fgcolor=BLACK, size=40)
    # f6rect = f1.render_to(screen, (225, 212.5), "短砖块", fgcolor=BLACK, size=40)
    # f7rect = f1.render_to(screen, (225, 367), "厚砖块", fgcolor=BLACK, size=40)
    # f8rect = f1.render_to(screen, (225, 521.5), "其他块", fgcolor=BLACK, size=40)
