import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

from pygame_ui_controls import UI, Button, Slider, CheckBox, Text, ImageButton

if __name__ == "__main__":
    pygame.init()

    UI.init()
    UI.FONT = pygame.freetype.Font("./data/Ubuntu-Regular.ttf", 24)
    Button.CONFIRM_TEXT = "Confirm ?"

    WIDTH, HEIGHT = 660, 410
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("UI Elements Tests")

    clock = pygame.time.Clock()

    execute = True

    last_click_state = False
    clicked_up = False

    Slider("test", (20, 20), (300, 28), ticks=10)
    Slider("test2", (20, 68), (300, 28), ticks=20)
    Slider("test3", (20, 116), (300, 28))
    Slider("test4", (20, 164), (300, 28), locked=True)
    Slider("test5", (20, 212), (300, 28), locked=True, ticks=10)    

    Button("test", (340, 20), text="Classic")
    Button("test2", (340, 80), text="No hover", hoverable=False)
    Button("locked", (340, 140), text="Locked", locked=True)

    CheckBox("test", (20, 260))
    CheckBox("test2", (70, 260), checked=True)
    CheckBox("test3", (120, 260), locked=True)
    CheckBox("test4", (170, 260), checked=True, locked=True)

    CheckBox("test-linked1", (20, 350),
             linked=["test-linked1", "test-linked2", "test-linked3"])
    CheckBox("test-linked2", (70, 350),
             linked=["test-linked1", "test-linked2", "test-linked3"])
    CheckBox("test-linked3", (120, 350),
             linked=["test-linked1", "test-linked2", "test-linked3"])
    
    ImageButton("test", "./data/hut.png", (340, 200))
    ImageButton("test2", "./data/hut.png", (400, 200), (100, 50))
    ImageButton("test3", "./data/hut.png", (340, 260), (50, 100))
    ImageButton("test4", "./data/hut.png", (400, 260), (100, 100))
    ImageButton("test5", "./data/hut.png", (510, 200), locked=True)
    ImageButton("test6", "./data/hut.png", (570, 200), hoverable=False)

    Text("test", (20, 310), "Text")
    Text("test2", (80, 310), "Text", color=(50, 50, 255))

    while execute:
        SCREEN.fill((10, 14, 18))

        pressed_mouse_keys = pygame.mouse.get_pressed()
        current_click_state = pressed_mouse_keys[0]

        if Button.clicked("test"):
            print("Button 1 pushed")

        if Button.clicked("test2"):
            print("Button 2 pushed")

        if Button.clicked("locked"):
            print("Locked button pushed")

        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                execute = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    execute = False

        UI.update(SCREEN, x, y, current_click_state)
        pygame.display.update(UI.updated_rects())
        # pygame.display.update() works well too

        clock.tick(60)