import pygame
from pygame import *

import random

pygame.init()


white = (255, 255, 255, 100)
red = (255, 0, 0)
green = (0, 155, 0)
black = (0, 0, 0)

display_width = 800
display_height = 600

snake_size = 20

FPS = 5
font = pygame.font.SysFont(None, 25)
img = pygame.image.load("C:/Users/Pavan/Documents/snakehead.png")
appimg = pygame.image.load("C:/Users/Pavan/Documents/apple.png")

direction = 'left'


def snake(snake_size, snakelist):
    if direction == 'left':
        head = pygame.transform.rotate(img, 90)
    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
    if direction == 'up':
        head = pygame.transform.rotate(img, 0)
    if direction == 'down':
        head = pygame.transform.rotate(img, 180)
    game_display.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(game_display, green, [XnY[0], XnY[1], snake_size, snake_size])


def textobject(text, color):
    txtsurface = font.render(text, True, color)
    return txtsurface, txtsurface.get_rect()


def display_message(message, color):
    txtsurface, txtrect = textobject(message, color)
    txtrect.center = (display_width / 2), (display_height / 2)
    game_display.blit(txtsurface, txtrect)


clock = pygame.time.Clock()
game_display = pygame.display.set_mode((display_width, display_height))


def gameLoop():
    global direction
    Apple_X = random.randrange(snake_size, display_width - snake_size, 20)
    Apple_Y = random.randrange(snake_size, display_height - snake_size, 20)
    snakelist = []
    snakelength = 1
    game_exit = False
    c_x = 0
    c_y = 0
    x = display_width / 2
    y = display_height / 2

    game_over = False
    while not game_exit:
        while game_over == True:
            display_message("Press C to Continue Or Press Q to Quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_exit = True

                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quit")
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    c_x = -snake_size
                    c_y = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    c_x = snake_size
                    c_y = 0
                elif event.key == pygame.K_UP:
                    direction = 'up'
                    c_y = -snake_size
                    c_x = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    c_y = snake_size
                    c_x = 0
        if x > display_width - snake_size or x < 0 or y > display_height - snake_size or y < 0:
            game_over = True

        x = x + c_x
        y = y + c_y

        game_display.fill(white)
        pygame.draw.rect(game_display, green, [Apple_X, Apple_Y, snake_size, snake_size])
        game_display.blit(appimg, [Apple_X, Apple_Y])

        snakehead = []
        snakehead.append(x)
        snakehead.append(y)
        snakelist.append(snakehead)
        if len(snakelist) > snakelength:
            del snakelist[0]
        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                game_over = True
        snake(snake_size, snakelist)
        pygame.display.update()
        if x == Apple_X and y == Apple_Y:
            Apple_X = random.randrange(0, display_width - snake_size, 20)
            Apple_Y = random.randrange(0, display_height - snake_size, 20)
            snakelength += 1

        clock.tick(FPS)
    quit()


gameLoop()
