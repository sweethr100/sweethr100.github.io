import pygame
import random

pygame.init()

screen_width = 288
screen_height = 512

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

bird_img = pygame.image.load("bird.png")
bird_width = bird_img.get_width()
bird_height = bird_img.get_height()

pipe_img = pygame.image.load("pipe.png")
pipe_width = pipe_img.get_width()
pipe_height = pipe_img.get_height()
pipe_min = 100
pipe_max = 300
gap_size = 100
pipe_speed = 2

gravity = 0.25

bird_x = 50
bird_y = 200
bird_speed = 0

pipes = []
for i in range(3):
    pipes.append({
        "x": screen_width + i * (screen_width + pipe_width) / 3,
        "y": random.randint(pipe_min, pipe_max)
    })

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed -= 5

    screen.fill((255, 255, 255))

    for pipe in pipes:
        pipe["x"] -= pipe_speed

        if pipe["x"] < -pipe_width:
            pipe["x"] = screen_width
            pipe["y"] = random.randint(pipe_min, pipe_max)

        screen.blit(pipe_img, (pipe["x"], pipe["y"] - pipe_height - gap_size))
        screen.blit(pygame.transform.flip(pipe_img, False, True), (pipe["x"], pipe["y"] + gap_size))

    bird_y += bird_speed
    bird_speed += gravity

    screen.blit(bird_img, (bird_x, bird_y))

    if bird_y > screen_height or bird_y < -bird_height:
        game_over = True

    for pipe in pipes:
        if bird_x + bird_width > pipe["x"] and bird_x < pipe["x"] + pipe_width:
            if bird_y < pipe["y"] or bird_y + bird_height > pipe["y"] + gap_size:
                game_over = True

    pygame.display.update()

pygame.quit()