import sys
from button import Button
import pygame


def check_events(model, ai_settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down_event(model, ai_settings, screen)
        elif event.type == pygame.MOUSEBUTTONUP:
            ai_settings.pressed = [False, False, False]
            ai_settings.is_upped = True


def mouse_down_event(model, ai_settings, screen):
    pressed_array = pygame.mouse.get_pressed()
    for index in range(len(pressed_array)):
        if pressed_array[index]:
            if index == 0:
                ai_settings.pressed = [True, False, False]
                if mouse_rect(ai_settings, screen):
                    x, y, kind, rotate = mouse_rect(ai_settings, screen)
                    layer = model[ai_settings.floor_number]
                    if (x, y, kind, rotate) in layer:
                        pass
                    elif kind == 4:
                        for brick in layer:
                            if brick[0] == x and brick[1] == y:
                                layer.pop(layer.index(brick))
                    else:
                        layer.append((x, y, kind, rotate))
                        model[ai_settings.floor_number] = layer

            elif index == 1:
                ai_settings.pressed = [False, True, False]
                ai_settings.mouse_state = -1
            elif index == 2:
                ai_settings.pressed = [False, False, True]
                ai_settings.mouse_state = -1


def update_screen(ai_settings, screen, model, botton_group):
    screen.fill(ai_settings.bg_color)
    for i in range(1, 22):
        pygame.draw.line(screen, ai_settings.RED, [361+30*i, 9], [361+30*i, 609], 1)
        pygame.draw.line(screen, ai_settings.RED, [391, -21+30*i], [991, -21+30*i], 1)
    draw_model(ai_settings, screen, model)
    mouse_rect(ai_settings, screen)
    botton_group.update()
    pygame.display.update()


def draw_model(ai_settings, screen, model):
    color_index = [ai_settings.BLUE, ai_settings.PURPLE, ai_settings.GREEN]
    gray_color_index = [ai_settings.GREY, ai_settings.GREY, ai_settings.BLACK]
    brick_info = [[60, 30], [30, 30], [30, 30]]
    layer_number = len(model)
    if layer_number == 1 or ai_settings.floor_number == 0:
        for brick in model[0]:
            color = color_index[brick[2]]
            shape = brick_info[brick[2]]
            if brick[3] == 1:
                rect_info = (brick[0] * 30 + 361, brick[1] * 30 - 21, shape[1], shape[0])
            else:
                rect_info = (brick[0] * 30 + 361, brick[1] * 30 - 21, shape[0], shape[1])
            pygame.draw.rect(screen, color, rect_info, 0)
    elif layer_number >= 2:
        last_layer = model[ai_settings.floor_number - 1]
        active_layer = model[ai_settings.floor_number]
        for brick in last_layer:
            color = gray_color_index[brick[2]]
            shape = brick_info[brick[2]]
            if brick[3] == 1:
                rect_info = (brick[0] * 30 + 361, brick[1] * 30 - 21, shape[1], shape[0])
            else:
                rect_info = (brick[0] * 30 + 361, brick[1] * 30 - 21, shape[0], shape[1])
            pygame.draw.rect(screen, color, rect_info, 0)
        for brick in active_layer:
            color = color_index[brick[2]]
            shape = brick_info[brick[2]]
            if brick[3] == 1:
                rect_info = (brick[0] * 30 + 361, brick[1] * 30 - 21, shape[1], shape[0])
            else:
                rect_info = (brick[0] * 30 + 361, brick[1] * 30 - 21, shape[0], shape[1])
            pygame.draw.rect(screen, color, rect_info, 0)


def mouse_rect(ai_settings, screen):
    point_x, point_y = pygame.mouse.get_pos()
    if 391 < point_x < 991 and 9 < point_y < 609:
        x = int((point_x - 361)/30)
        y = int((point_y - 9)/30 + 1)
        if ai_settings.mouse_state == 0:
            draw_model(ai_settings, screen, [[(x, y, 0, ai_settings.rotate)]])
            return x, y, 0, ai_settings.rotate
        elif ai_settings.mouse_state == 1:
            draw_model(ai_settings, screen, [[(x, y, 1, ai_settings.rotate)]])
            return x, y, 1, ai_settings.rotate
        elif ai_settings.mouse_state == 2:
            draw_model(ai_settings, screen, [[(x, y, 2, ai_settings.rotate)]])
            return x, y, 2, ai_settings.rotate
        elif ai_settings.mouse_state == 3:
            draw_model(ai_settings, screen, [[(x, y, 0, ai_settings.rotate)]])
            return x, y, 0, ai_settings.rotate
        elif ai_settings.mouse_state == 4:
            return x, y, 4, 4
        else:
            return False


def button_maker(ai_settings, screen, button_group):
    button_texts = ["Last", "Next", "Delete", "Finish", "Long", "Short", "Thick", "other"]
    button_positions = [[20, 52.25], [20, 206.75], [20, 361.25], [20, 515.75],
                        [205, 52.25], [205, 206.75], [205, 361.25], [205, 515.75]]
    functions = [5, 6, 4, 7, 0, 1, 2, 3]
    for i in range(8):
        button = Button(ai_settings, screen, button_texts[i], button_positions[i], functions[i])
        button_group.add(button)
    return button_group


def function_controller(ai_settings, model):
    if ai_settings.mouse_state == 5:
        if ai_settings.floor_number >= 1:
            ai_settings.floor_number -= 1
            ai_settings.mouse_state = -1
    elif ai_settings.mouse_state == 6:
        layer_number = len(model)
        if ai_settings.floor_number > layer_number-2:
            model.append([])
        ai_settings.floor_number += 1
        ai_settings.mouse_state = -1
    elif ai_settings.mouse_state == 7:
        pass
