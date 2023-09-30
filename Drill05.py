from pico2d import *
import random
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def random_point():
    global x1, y1, x2, y2
    x1 ,y1 = x2, y2
    x2, y2 = random.randint(200, 1000) , random.randint(100, 800)

def draw_arrow():
    global i
    if i >= 100:
        random_point()
        i = 0
    hand_arrow.draw(x2,y2)

def fallow_point():
    global frame, i
    t = i / 100
    x = (1 - t) * x1 + t * x2
    y = (1 - t) * y1 + t * y2
    if x1 < x2:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    i = i + 1
    if i % 6 == 0:
        frame = (frame + 1) % 8

running = True
x1, y1 = TUK_WIDTH // 2, TUK_HEIGHT // 2
x2, y2 = random.randint(300, 900) , random.randint(200, 500)
i = 0
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    draw_arrow()
    fallow_point()
    update_canvas()
    handle_events()
    delay(0.01)

close_canvas()




