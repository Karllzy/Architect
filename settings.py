import pygame


class Settings():
    """
    存储所有设置的类
    """

    def __init__(self):
        """
        初始化游戏
        """
        self.screen_width = 1000
        self.screen_height = 618
        self.bg_color = (245, 245, 247)

        self.GOLD = pygame.Color('gold')
        self.RED = pygame.Color('red')
        self.GREEN = pygame.Color('green')
        self.BLUE = pygame.Color("blue")
        self.GREY = pygame.Color('grey')
        self.BLACK = pygame.Color('black')
        self.PURPLE = pygame.Color('purple')

        self.mouse_state = -1
        # -1: 没有携带砖块
        # 0 : 横向的长砖块
        # 1 : 短砖块
        # 2 : 厚砖块
        # 3 : 纵向的长砖块
        # 4 : 删除砖块

        self.pressed = [False, False, False]

        self.floor_number = 0

        self.rotate = 0

        self.is_upped = True

