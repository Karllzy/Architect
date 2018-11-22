import pygame,sys
import pygame.freetype
from settings import Settings
from button import Button
import game_functions as gf
from pygame.sprite import Group


def run_game():
    model = [[]]

    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("我，牙尖爪利！")

    icon = pygame.image.load("images/icon_1.jpg")
    pygame.display.set_icon(icon)

    button_group = Group()
    gf.button_maker(ai_settings, screen, button_group)

    while True:
        gf.check_events(model, ai_settings, screen)
        gf.function_controller(ai_settings, model)
        gf.update_screen(ai_settings, screen, model, button_group)


if __name__ == "__main__":
    run_game()

