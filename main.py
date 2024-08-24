import random
import sys

import pygame

# functions
def draw_grid(screen):
    for i in range(20):
        for j in range(20):
            rect = pygame.Rect(i * 20 + 1, j * 20 + 1, 19, 19)
            pygame.draw.rect(surface=screen, color='White', rect=rect)

def draw_snake(screen):
    pygame.draw.rect(screen, 'Red', snake)

def draw_food(screen):
    pygame.draw.ellipse(screen, 'Orange', food)

def update_snake():
    if key_pressed == 'up':
        snake.y -= 20
    elif key_pressed == 'down':
        snake.y += 20
    elif key_pressed == 'left':
        snake.x -= 20
    elif key_pressed == 'right':
        snake.x += 20

def generate_food_at_random_position():
    global food
    x_random = random.randint(0, 19) * 20
    y_random = random.randint(0, 19) * 20
    food.x = x_random
    food.y = y_random

def check_collision():
    if snake.colliderect(food):
        return True
    return False

def tail_collision():
    for tail in tails[1:]:
        if tail.colliderect(snake):
            return True
    return False
def add_tail():
    tail = pygame.Rect(snake.x, snake.y, 19, 19)
    tails.append(tail)

def update_tails():
    for index in range(len(tails)-1, 0, -1):
        prev_tail = tails[index-1]
        tails[index].x = prev_tail.x
        tails[index].y = prev_tail.y

def draw_tails():
    for tail in tails[1:]:
        pygame.draw.rect(screen, 'Red', tail)

def check_outside():
    if snake.x < 0 or snake.x > 19 * 20 or snake.y < 0 or snake.y > 19 * 20:
        return True
    else:
        return False

def draw_score():
    score_label = font.render(f'Score: {score}', True, 'White')
    screen.blit(score_label, (450, 20))

def draw_start_screen():
    label = font.render(f'Press space to start', True, 'White')
    screen.blit(label, (150, 200))

def draw_reset_screen():
    label = font.render(f'Your current score is: {score}', True, 'White')
    label1 = font.render(f'Your highest score is: {highest_score}', True, 'White')
    label2 = font.render(f'Press space to restart', True, 'White')
    screen.blit(label, (150, 200))
    screen.blit(label1, (150, 230))
    screen.blit(label2, (150, 260))

def reset():
    global score, key_pressed, tails

    snake.x = 200
    snake.y = 200
    tails = [snake]
    score = 0
    key_pressed = None


# global variables
pygame.init()
clock = pygame.time.Clock()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
snake = pygame.Rect(9*20 + 1, 9*20 + 1, 19, 19)
food = pygame.Rect(0, 0, 20, 20)
key_pressed = None
tails = [snake]
font = pygame.font.Font(None, 40)
score = 0
highest_score = 0
begin = True
playing = False

# initialize
pygame.display.set_caption('Snake game')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if playing:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if key_pressed != 'down':
                        key_pressed = 'up'
                if event.key == pygame.K_DOWN:
                    if key_pressed != 'up':
                        key_pressed = 'down'
                if event.key == pygame.K_LEFT:
                    if key_pressed != 'right':
                        key_pressed = 'left'
                if event.key == pygame.K_RIGHT:
                    if key_pressed != 'left':
                        key_pressed = 'right'
        if not playing:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if begin:
                        begin = False

                    reset()
                    playing = True
    if begin:
        draw_start_screen()
    else:
        if playing:
            print(len(tails))


            if check_collision():
                generate_food_at_random_position()
                add_tail()

                score += 1

            update_tails()
            update_snake()

            if check_outside() or tail_collision():
                playing = False
                if score > highest_score:
                    highest_score = score
                continue

            screen.fill('black')
            draw_grid(screen)
            draw_tails()
            draw_snake(screen)
            draw_food(screen)
            draw_score()
        else:
            screen.fill('Black')
            draw_reset_screen()


    pygame.display.update()
    clock.tick(15)