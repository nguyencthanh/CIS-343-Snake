# 8-Bit Snake Game
# Created by: Thanh Nguyen, Hunter Sutton

# Assets Used (name, Url):
# apple and snake, https://opengameart.org/content/snake-game-assets


# All Imports
import pygame as game
from pygame.math import Vector2
import sys
import random
import os


# Classes Created
# This class is created as 'the fruit for the snake to eat'
class Fruit:
    def __init__(self):
        self.apple = game.image.load(os.path.join('Assets', 'Graphics/apple.png')).convert_alpha()
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.position = Vector2(self.x, self.y)

    @property
    def x_pos(self):
        return self.x

    @x_pos.setter
    def x_pos(self, x_pos):
        self.x = x_pos

    @property
    def y_pos(self):
        return self.y

    @y_pos.setter
    def y_pos(self, y_pos):
        self.y = y_pos

    def draw_fruit(self):
        fruit_rectangle = game.Rect(int(self.position.x * 40), int(self.position.y * 40), 40, 40)
        screen.blit(self.apple, fruit_rectangle)

    def move_fruit(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.position = Vector2(self.x, self.y)

# Powerups
# Powerups for the player to give them an edge.
# Power-up Class
class PowerUp:
    def __init__(self, snake):
        self.powerup_icon = game.image.load(os.path.join('Assets', 'Graphics/powerup.png')).convert_alpha()
        self.snake = snake
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.position = Vector2(self.x, self.y)

    @property
    def x_pos(self):
        return self.x

    @x_pos.setter
    def x_pos(self, x_pos):
        self.x = x_pos

    @property
    def y_pos(self):
        return self.y

    @y_pos.setter
    def y_pos(self, y_pos):
        self.y = y_pos

    def draw_powerup(self):
        powerup_rectangle = game.Rect(int(self.position.x * 40), int(self.position.y * 40), 40, 40)
        screen.blit(self.powerup_icon, powerup_rectangle)

    def move_powerup(self):
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.position = Vector2(self.x, self.y)
        for _ in range(2):
            self.snake.add_body()


# The Player
class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.x = 1
        self.y = 0
        self.direction = Vector2(self.x, self.y)
        self.new_body = False

        # Images
        self.head_up = game.image.load(os.path.join('Assets', 'Graphics/head_up.png')).convert_alpha()
        self.head_down = game.image.load(os.path.join('Assets', 'Graphics/head_down.png')).convert_alpha()
        self.head_left = game.image.load(os.path.join('Assets', 'Graphics/head_left.png')).convert_alpha()
        self.head_right = game.image.load(os.path.join('Assets', 'Graphics/head_right.png')).convert_alpha()

        self.body_bottomleft = game.image.load(os.path.join('Assets', 'Graphics/body_bottomleft.png')).convert_alpha()
        self.body_bottomright = game.image.load(os.path.join('Assets', 'Graphics/body_bottomright.png')).convert_alpha()
        self.body_topleft = game.image.load(os.path.join('Assets', 'Graphics/body_topleft.png')).convert_alpha()
        self.body_topright = game.image.load(os.path.join('Assets', 'Graphics/body_topright.png')).convert_alpha()

        self.body_horizontal = game.image.load(os.path.join('Assets', 'Graphics/body_horizontal.png')).convert_alpha()
        self.body_vertical = game.image.load(os.path.join('Assets', 'Graphics/body_vertical.png')).convert_alpha()

        self.tail_down = game.image.load(os.path.join('Assets', 'Graphics/tail_down.png')).convert_alpha()
        self.tail_up = game.image.load(os.path.join('Assets', 'Graphics/tail_up.png')).convert_alpha()
        self.tail_right = game.image.load(os.path.join('Assets', 'Graphics/tail_right.png')).convert_alpha()
        self.tail_left = game.image.load(os.path.join('Assets', 'Graphics/tail_left.png')).convert_alpha()

    @property
    def change_x(self):
        return self.x

    @change_x.setter
    def change_x(self, x_pos):
        self.x = x_pos

    @property
    def change_y(self):
        return self.y

    @change_y.setter
    def change_y(self, y_pos):
        self.y = y_pos

    def update_game(self):
        self.direction = Vector2(self.x, self.y)

    def draw_snake(self):
        self.update_graphics_head()
        self.update_graphics_tail()

        for index, square in enumerate(self.body):
            x_position = int(square.x * 40)
            y_position = int(square.y * 40)
            snake_rectangle = game.Rect(x_position, y_position, 40, 40)

            if index == 0:
                screen.blit(self.head, snake_rectangle)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, snake_rectangle)
            else:
                prev_square = self.body[index + 1] - square
                next_square = self.body[index - 1] - square
                if prev_square.x == next_square.x:
                    screen.blit(self.body_vertical, snake_rectangle)
                if prev_square.y == next_square.y:
                    screen.blit(self.body_horizontal, snake_rectangle)
                else:
                    if prev_square.x == -1 and next_square.y == -1 or prev_square.y == -1 and next_square.x == -1:
                        screen.blit(self.body_topleft, snake_rectangle)
                    if prev_square.x == -1 and next_square.y == 1 or prev_square.y == 1 and next_square.x == -1:
                        screen.blit(self.body_bottomleft, snake_rectangle)
                    if prev_square.x == 1 and next_square.y == -1 or prev_square.y == -1 and next_square.x == 1:
                        screen.blit(self.body_topright, snake_rectangle)
                    if prev_square.x == 1 and next_square.y == 1 or prev_square.y == 1 and next_square.x == 1:
                        screen.blit(self.body_bottomright, snake_rectangle)

    def update_graphics_head(self):
        head_position = self.body[1] - self.body[0]

        if head_position == Vector2(0, 1):
            self.head = self.head_up
        elif head_position == Vector2(0, -1):
            self.head = self.head_down
        elif head_position == Vector2(-1, 0):
            self.head = self.head_right
        elif head_position == Vector2(1, 0):
            self.head = self.head_left

    def update_graphics_tail(self):
        tail_position = self.body[-2] - self.body[-1]

        if tail_position == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_position == Vector2(0, -1):
            self.tail = self.tail_down
        elif tail_position == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_position == Vector2(1, 0):
            self.tail = self.tail_left

    def move_up(self):
        main_game.snake.change_x = 0
        main_game.snake.change_y = -1
        main_game.snake.update_game()

    def move_down(self):
        main_game.snake.change_x = 0
        main_game.snake.change_y = 1
        main_game.snake.update_game()

    def move_left(self):
        main_game.snake.change_x = -1
        main_game.snake.change_y = 0
        main_game.snake.update_game()

    def move_right(self):
        main_game.snake.change_x = 1
        main_game.snake.change_y = 0
        main_game.snake.update_game()

    def move(self):
        if self.new_body:
            copy_body = self.body[:]
            copy_body.insert(0, copy_body[0] + self.direction)
            self.body = copy_body[:]
            self.new_body = False
        else:
            copy_body = self.body[:-1]
            copy_body.insert(0, copy_body[0] + self.direction)
            self.body = copy_body[:]

    def add_body(self):
        self.new_body = True

    def reset_game(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_body = False


# The scoreboard
class Scoreboard:
    def __init__(self):
        self.font = game.font.Font('Font/Andale Mono.ttf', 25)
        self.scoreboard_x = int(740)
        self.scoreboard_y = int(760)

# Class of the whole logic
class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.scoreboard = Scoreboard()
        self.powerup = PowerUp(self.snake)

    def update(self):
        self.snake.move()
        self.fruit_collision()
        self.snake_collision()
        self.powerup_collision()

    def draw_element(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.display_score()
        self.powerup.draw_powerup()

    def fruit_collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.move_fruit()
            self.snake.add_body()
        elif self.powerup.position == self.snake.body[0]:
            self.powerup.move_powerup()
            
    def powerup_collision(self):
        if self.powerup.position == self.snake.body[0]:
            self.powerup.move_powerup()

    def snake_collision(self):
        if not 0 <= self.snake.body[0].x < 20 or not 0 <= self.snake.body[0].y < 20:
            self.game_over()

        for b in self.snake.body[1:]:
            if b == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset_game()

    def display_score(self):
        score = str(len(self.snake.body) - 3)
        score_surface = self.scoreboard.font.render(score, True, (56, 74, 12))
        score_rectangle = score_surface.get_rect(center=(self.scoreboard.scoreboard_x, self.scoreboard.scoreboard_y))
        screen.blit(score_surface, score_rectangle)


# Main Code Method
game.init()
game_screen = 800
screen = game.display.set_mode((game_screen, game_screen))
game.display.set_caption("Snake")
clock = game.time.Clock()
fps = 60

update_screen = game.USEREVENT
game.time.set_timer(update_screen, 150)

main_game = Main()

while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()
            sys.exit()
        if event.type == update_screen:
            main_game.update()
        if event.type == game.KEYDOWN:
            if event.key == game.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.move_up()
            if event.key == game.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.move_right()
            if event.key == game.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.move_down()
            if event.key == game.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.move_left()

    screen.fill((124, 252, 0))
    main_game.draw_element()
    game.display.update()
    clock.tick(fps)
